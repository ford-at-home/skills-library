# Brief: <piece-name>

<!--
Required input for every run. No brief, no run.

Fill in every field. An empty field is a stop condition, not a default.
Delete the guidance comments as you go.
-->

## Voice

<!--
A bare name resolves as ./.voices/<name>.md, then ~/.voices/<name>.md.
The paired <name>.anti.md beside it is loaded too whenever it exists.
A path is used as given.
-->

<voice-name-or-path>

## Persona

<!--
ONE human who reads this. Not a segment, not a job title, not "our audience".
Give them a situation, a belief they already hold, and something they are
already tired of hearing.

Good: "a staff engineer who inherited a service nobody owns, has already
written the runbooks once, watched them rot, and suspects the problem is
organizational but cannot argue it to their VP."

Bad: "engineers", "technical decision makers", "people who care about quality".
-->

<one-named-human>

## Throughline

<!--
ONE sentence. What this person walks away with — not what the piece is about.
If it takes two sentences, the piece is not ready, or it is two pieces.

Test: could a paragraph fail this? If no paragraph could fail it, it is a
topic, not a throughline.
-->

<one-sentence>

## Channels

<!--
One per line. Each name must resolve to a channel definition at
./.channels/<name>.md or ~/.channels/<name>.md, which supplies length,
register, format, and output filename.
-->

- <channel-name>

## Why this persona, why now

<!--
ONE paragraph. The stakes. Why does it matter that this lands, for this
person, at this moment? What changes for them if it does?

This is the field people skip and the field that does the most work. Without
it the piece reads as content. With it, it reads as a letter from someone who
had a reason to write.
-->

<one-paragraph>
