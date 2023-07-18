# Nostr Serverless API

This repository contains a Dockerized Flask application and an AWS CloudFormation template to deploy the application to AWS Lambda and expose it via Amazon API Gateway.
![Figure 1: System Architecture Diagram](https://github.com/garyokeeffe/NSA/blob/main/resources/NostrServerlessAPI.png?raw=true "Figure 1: System Architecture Diagram")



## Prerequisites

- An AWS account
- Docker installed
- AWS CLI installed and configured with your AWS credentials.

## Deployment

1. **Build and push the Docker image**:

    Make sure Docker is running on your machine. Then, navigate to the directory containing the Dockerfile and run the following commands, replacing ACCOUNT_ID with your AWS account ID and REGION with your AWS region:

   ```bash
    aws ecr get-login-password --region REGION | docker login --username AWS --password-stdin ACCOUNT_ID.dkr.ecr.REGION.amazonaws.com
    docker build -t nostr-app .
    docker tag nostr-app:latest ACCOUNT_ID.dkr.ecr.REGION.amazonaws.com/nostr-app:latest
    # The following command is only necessary if the ECR repository does not already exist.
    aws ecr create-repository --repository-name nostr-app --region REGION
    docker push ACCOUNT_ID.dkr.ecr.REGION.amazonaws.com/nostr-app:latest
   ```

2. **Deploy the CloudFormation stack**:

   Navigate to the directory containing the CloudFormation template (`cloudformationtemplate.yaml`) and run the following command, replacing `STACK_NAME` with your desired CloudFormation stack name, `DOCKER_IMAGE_URI` with the URI of the Docker image you just pushed, and `NSEC_FORMATTED_PRIVATE_KEY` with a throwaway nostr account's private key:

   ```bash
   aws cloudformation deploy --template-file ./cloudformationtemplate.yaml --stack-name STACK_NAME --parameter-overrides DockerImageUri=DOCKER_IMAGE_URI NostrPrivateKey=NSEC_FORMATTED_PRIVATE_KEY --capabilities CAPABILITY_IAM --capabilities CAPABILITY_IAM
   ```

## Usage

After successful deployment, you can access the Flask application via the URL of the API Gateway that was created. You can find this URL in the Outputs section of the CloudFormation stack in the AWS Management Console. Hit the `/verify` endpoint to verify that the Nostr Serverless API has been successfully configured (this will post a message from your account to the following relays: "wss://nos.lol", "wss://nostr.bitcoiner.social", "wss://relay.damus.io"). If you need to confirm your API gateway URL, run the following command:
```bash
aws cloudformation describe-stacks --stack-name STACK_NAME --query 'Stacks[].Outputs'
```
(remember to replace `STACK_NAME` with the name of your stack (which is defined when you ran `aws cloudformation deploy` in the last step).