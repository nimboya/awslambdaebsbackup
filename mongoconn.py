import config
from pymongo import MongoClient

def connect():
    if config.environment == "production":
        client = MongoClient('mongodb://%s:%s@%s:%s' % (config.mongousername, config.mongopassword, config.mongohost, config.mongoport))
        db = client['andromeda']
        instances = db.instances
        return instances
    else:
        client = MongoClient('localhost', 27017)
        db = client['andromeda']
        instances = db.instances
        return instances