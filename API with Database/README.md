# API with Database – AWS Serverless Application

This project demonstrates how I built a fully serverless API using **Amazon DynamoDB**, **AWS Lambda**, and **Amazon API Gateway** as part of an AWS Skill Builder lab.  
The goal was to integrate a NoSQL database into a vehicle rental application and expose REST endpoints using API Gateway.

---

##  What I Did in This Lab

### **1️ Created a DynamoDB Table**
- Created a DynamoDB table named **`rental_app`**.
- Designed the table to store location and vehicle details.
- Configured the primary key for unique item identification.

### **2️ Created & Tested the Lambda Function**
- Created a Lambda function named **`JaswanthFunction`**.
- Wrote and deployed Lambda code that:
  - **POST** → Inserts or updates DynamoDB items  
  - **GET** → Retrieves records  
- Tested the Lambda function in the console to confirm database interactions work correctly.

### **3️ Built the REST API with API Gateway**
- Created a new REST API.
- Added the first resource: **`/location`**
  - Added **GET** method → fetch location records  
  - Added **POST** method → insert/update data  
  - Integrated both methods with the Lambda function using **Lambda Proxy Integration**  
- Added second resource: **`/vehicles`**
  - Added **POST** method → add vehicle data  
- Finally, **re-deployed the API** to make all updates live.

---

##  Architecture
Client Application

Amazon API Gateway

AWS Lambda

Amazon DynamoDB (rental_app)


---

##  API Endpoints

| Resource | Method | Description |
|----------|---------|-------------|
| `/location` | GET | Retrieve location information |
| `/location` | POST | Add or update location entries |
| `/vehicles` | POST | Insert vehicle details |

---

##  Skills Practiced

- DynamoDB NoSQL design  
- Lambda function development  
- API Gateway resource & method setup  
- Lambda Proxy Integration  
- Serverless CRUD operations  
- Deploying APIs to stages  
- Understanding AWS event-driven architecture  

---

##  Why This Project Matters

This architecture is commonly used in real-world applications such as:

- Car rental systems  
- Inventory management  
- Booking/Reservation systems  
- Mobile app backends  
- IoT device telemetry APIs  

It demonstrates **end-to-end serverless development**, which is a key skill for AWS Cloud Engineers and Backend Developers.

---




