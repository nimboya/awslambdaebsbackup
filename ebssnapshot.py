import boto3, os, mongoconn, time
from bson.json_util import dumps
from datetime import datetime

timestamp = int(time.time())
accesskey = 'AKIAJ4EARHHTRFZO7VMQ' #os.getenv('accesskey')
secretkey = '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' #os.getenv('secrekey')

ec = boto3.client('ec2', aws_access_key_id=accesskey, aws_secret_access_key=secretkey)
#ec = boto3.client('ec2')
def lambda_handler(event, context):
    conn = mongoconn.connect()
    instances = conn.find({},{"_id": 0})
    for instance in instances:
        response = startsnapshot(instance['instanceid'])
        return instance['instanceid']
        #snapshotdata = json.loads(response)
        #conn = mongoconn.rootconn()
        #coll = conn.dbsnapshots
        #coll.insert_one(snapshotdata)

def startsnapshot(instanceid=""):
        reservations = ec.describe_instances(
            InstanceIds=['i-0fe082f2790b33096']
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

                res = ec.create_snapshot(
                    VolumeId=vol_id,
                    Description='SAP Database Snapshot on ' + str(timestamp)
                )
                print res 