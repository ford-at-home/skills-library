---
name: aws-deploy
description: "This skill automates the complete deployment lifecycle:"
---

# AWS Deploy & Verify

Automated CDK deployment workflow with verification and health checks.

## Description

This skill automates the complete deployment lifecycle:
1. Runs CDK deploy with proper profile and approval settings
2. Captures deployment output to log file
3. Verifies deployment succeeded
4. Extracts stack outputs (API URL, bucket name, etc.)
5. Runs basic health checks on deployed resources

## When to Use

- After making code changes to Lambda functions
- After updating CDK infrastructure definitions
- Before running benchmark tests to ensure latest code is deployed
- After fixing bugs that require redeployment

## Usage

```bash
claude-flow run aws-deploy
```

## Optional Parameters

```bash
# Specify custom log file name
claude-flow run aws-deploy --log-name "my-deployment"

# Skip health checks (faster)
claude-flow run aws-deploy --skip-checks
```

## Implementation

```python
import subprocess
import json
import time
import sys
import os

# Configuration
PROFILE = "mvp"
REGION = "us-east-1"
INFRA_DIR = "~/Development/GitHub/socratic-ai-benchmarks/serverless/infra"
LOG_NAME = os.getenv("LOG_NAME", "deployment")
SKIP_CHECKS = os.getenv("SKIP_CHECKS", "false").lower() == "true"

print("🚀 Starting AWS CDK deployment...\n")

# Step 1: Run CDK deploy
log_file = f"/tmp/cdk-deploy-{LOG_NAME}.log"
print(f"Step 1: Deploying stack (log: {log_file})...")

deploy_cmd = f"cd {INFRA_DIR} && cdk deploy --profile {PROFILE} --require-approval never 2>&1 | tee {log_file}"

result = subprocess.run(deploy_cmd, shell=True, capture_output=False)

if result.returncode != 0:
    print(f"\n❌ Deployment failed! Check log: {log_file}")
    sys.exit(1)

print("✅ Deployment completed\n")

# Step 2: Extract stack outputs
print("Step 2: Extracting stack outputs...")

with open(log_file, 'r') as f:
    log_content = f.read()

outputs = {}
for line in log_content.split('\n'):
    if 'SocraticBenchStack.' in line and '=' in line:
        parts = line.split('=', 1)
        if len(parts) == 2:
            key = parts[0].strip().replace('SocraticBenchStack.', '')
            value = parts[1].strip()
            outputs[key] = value

print(f"✅ Extracted {len(outputs)} outputs:")
for key, value in outputs.items():
    print(f"   {key}: {value}")
print()

# Step 3: Health checks
if not SKIP_CHECKS:
    print("Step 3: Running health checks...")

    import boto3
    session = boto3.Session(profile_name=PROFILE)

    # Check Lambda function
    lambda_client = session.client('lambda', region_name=REGION)
    try:
        response = lambda_client.get_function(FunctionName='SocraticBenchStack-ApiFunction')
        last_modified = response['Configuration']['LastModified']
        print(f"   ✅ API Lambda updated: {last_modified}")
    except Exception as e:
        print(f"   ⚠️  Lambda check failed: {e}")

    # Check API endpoint
    if 'ApiUrl' in outputs:
        import requests
        try:
            response = requests.get(f"{outputs['ApiUrl']}/health", timeout=5)
            if response.status_code == 200:
                print(f"   ✅ API health check passed")
            else:
                print(f"   ⚠️  API returned {response.status_code}")
        except Exception as e:
            print(f"   ⚠️  API check failed: {e}")

    # Check DynamoDB table
    if 'TableName' in outputs:
        dynamodb = session.client('dynamodb', region_name=REGION)
        try:
            response = dynamodb.describe_table(TableName=outputs['TableName'])
            status = response['Table']['TableStatus']
            print(f"   ✅ DynamoDB table status: {status}")
        except Exception as e:
            print(f"   ⚠️  DynamoDB check failed: {e}")

    # Check S3 bucket
    if 'BucketName' in outputs:
        s3 = session.client('s3', region_name=REGION)
        try:
            s3.head_bucket(Bucket=outputs['BucketName'])
            print(f"   ✅ S3 bucket accessible")
        except Exception as e:
            print(f"   ⚠️  S3 check failed: {e}")

    print()

print(f"🎯 Deployment complete! Stack outputs saved.")
print(f"   API URL: {outputs.get('ApiUrl', 'N/A')}")
print(f"   UI URL: {outputs.get('UIUrl', 'N/A')}")
```

## Output

```
🚀 Starting AWS CDK deployment...

Step 1: Deploying stack (log: /tmp/cdk-deploy-deployment.log)...
✅ Deployment completed

Step 2: Extracting stack outputs...
✅ Extracted 6 outputs:
   ApiKeyId: 0qwosllwel
   ApiUrl: https://wcyf23uxxe.execute-api.us-east-1.amazonaws.com/prod/
   BucketName: socratic-bench-data-<aws-account-id>
   EventBusName: socratic-bench
   TableName: socratic_core
   UIUrl: https://<cloudfront-domain>

Step 3: Running health checks...
   ✅ API Lambda updated: 2025-11-08T05:02:05.000+0000
   ✅ API health check passed
   ✅ DynamoDB table status: ACTIVE
   ✅ S3 bucket accessible

🎯 Deployment complete! Stack outputs saved.
   API URL: https://wcyf23uxxe.execute-api.us-east-1.amazonaws.com/prod/
   UI URL: https://<cloudfront-domain>
```

## Notes

- Uses AWS profile 'mvp' - ensure credentials are configured
- Requires `boto3` Python package
- Deployment logs saved to `/tmp/cdk-deploy-{name}.log`
- Health checks verify Lambda, API, DynamoDB, and S3
- Use `--skip-checks` to deploy faster without verification
