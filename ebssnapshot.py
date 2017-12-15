import boto3
import os
import time

timestamp = int(time.time())
accesskey = os.environ['accesskey']
secretkey = os.environ['secrekey']

ec = boto3.client('ec2', aws_access_key_id=accesskey, aws_secret_access_key=secretkey)

def lambda_handler(event, context):
    print "helloworld"

def startsnapshot(instanceid):
        reservations = ec.describe_instances(
            InstanceIds=[instanceid]
        ).get(
            'Reservations', []
        )

        instances = sum(
            [
                [i for i in r['Instances']]
                for r in reservations
            ], [])


        for instance in instances:
            for dev in instance['BlockDeviceMappings']:
                if dev.get('Ebs', None) is None:
                    continue
                vol_id = dev['Ebs']['VolumeId']
                print "Found EBS volume %s on instance %s" % (
                    vol_id, instance['InstanceId'])

                ec.create_snapshot(
                    VolumeId=vol_id,
                    Description='Mobilezone Database Snapshot on ' + str(timestamp)
                )

