import tweepy
from py2neo import Graph
import re
import csv

uri = "http://neo4j:7474"
password="admin"

graph = Graph(uri,password=password)
# http://py2neo.org/v4/database.html#the-graph
# graph.data("CREATE (:USER {name:'VERLEYEN',bdd:'twitter.bdd'})")

with open('Traffic_Violations.csv', "rt", encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:

        id = row[25]
        accident = row[9]
        alcool = row[17]
        arrest_type = row[24]
        
        list_lines = ""
        create_string = """
            MERGE (a:VIOLATION {id: \"%s\" ,ACCIDENT : \"%s\", ALCOOL : \"%s\", VIOLATION_TYPE : \"%s\"})"""%(
        id, accident, alcool, arrest_type)
        list_lines += (create_string+'\n ')

        try :
            graph.data(list_lines)
        except :
            print("this call didn't work:")
            print(list_lines)


    print("Similitude :")

    for row in spamreader:
        id = row[25]
        accident = row[9]
        alcool = row[17]
        arrest_type = row[24]
        
        list_lines = ""
        create_string = """
            MATCH (a:VIOLATION)
            WHERE a.ACCIDENT = \"%s\" AND ALCOOL = \"%s\" AND VIOLATION_TYPE = \"%s\"
            RETURN a.id
            """%(
        accident, alcool, arrest_type)
        list_lines += (create_string+'\n ')

        try :
            graph.data(list_lines)
        except :
            print("this call didn't work:")
            print(list_lines)