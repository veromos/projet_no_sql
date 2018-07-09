import tweepy
from py2neo import Graph
import re
import csv

uri = "http://neo4j:7474" 
password="admin"

graph = Graph(uri,password=password)
# http://py2neo.org/v4/database.html#the-graph
# graph.data("CREATE (:USER {name:'VERLEYEN',bdd:'twitter.bdd'})")
i = 0
limit = 200

def count_violations_by_city(city):
    count = graph.data("""MATCH (n:DRIVER_CITY {value: "%s"})-[:DRIVER_FROM]-()
                RETURN COUNT(*)"""%(city))
    print(count)

with open('/srv/python/Traffic_Violations.csv', "rt", encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    
    for row in spamreader:
        if i > limit:
            break
        i = i+1
        charge = row[25]
        car_brand = row[21]
        car_color = row[23]
        arrest_type = row[24]
        driver_city = row[30]
        geolocation = row[34]

        list_lines = ""
        create_string = """
            MERGE (a:VIOLATION {id: %s, charge: "%s"})
            MERGE (b:CAR_BRAND {value: "%s"})
            MERGE (c:CAR_COLOR {value: "%s"})
            MERGE (d:VIOLATION_TYPE {value: "%s"})
            MERGE (a)-[:DRIVER_FROM]-(e:DRIVER_CITY {value: "%s"})
            MERGE (f:GEOLOCATION {value: "%s"})
            """%(
        i, charge, car_brand, car_color, arrest_type, driver_city, geolocation)
        list_lines += (create_string+'\n ')
        try :
            print(i)
            graph.data(list_lines)
        except :
            print("this call didn't work:")
            print(list_lines)

count_violations_by_city("SILVER SPRING")