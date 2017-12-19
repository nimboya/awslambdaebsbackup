import boto, os, mongoconn, time
from bson.json_util import dumps
from datetime import datetime

timestamp = int(time.time())
#accesskey = os.getenv('accesskey')
#secretkey = os.getenv('secrekey')

#ec = boto3.client('ec2', aws_access_key_id=accesskey, aws_secret_access_key=secretkey)
ec = boto3.client('ec2')
def lambda_handler(event='', context=''):
    conn = mongoconn.connect()
    instances = conn.find({},{"_id": 0})
    for instance in instances:
        startsnapshot(instance['instanceid'])
        print instance['instanceid']

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

lambda_handler()