# Spot Instances in Cloud Computing

## What are Spot Instances?

Spot Instances are unused EC2 capacity offered at up to 90% discount compared to On-Demand prices. AWS can reclaim these instances with a 2-minute warning when capacity is needed.

## How Spot Instances Work

1. You request instances at current spot price
2. AWS provides instances while capacity available
3. If capacity needed, AWS sends 2-minute warning
4. Instance is terminated (you only pay for used time)

## Pricing Model

| Pricing Type | Discount | Interruption Risk   |
| ------------ | -------- | ------------------- |
| On-Demand    | 0%       | None                |
| Reserved     | 40-72%   | None                |
| Spot         | 60-90%   | Yes (2-min warning) |

**Price Fluctuation:**

- Prices change based on supply/demand
- Can set maximum price willing to pay
- No bidding - you get current spot price

## Spot Instance Best Practices

### 1. Design for Interruption

- Save state periodically
- Use checkpointing for long jobs
- Implement graceful shutdown handling
- Store data externally (S3, EFS)

### 2. Diversify Instance Types

```
Use multiple instance types and AZs:
- c5.large in us-east-1a
- c5.xlarge in us-east-1b
- c5a.large in us-east-1c
- m5.large in us-east-1a
```

More options = higher availability

### 3. Mix with On-Demand

**Mixed Instances Strategy:**

- Base capacity: On-Demand (reliable)
- Scaling capacity: Spot (cost-effective)
- Example: 4 On-Demand + up to 20 Spot

## Use Cases

### Good for Spot

- Batch processing jobs
- Big data analytics (EMR, Spark)
- CI/CD build workers
- Testing environments
- Containerized workloads
- Machine learning training
- Image/video rendering

### Not Good for Spot

- Production web servers
- Databases
- Single critical instances
- Stateful applications without checkpointing

## Handling Interruptions

### Termination Notice

AWS provides 2-minute warning via:

- Instance metadata service
- CloudWatch Events
- EventBridge

### Checking for Interruption

```bash
# Check instance metadata
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" \
  -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")

curl -H "X-aws-ec2-metadata-token: $TOKEN" \
  http://169.254.169.254/latest/meta-data/spot/termination-time
```

### Graceful Shutdown Script

```python
import requests
import time
import subprocess

def check_for_termination():
    try:
        token = requests.put(
            'http://169.254.169.254/latest/api/token',
            headers={'X-aws-ec2-metadata-token-ttl-seconds': '21600'}
        ).text

        response = requests.get(
            'http://169.254.169.254/latest/meta-data/spot/termination-time',
            headers={'X-aws-ec2-metadata-token': token}
        )

        if response.status_code == 200:
            return True  # Termination scheduled
    except:
        pass
    return False

def graceful_shutdown():
    # Save state
    subprocess.run(['app-checkpoint.sh'])
    # Drain connections
    subprocess.run(['nginx', '-s', 'quit'])
    # Deregister from load balancer
    # ...

while True:
    if check_for_termination():
        graceful_shutdown()
        break
    time.sleep(5)
```

## Spot Fleet

Request multiple Spot instance types simultaneously.

**Features:**

- Request capacity across instance types/AZs
- Automatic replacement of interrupted instances
- Mixed On-Demand and Spot

**Allocation Strategies:**

- **lowestPrice**: Cheapest instances first
- **diversified**: Spread across pools
- **capacityOptimized**: Least likely to be interrupted
- **priceCapacityOptimized**: Balance price and availability

## EC2 Fleet

Unified API for managing On-Demand, Reserved, and Spot.

```hcl
resource "aws_ec2_fleet" "example" {
  target_capacity_specification {
    default_target_capacity_type = "spot"
    total_target_capacity        = 10
    on_demand_target_capacity    = 2
    spot_target_capacity         = 8
  }

  spot_options {
    allocation_strategy = "capacity-optimized"
    maintenance_strategies {
      capacity_rebalance {
        replacement_strategy = "launch-before-terminate"
      }
    }
  }
}
```

## Capacity Rebalancing

**Launch-Before-Terminate:**

1. AWS detects elevated interruption risk
2. Launches replacement instance
3. Terminates at-risk instance after new one ready

Provides smoother transitions than 2-minute warning.

## Spot with Auto Scaling

```hcl
resource "aws_autoscaling_group" "mixed" {
  mixed_instances_policy {
    instances_distribution {
      on_demand_base_capacity                  = 2
      on_demand_percentage_above_base_capacity = 25
      spot_allocation_strategy                 = "capacity-optimized"
    }

    launch_template {
      launch_template_specification {
        launch_template_id = aws_launch_template.app.id
      }

      override {
        instance_type = "c5.large"
      }
      override {
        instance_type = "c5a.large"
      }
      override {
        instance_type = "c5n.large"
      }
    }
  }
}
```

## Summary

- **Up to 90% savings** for fault-tolerant workloads
- **Design for interruption** - save state, handle gracefully
- **Diversify** across instance types and AZs
- **Use with Auto Scaling** for automatic replacement
- **Capacity Optimized** strategy for fewer interruptions
- **Not suitable** for stateful or single-instance workloads
