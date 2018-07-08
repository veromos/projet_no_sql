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
        car_brand = row[21]
        car_color = row[23]
        arrest_type = row[24]
        driver_city = row[30]
        geolocation = row[34]
        
        list_lines = ""
        create_string = """
            MERGE (a:VIOLATION {id: \"%s\"})
            MERGE (a)-[:CAR_BRAND]-(b:CAR_BRAND {value: \"%s\"})
            MERGE (a)-[:CAR_COLOR]-(c:CAR_COLOR {value: \"%s\"})
            MERGE (a)-[:TYPE]-(d:VIOLATION_TYPE {value: \"%s\"})
            MERGE (a)-[:FROM]-(e:DRIVER_CITY {value: \"%s\"})
            MERGE (a)-[:AT]-(d:GEOLOCATION {value: \"%s\"})"""%(
        id, car_brand, car_color, arrest_type, driver_city, geolocation)
        list_lines += (create_string+'\n ')
        try :
            graph.data(list_lines)
        except :
            print("this call didn't work:")
            print(list_lines)