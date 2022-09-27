import os
from pymongo import MongoClient

os.environ["MONGODB_URI"] = "mongodb://root:labcepatsaji777@192.168.241.10:27017" # :)
client = MongoClient(os.environ['MONGODB_URI'])
db = client['attempts']
