# Deploying RESTful APIs on AWS (API Gateway + Lambda)

This project shows how I built and deployed a RESTful API using **Amazon API Gateway** and **AWS Lambda**. The main goal of this lab was to understand how serverless backend applications work and how API Gateway connects to Lambda to return JSON responses without managing any servers.

---

## Overview

I created a simple API with multiple endpoints and connected each one to a Lambda function. API Gateway handles incoming HTTP requests and triggers Lambda, which sends back a response. After setting everything up, I deployed the API and tested it to make sure each endpoint was working correctly.

---

## Architecture Flow

1. The client sends an HTTP GET request (example: `/pets` or `/vehicles`).
2. API Gateway receives the request and forwards it to the correct Lambda function.
3. The Lambda function runs the logic and returns a JSON response.
4. API Gateway sends the response back to the user or application.

This is a common pattern used in real-world serverless applications.

---

## What I Built

### 1. Created an API Gateway REST API
- Set up a REST API with routes such as `/pets` and `/vehicles`.
- Configured methods and responses.

### 2. Integrated API Gateway with Lambda
- Used **Lambda proxy integration** to pass full request data.
- Connected each route to a dedicated Lambda function.

### 3. Wrote Lambda Functions
- Created simple Python functions returning structured JSON.
- Used example data such as pet info and vehicle inventory.

### 4. Deployed and Tested the API
- Published the API using a deployment stage.
- Tested endpoints using the API Gateway console.
- Verified execution through CloudWatch logs.

---

## Technologies Used

- **Amazon API Gateway** (REST API)
- **AWS Lambda** (Python)
- **IAM Roles** (API Gateway → Lambda access)
- **Amazon CloudWatch** (Logs)

---

## What I Learned

- How API Gateway and Lambda work together in a serverless setup  
- How to build, deploy, and test REST APIs  
- How to return JSON responses using Lambda  
- How proxy integration works behind the scenes  
- How serverless architectures scale automatically  

This project gave me a solid foundation in building backend APIs using AWS serverless services.

---



