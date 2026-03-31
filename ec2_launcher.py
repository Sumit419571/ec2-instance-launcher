import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')

def launch_instance(name, instance_type):
    response = ec2.run_instances(
        ImageId='ami-0f58b397bc5c1f2e8',
        InstanceType=instance_type,
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': name}]
            }
        ]
    )
    
    instance = response['Instances'][0]
    instance_id = instance['InstanceId']
    
    print(f"✅ EC2 Instance Launched!")
    print(f"   Instance ID: {instance_id}")
    print(f"   State      : {instance['State']['Name']}")
    print(f"   Launch Time: {instance['LaunchTime']}")
    print(f"   AMI ID     : {instance['ImageId']}")
    print(f"   Instance Type: {instance_type}")
    print(f"   Status: Starting...")
    
    return instance_id

def terminate_instance(instance_id):
    ec2.terminate_instances(
        InstanceIds=[instance_id]
    )
    print(f"🗑️ Instance {instance_id} Terminated!")


name = input("Enter instance name: ")
instance_type = input("Enter instance type (t3.micro/t3.small): ")
instance_id = launch_instance(name, instance_type)

# Ask user before terminating
input("\n⏸️ Press Enter to terminate the instance...")

# Terminate instance
terminate_instance(instance_id)