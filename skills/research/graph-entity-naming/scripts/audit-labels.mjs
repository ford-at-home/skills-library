#!/usr/bin/env node
/**
 * Find knowledge-graph nodes whose label cannot identify them.
 *
 *   node audit-labels.mjs [dir]
 *
 * With no argument it looks for this pillar's own `knowledge-graph/data`, then
 * for the site's `rvahacks/public/knowledge-graph/data`, which holds all eight
 * graphs. A directory containing graph.json is read directly; a directory of
 * such directories is read as a set.
 *
 * Exits 1 when anything is found, so it can gate a publish.
 */
import { readdirSync, statSync, existsSync, readFileSync } from 'node:fs';
import { resolve, join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));

const CANDIDATES = [
  process.argv[2],
  resolve(HERE, '../../../knowledge-graph/data'),
  resolve(HERE, '../../../../../rvahacks/public/knowledge-graph/data'),
].filter(Boolean);

const root = CANDIDATES.find((p) => existsSync(p));
if (!root) {
  console.error('no graph data found; pass a directory containing graph.json');
  process.exit(2);
}

/** Every graph.json under `dir`, whether it is one graph or a set of them. */
function graphs(dir) {
  if (existsSync(join(dir, 'graph.json'))) return [['.', join(dir, 'graph.json')]];
  return readdirSync(dir)
    .filter((d) => statSync(join(dir, d)).isDirectory())
    .map((d) => [d, join(dir, d, 'graph.json')])
    .filter(([, f]) => existsSync(f));
}

/**
 * Each rule is a label that shipped once. Real Richmond names that would
 * otherwise trip a rule are excused rather than the rule being weakened:
 * "3-1-1" is a phone number, "Last-Modified" is an HTTP header.
 */
const REAL = /^(3-1-1|If-Modified-Since|Last-Modified|Sunrise-Sunset|Remit-Online)$/;

const RULES = [
  // Only the apparatus that produced the corpus. A model or library the
  // research genuinely discusses ("GPT-4o-mini", "PyMuPDF") is an accurate
  // label and an off-brief-relevance question, not a naming defect.
  ['named after the research apparatus', (l) => /parallel[- ]?research|^(llm|ai) (extraction|research|analysis)$/i.test(l)],
  ['title-cased directory slug', (l) => /^[A-Z][a-z]+(-[A-Z][a-z]+)+$/.test(l) && !REAL.test(l)],
  ['raw lowercase slug', (l) => /^[a-z0-9]+(-[a-z0-9]+){2,}$/.test(l) && !REAL.test(l)],
  ['snake_case identifier', (l) => /^[a-z]+(_[a-z]+)+$/.test(l)],
  ['untrimmed whitespace', (l) => l !== l.trim()],
  // UnknownEntity is exempt: naming a known-unknown ("Unknown GPS system
  // vendor") is deliberate here, and better than omitting the gap.
  ['placeholder for a missing answer', (l, t) => t !== 'UnknownEntity'
    && /^(n\/a|none|unknown|tbd|todo|not specified|no information)\b/i.test(l)],
  ['empty or near-empty', (l) => l.trim().length < 3],
];

let found = 0;

for (const [name, file] of graphs(root)) {
  const g = JSON.parse(readFileSync(file, 'utf8'));
  const hits = [];

  for (const [rule, test] of RULES) {
    for (const n of g.nodes) if (test(n.label, n.type)) hits.push([rule, n]);
  }

  // A label shared by several nodes cannot tell them apart. Bare hostnames are
  // the usual cause: a citation with no title falls back to its domain.
  const byLabel = new Map();
  for (const n of g.nodes) byLabel.set(n.label, (byLabel.get(n.label) ?? 0) + 1);
  for (const [label, count] of byLabel) {
    if (count > 3) hits.push([`shared by ${count} nodes`, { label, type: '—' }]);
  }

  if (!hits.length) continue;
  found += hits.length;
  console.log(`\n${name} (${g.nodes.length} nodes)`);
  for (const [rule, n] of hits.slice(0, 25)) {
    console.log(`  ${rule.padEnd(34)} ${String(n.type).padEnd(16)} ${JSON.stringify(n.label).slice(0, 72)}`);
  }
  if (hits.length > 25) console.log(`  … and ${hits.length - 25} more`);
}

if (!found) {
  console.log(`no unusable labels found in ${root}`);
  process.exit(0);
}
console.log(`\n${found} label(s) need attention — fix in the extractor, not in the data`);
process.exit(1);
