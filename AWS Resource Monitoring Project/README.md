# AWS Resource Monitoring System

This project demonstrates how I implemented a real-time monitoring and alerting system for Amazon EC2 instances using Amazon CloudWatch. The goal was to build a monitoring solution that detects performance issues, notifies engineers, and automatically recovers an unhealthy server.

---

##  Project Overview

As part of this assignment, I configured a complete monitoring workflow that includes:

- A CloudWatch dashboard for key EC2 metrics  
- CloudWatch alarms for CPU and memory utilization  
- SNS email notifications for high CPU usage  
- An EC2 automatic reboot action when memory usage exceeds a defined threshold  

These components work together to create a simple **self-healing infrastructure**, which is commonly used in production environments.

---

## 🛠 Components Implemented

### **1. CloudWatch Dashboard**
Created a custom dashboard to visualize:
- CPU utilization  
- Memory utilization  
- Additional EC2 metrics  

This provides a clear, centralized view of instance health.

---

### **2. CPU Utilization Alarm (SNS Email Alert)**
Configured a CloudWatch alarm that triggers when CPU usage is high.  
When the threshold is crossed:
- An Amazon SNS topic sends an email notification to subscribed users.  

This setup reflects real-world incident alerting systems used by cloud operations teams.

---

### **3. Memory Utilization Alarm**
Created a memory utilization alarm that detects when memory usage exceeds **300 MB (300,000,000 bytes)**.

This helps identify memory leaks or applications that consume excessive memory.

---

### **4. EC2 Automatic Reboot (Self-Healing Action)**
Attached an **EC2 Reboot** action to the memory alarm.  
If memory usage remains above the threshold:
- CloudWatch automatically reboots the EC2 instance.  

This simulates a basic self-recovery mechanism used to maintain system stability without manual intervention.

---

##  Technologies Used

- **Amazon CloudWatch** (Metrics, Dashboards, Alarms)  
- **Amazon SNS** (Email Notifications)  
- **Amazon EC2** (Reboot actions)  
- **IAM Roles & Policies** (Permissions for actions)

---

##  Key Learnings

Through this project, I gained hands-on experience in:

- Building operational dashboards for EC2 monitoring  
- Designing and configuring CloudWatch alarms  
- Integrating SNS for automated alerting  
- Implementing automatic recovery actions  
- Understanding how self-healing infrastructure is built on AWS  

These are essential skills for Cloud, DevOps, and Site Reliability Engineering roles.

---

##  Files Included
- `README.md`  
- (Optional) Screenshots of dashboard, alarms, and SNS setup  

---


This project showcases how to combine CloudWatch, SNS, and EC2 actions to create an automated monitoring and recovery system.

