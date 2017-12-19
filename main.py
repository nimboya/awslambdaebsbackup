import os, config, mongoconn, json
from datetime import datetime
from bson.json_util import dumps

def optionrouter(event, context):
    if event['action'] == 'create':
        createinstance(event['instancename'], event['instanceid'], event['description'])
        return {"status_code":200, "status":"backup created"}
    elif event['action'] == 'view':
        getinstances()
    elif event['action'] == 'delete':
        deleteinstance(event['instanceid'])
        return {"status_code":200, "status":"backup deleted"}
    else:
        return 'No Action Set'
    
def optionrouter(event, context):
    if event['action'] == 'create':
        createinstance(event['instancename'], event['instanceid'], event['description'])
        return {"status_code":200, "status":"backup created"}
    elif event['action'] == 'delete':
        deleteinstance(event['instanceid'])
        return {"status_code":200, "status":"backup deleted"}
    elif event['action'] == 'view':
        return getinstances()
    else:
        return 'No Action Set'
    
    
def createinstance(instancename="", instanceid="", description=""):
    created = datetime.now().replace(microsecond=0).isoformat()
    instancedata = {'instancename':instancename,'instanceid':instanceid,'description':description,'created':created}
    conn = mongoconn.connect()
    result = conn.insert_one(instancedata)
    return "created"

def getinstances():
    conn = mongoconn.connect()
    instances = conn.find({},{"_id": 0})
    js = dumps(instances)
    allinstances = {"status_code":200, "status":"backup created", "data": js}
    data = json.loads(allinstances)
    print data

def deleteinstance(instanceid):
    conn = mongoconn.connect()
    conn.delete_one({'instanceid':instanceid})
    return "deleteinstance"

print getinstances()