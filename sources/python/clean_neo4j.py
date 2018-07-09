from py2neo import Graph
import re


uri = "http://neo4j:7474"
password="admin"

graph = Graph(uri,password=password)
graph.data("match (n) detach delete (n)")
