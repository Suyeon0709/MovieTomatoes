# MongoDB Access and CRUD test

from pymongo import MongoClient

# 1. MongoDB Connection

# local host == 127.0.0.1 == real IP
client = MongoClient('localhost', 27017) # (IP address, Post number)
db = client['local']                     # Allocating 'local' DB
collection = db.get_collection('test')   # Allocating 'review' Collection

deta = {'name': 'cherry', 'age': 8}
collection.insert_one(deta)


# MongoDB > detabase > collection > document
# 우리은행 > 우리은행 광주지점 > 예금 > 50,000 입금: 김수연

# CRUD => Crate, Read, Update, Delete


