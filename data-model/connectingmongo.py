# connecting-mongodb with python
# connectingmongo.py

import json

from pymongo import MongoClient

url = "mongodb://127.0.0.1:27017"
db = MongoClient(url)

databases = db.list_database_names()

def lsdb():
	for item in db.list_database_names():
		print(item)





