import requests
from pymongo import MongoClient
import xmltodict
data_path = "../data/mongodb_xml/ai.stackexchange.com/Posts.xml"

with open(data_path,'r') as file :
    line = file.readline()
    print(line)
    line = file.readline()
    print(line)
    line = file.readline()
    print(line)
    dict_test = xmltodict.parse(line)
    print(dict_test)
    print("Titre : \n",dict_test['row']['@Title'])

