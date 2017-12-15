import os, config, mongoconn, json
from datetime import datetime
from bson.json_util import dumps

def optionrouter(event, context, callback):
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
    print "created"

def getinstances():
    conn = mongoconn.connect()
    instances = conn.find({},{"_id": 0})
    
    #for instance in instances:
    #    print '{"instanceid":"%s", "instancename":"%s"}' %  (instance['instanceid'], instance['instancename'])
    js = dumps(instances)
    print js

def deleteinstance(instanceid):
    conn = mongoconn.connect()
    conn.delete_one({'instanceid':instanceid})
    print "deleteinstance"

getinstances()