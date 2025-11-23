# Highly Available Web Application on AWS

This project demonstrates how to design and deploy a **highly available, fault-tolerant web application** using core AWS services such as **EC2, Auto Scaling Groups, Application Load Balancer (ALB), RDS Multi-AZ, Route 53**, and **CloudFront**.  
The goal was to ensure the application remains accessible even if individual instances or entire Availability Zones fail.

---

##  Project Overview

The project started with a simple, non-highly available setup:
- 1 EC2 instance  
- Auto Scaling Group with desired capacity = 1  
- No load balancer  
- Any instance failure caused downtime  

I upgraded this architecture to a **multi-AZ production-grade system** with automatic failover, load balancing, and self-healing.

---

##  What I Built

### **1️ Application Load Balancer Across 3 Availability Zones**
- Created an **Application Load Balancer (ALB)** deployed across **AZ-A, AZ-B, and AZ-C**.
- Ensures traffic automatically shifts to healthy instances during failures.

### **2️ Secure Networking Configuration**
- **ALB Security Group** allows **public HTTP (port 80)**.
- **EC2 Security Group** allows inbound traffic **only from ALB**, improving security.
- Enforced least-privilege access between all components.

### **3️ Target Group & Health Checks**
- Configured health checks to automatically detect unhealthy EC2 instances.
- ALB stops sending traffic to unhealthy instances until recovered or replaced.

### **4️ Auto Scaling Group Enhancements**
- Integrated the ASG with the ALB.
- Added **multiple AZs** to the ASG to ensure multi-zone resilience.
- Updated scaling policies for faster replacement of failed instances.

### **5️ Self-Healing Test**
To validate the architecture:
- I manually terminated the running EC2 instance.
- Auto Scaling immediately launched a new instance.
- ALB routed traffic only to healthy targets.

**Result: Application stayed online with zero manual intervention.**

---

##  Final Architecture Components

- **Amazon Route 53** – DNS routing  
- **Amazon CloudFront** – global performance boost  
- **Application Load Balancer (ALB)** – traffic distribution  
- **Auto Scaling Group** – self-healing + scaling  
- **EC2 Instances** – web server layer  
- **Amazon RDS Multi-AZ** – database failover  
- **Amazon S3** – static file hosting  
- **Amazon CloudWatch** – monitoring & alarms  

---

##  What I Learned

- How to design **highly available systems** using multi-AZ best practices  
- How **ALB + Auto Scaling** work together for uptime and load distribution  
- Setting up secure VPC networking using **Security Groups, NACLs, routing**  
- Understanding **health checks** and how they influence routing  
- The importance of redundancy and **self-healing architecture**  
- How to test failover and validate high availability in real time  

---

##  Summary

This project strengthened my AWS cloud architecture skills with hands-on experience in:
- EC2  
- Auto Scaling  
- ALB  
- RDS Multi-AZ  
- VPC networking  
- Fault tolerance & self-healing  
- Distributed architecture design  

This aligns closely with real-world production architectures used by global systems.


