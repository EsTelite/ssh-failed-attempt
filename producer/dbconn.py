import os
from pymongo import MongoClient

os.environ["MONGODB_URI"] = "mongodb://root:labcepatsaji777@localhost:27017" # TODO: Need to utilize env var or secret engine for real
client = MongoClient(os.environ['MONGODB_URI'])
db = client['attempts']
