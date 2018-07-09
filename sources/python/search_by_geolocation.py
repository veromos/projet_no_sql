import sys
import requests
from pymongo import MongoClient

client = MongoClient("mongodb", 27017)
db = client['mydbb']
TV = db['Traffic_Violations']

if len(sys.argv) == 4:
    try:
        print("{ Latitude: { $gt: "+str(float(sys.argv[1]) - float(sys.argv[3]) * 0.01)+", $lt: "+str(float(sys.argv[1]) + float(sys.argv[3]) * 0.01) +"}, Longitude : { $gt: "+ str(float(sys.argv[2]) - float(sys.argv[3]) * 0.01)+", $lt: "+str(float(sys.argv[2]) + float(sys.argv[3]) * 0.01)+" })");
        for violation in TV.find({ "Latitude": { "$gt": float(sys.argv[1]) - float(sys.argv[3]) * 0.01, "$lt": float(sys.argv[1]) + float(sys.argv[3]) * 0.01 }, "Longitude" : { "$gt": float(sys.argv[2]) - float(sys.argv[3]) * 0.01, "$lt": float(sys.argv[2]) + float(sys.argv[3]) * 0.01 }}):
            print("------------- Date et heure: " + violation['Date Of Stop'] + ' - ' + violation['Time Of Stop'] + ' -------------')
            print("Infraction: " + violation['Description'])
            print("Accident: " + violation['Accident'])
            print("Genre: " + violation['Gender'])
            print("Race: " + violation['Race'])
            print("Coordonnees: " + violation['Geolocation'])
    except ValueError:
        print("Les parametres de sont pas des nombres flotants.")
else:
    print("Nombre de parametre invalide.")
