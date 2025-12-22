# Production-Grade AWS Auto Scaling – Behavioral & Cost Analysis

## 1. Project Overview

This project was built to study real-world AWS Auto Scaling behavior through measured observation rather than assumptions or tutorial-driven deployment. The primary focus was on understanding how infrastructure responds to traffic, how scaling decisions are made, and how capacity can be right-sized safely using observable metrics.

The project intentionally explores:
- Auto Scaling behavior under sustained load
- Metric-driven decision making
- Cost optimization through right-sizing
- Fault tolerance and self-healing
- Debugging real infrastructure misconfigurations

This project does not attempt to benchmark maximum throughput, implement complex application logic, or represent large-scale enterprise production ownership.

---

## 2. Architecture Overview

The system follows a standard, production-style AWS architecture designed for clarity and observability.

- VPC spanning multiple Availability Zones with public and private subnets
- Internet-facing Application Load Balancer in public subnets
- Auto Scaling Group launching EC2 instances in private subnets
- NAT Gateway enabling outbound internet access
- CloudWatch for metrics and dashboards
- VPC Flow Logs for network traffic validation

The architecture was intentionally kept minimal to ensure scaling signals, latency behavior, and cost implications were easy to observe and reason about.

---

## 3. Auto Scaling Behavior Analysis

Auto Scaling was configured using CPU-based target tracking with a 50% utilization target.

Observed behavior:
- Scale-out occurred only when CPU utilization was sustained above the target
- Scale-in was conservative and delayed due to stabilization windows and cooldowns
- Capacity was not immediately reduced after traffic dropped, preventing oscillation

Traffic volume alone was not treated as a scaling signal. Scaling decisions were based on resource pressure, not request count.

---

## 4. Metrics & Observability

Decisions were driven by interpreting multiple CloudWatch metrics together:

- CPUUtilization as the primary indicator of resource pressure
- RequestCount to understand traffic volume
- TargetResponseTime evaluated only under sustained traffic
- HTTP 2XX responses to confirm availability and health

At stable traffic levels, CPU utilization remained low, latency showed no sustained upward trend, and 2XX responses were consistent. This indicated excess unused capacity rather than performance constraints.

---

## 5. Cost Optimization & Right-Sizing

The project began in an intentionally over-provisioned state.

Right-sizing was performed iteratively:
- Initial state: 2 × t3.micro
- Reduced to 1 × t3.micro after observing low utilization
- Further reduced to t3.nano after confirming continued excess capacity

Each change was validated by re-analyzing metrics to ensure no impact on availability or performance.

---

## 6. Failure Scenarios & Debugging

### Incident: Target Group Health Check Failure

**Root Cause**  
A Network ACL misconfiguration on the private subnet prevented inbound health check traffic from reaching EC2 instances.

**Impact**  
- ALB marked all targets as unhealthy
- Traffic was not routed to instances despite them running

**Resolution**  
- Corrected Network ACL association and rules
- Verified inbound and outbound traffic paths
- Health checks passed immediately after correction

**Lessons Learned**  
Network-layer misconfigurations can cause silent failures that are not visible at the instance or application level.

---

## 7. Availability & Self-Healing Validation

Instances were intentionally terminated while the Auto Scaling Group maintained a desired capacity greater than one.

Observed behavior:
- Replacement instances were launched automatically
- Capacity was restored without manual intervention
- No service disruption occurred

This confirmed expected self-healing behavior across Availability Zones.

---

## 8. VPC Flow Logs & Network Validation

VPC Flow Logs were enabled to validate network behavior and investigate traffic flow.

Analysis confirmed:
- Expected inbound and outbound traffic patterns
- No unexpected rejected traffic
- No indicators requiring IP blocking

---

## 9. Key Learnings

- Over-provisioning is identified through unused capacity, not failure
- Scaling signals must be interpreted in context
- Latency metrics are meaningful only under sustained load
- Conservative scale-in behavior is intentional
- Cost optimization should follow measurement
- Simplicity improves observability and decision-making

---

## 10. Project Status & Cost Control

All AWS resources were intentionally decommissioned after project completion to avoid unnecessary cloud costs.

---

## Final Note

This project reflects a behavior-driven approach to cloud infrastructure design, emphasizing observation, analysis, and engineering judgment over service quantity or complexity.
