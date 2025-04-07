# using cloudwatch metric to control instances
import datetime
import boto3
from python_with_aws_list_ec2 import *


def get_cpu_usage():
    cloudwatch = boto3.client("cloudwatch", region_name="eu-north-1")  # Change the region
    instance_ids = get_running_ec2()
    cpu_usage=[]


    # Get CPU utilization for the last 10 minutes
    # We are using cloudwatch get_metric_statistics
    for instance in instance_ids:
        response = cloudwatch.get_metric_statistics(
            Namespace="AWS/EC2",
            MetricName="CPUUtilization",
            Dimensions=[{"Name": "InstanceId", "Value": instance[0]}],
            StartTime=datetime.datetime.now(datetime.UTC) - datetime.timedelta(minutes=10),
            EndTime=datetime.datetime.now(datetime.UTC),
            Period=300,  # Every 5 minutes
            Statistics=["Average"],
            Unit="Percent",
        )
        data_points = response.get("Datapoints", [])
        cpu_usage.append((data_points[0]["Average"], instance[1], instance[0]))

    # Extract CPU usage

    # cpu_utilization = data_points[0]["Average"] if data_points else 0
    return cpu_usage
    


if __name__ == '__main__':
    get_cpu_usage()
    # print(f"CPU Utilization: {cpu_utilization}%")