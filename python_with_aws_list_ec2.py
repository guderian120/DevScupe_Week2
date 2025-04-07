import boto3

ec2 = boto3.client("ec2", region_name="eu-north-1")

def get_running_ec2():
# Create an EC2 client
    

    # Get all running instances
    response = ec2.describe_instances(Filters=[{"Name": "instance-state-name", "Values": ["running"]}])

    instance_ids = []
    # Print instance IDs
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_ids.append((instance['InstanceId'], instance['State']['Name']))
        
            # print(f"stopping instance {instance['InstanceId']}")
            # start_ec2_instance(instance['InstanceId'], ec2)
    return instance_ids


def stop_ec2_instance(instance_id, ec2=ec2):
    instance_id = instance_id # Replace with your actual instance ID

    response = ec2.stop_instances(InstanceIds=[instance_id])

    return f" instance {instance_id} Stopped... Status: {response}"

def start_ec2_instance(instance_id, ec2=ec2):
    instance_id = instance_id # Replace with your actual instance ID

    response = ec2.start_instances(InstanceIds=[instance_id])

    return f"Starting instance {instance_id}... Status: {response}"

def terminate_ec2(instance_id, ec2=ec2):
    response = ec2.terminate_instances(InstanceIds=[instance_id])

    return f"Terminating instance {instance_id}... Status: {response}"


if __name__ == '__main__':
    print(get_running_ec2())