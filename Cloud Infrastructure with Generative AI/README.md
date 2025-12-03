#  Cloud Infrastructure with Generative AI

A fully automated cloud infrastructure deployed using **AWS CDK**, **Generative AI (Amazon Q Developer)**, and **CloudFormation**.  
This project demonstrates how developers can use GenAI to accelerate Infrastructure-as-Code, automate provisioning, and standardize cloud deployments.

---



##  What This Project Demonstrates

### **1. CDK Application Bootstrapping**
- Initialized a Python-based AWS CDK application  
- Installed dependencies and configured virtual environments  
- Used **Amazon Q Developer** to generate, refine, and troubleshoot CDK constructs

---

### **2. Network Architecture Design**
Built a secure and scalable network following AWS best practices:

- Multi-AZ **VPC**
- **Public**, **Private With Egress**, and **Isolated** subnets  
- **Internet Gateway (IGW)**  
- **NAT Gateway** for outbound traffic  
- Automatically generated route tables and associations  

---

### **3. Compute Layer**
Provisioned compute resources with IaC:

- **Amazon Linux 2023 EC2 instances**  
- EC2 instances placed in private subnets  
- Startup automation via **User Data**  
- Attached IAM instance roles  
- Created a second EC2 instance in a different Availability Zone for load balancing  

---

### **4. Security Design**
Implemented least-privilege, segmented security:

- Dedicated security groups for:
  - Application Load Balancer  
  - EC2 instances  
  - RDS cluster  
- Strict inbound rules:
  - ALB → EC2 (HTTP/80 or custom ports)  
  - EC2 → RDS (MySQL/3306)  
- Outbound rules controlled by default SG and route tables  

---

### **5. Application Load Balancer**
Configured a production-ready ALB:

- Deployed across multiple Availability Zones  
- Listener on port **80**  
- Target group configured with the **new EC2 instance**  
- Health checks to validate application availability  

---

### **6. Automated Deployment**
- Generated CloudFormation templates using **`cdk synth`**  
- Deployed all resources with **`cdk deploy`**  
- Verified infrastructure creation in the AWS Console  

---

### **7. Application Verification**
Validated end-to-end application behavior:

- Retrieved ALB DNS endpoint  
- Confirmed successful HTTP response from backend EC2 instance  
- Verified:
  - ALB → EC2 connectivity  
  - EC2 → RDS connection  
  - NAT → Public internet routing  
  - Multi-AZ failover readiness  

---

##  Core AWS Services Used

- Amazon VPC  
- EC2 (Amazon Linux 2023)  
- Application Load Balancer  
- NAT Gateway  
- Security Groups  
- IAM Roles  
- RDS Aurora MySQL  
- AWS CDK (Python)  
- Amazon Q Developer  
- CloudFormation  

---

##  Key Learnings

- Converting natural language into CDK code using Amazon Q  
- Automating multi-tier cloud architectures with IaC  
- Implementing secure, multi-AZ designs  
- Troubleshooting CDK synthesis and deployment  
- Integrating ALB → EC2 → RDS using AWS best practices  
- Understanding real-world cloud infrastructure workflows  

---
