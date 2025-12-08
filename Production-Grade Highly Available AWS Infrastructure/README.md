# Production-Grade Highly Available AWS Infrastructure

This project implements a fully production-ready, scalable, and highly available cloud architecture on AWS. It follows real industry best practices and demonstrates end-to-end skills in VPC design, load balancing, auto scaling, security hardening, logging, monitoring, and global content delivery.

The system is architected across multiple Availability Zones and includes CloudFront, ALB, Auto Scaling Group, IAM roles, NACLs, WAF, S3 logging, CloudWatch dashboards, SNS alerts, and lifecycle automation.

---

##  Architecture Overview

This infrastructure includes:

- Custom VPC (10.0.0.0/16) with public and private subnets  
- Internet Gateway and NAT Gateway for controlled connectivity  
- Route tables for public/private routing separation  
- Network ACLs and Security Groups to enforce layered security  
- Application Load Balancer for traffic distribution  
- Auto Scaling Group with Launch Template for EC2 management  
- IAM role for EC2 using least-privilege permissions  
- AWS WAF attached to the ALB for threat protection  
- CloudFront distribution for global acceleration  
- S3 logging bucket with lifecycle rules  
- CloudWatch dashboards, metrics, and alarms  
- SNS notifications for operational alerts  

---

##  Key Features

### **1. Multi-AZ VPC Networking**
- VPC with public/private subnets across us-east-1a & 1b  
- Internet Gateway and NAT Gateway configured  
- Route tables and subnet associations  
- Custom NACLs for stateless subnet-level filtering  
- Troubleshot ASG failures and fixed ephemeral port issues using Amazon Q Developer  

### **2. Application Load Balancer**
- Internet-facing ALB with HTTP listener  
- Target group with health checks  
- Proper SG rules to control inbound/outbound traffic  

### **3. Auto Scaling Group**
- Launch Template (Amazon Linux 2023 + t2.micro)  
- ASG deployed in private subnets  
- Target tracking policy maintaining 60% CPU utilization  
- Ensures scalability and high availability  

### **4. IAM & Security**
- EC2 instance role with required permissions  
- ALB SG allows HTTP from the internet  
- EC2 SG allows HTTP only from ALB  
- NACLs designed for subnet isolation  

### **5. AWS WAF**
- Web ACL attached to ALB  
- Managed rule groups enabled (SQLi, Common Vulnerabilities, Bad Bots, etc.)  

### **6. CloudFront Distribution**
- ALB set as the origin  
- Optimized caching and compression  
- HTTPS enforcement and improved global performance  

### **7. Logging & Monitoring**
#### **S3 Logging**
- Dedicated S3 bucket for ALB access logs  
- Lifecycle transitions: IA → Glacier IR → Glacier Deep Archive → Expiration  

#### **CloudWatch**
- Custom dashboard monitoring:
  - Request Count  
  - 5XX Errors  
  - Target Response Time  
  - CPU Utilization  
  - Healthy Host Count  
- Alarms with SNS notifications  

---

##  What This Project Demonstrates

This project showcases real-world AWS cloud engineering capabilities:

- Designing highly available and secure cloud architectures  
- Implementing scalable compute environments with ASG  
- Applying layered security using IAM, SGs, NACLs, and WAF  
- Building global content delivery with CloudFront  
- Automating log storage and lifecycle management  
- Monitoring infrastructure health using CloudWatch  
- Troubleshooting using Amazon Q Developer  

  

---

##  Conclusion

This project represents a full end-to-end AWS production environment with high availability, security, monitoring, and performance optimization. It demonstrates hands-on cloud knowledge and practical deployment skills that align with real-world architecture standards.

---
