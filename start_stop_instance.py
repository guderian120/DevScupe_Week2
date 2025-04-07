from hands_on1 import get_cpu_usage
from python_with_aws_list_ec2 import *

cpu_usage = get_cpu_usage()

for cpu_utilization, instance_state, instance_id in cpu_usage:
    if cpu_utilization > 50 and instance_state == "stopped":
        print(f"Starting instance {instance_id} as CPU is {cpu_utilization}%")
        res = start_ec2_instance(instance_id)
        print(res)

    elif cpu_utilization < 10 and instance_state == "running":
        print(f"Stopping instance {instance_id} as CPU is {cpu_utilization}%")
        res = stop_ec2_instance(instance_id)
        print(res)

    else:
        print(f"No action needed. Instance is {instance_state}")
