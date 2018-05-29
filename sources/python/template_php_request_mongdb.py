import requests
from pymongo import MongoClient


for i in range(10):
    r = requests.get("http://ihm/users_search_preferences.php")
    print(r.json())


client = MongoClient('mongodb',27017)

db = client['mabdd']
collection = db['macollection']
collection.insert_one({'x':42,'y':42})
results = collection.find({},{'x':1})
print(results)
print([result for result in results])
