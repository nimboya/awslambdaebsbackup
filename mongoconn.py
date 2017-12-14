import os, config
from pymongo import MongoClient
from datetime import datetime

def connect():
    if config.environment == "production":
        client = MongoClient('mongodb://%s:%s@%s:%s/terragonbackup' % (config.mongousername, config.mongopassword, config.mongohost, config.mongoport))
        db = client['terragonbackup']
        instances = db.instances
        return instances
    else:
        client = MongoClient('localhost', 27017)
        db = client['terragonbackup']
        instances = db.instances
        return instances