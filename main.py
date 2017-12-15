import os, config, mongoconn, json
from datetime import datetime
from bson.json_util import dumps

def optionrouter(event, context):
    if event['action'] == 'create':
        createinstance(event['instancename'], event['instanceid'], event['description'])
    elif event['action'] == 'delete':
        deleteinstance(event['instanceid'])
    else:
        return 'No Action Set'
    
def createinstance(instancename='', instanceid='', description=''):
    instancename = "staging mobilezone"
    instanceid = "i-00f0937f1f01b3dac"
    description = "staging mobilezone Server"
    created = datetime.now().replace(microsecond=0).isoformat()
    instancedata = {'instancename':instancename,'instanceid':instanceid,'description':description,'created':created}
    conn = mongoconn.connect()
    result = conn.insert_one(instancedata)
    context.succeed("created")

def getinstances():
    conn = mongoconn.connect()
    instances = conn.find({},{"_id": 0})
    js = dumps(instances)
    return js

def deleteinstance(instanceid):
    conn = mongoconn.connect()
    conn.delete_one({'instanceid':instanceid})
    return "deleteinstance"