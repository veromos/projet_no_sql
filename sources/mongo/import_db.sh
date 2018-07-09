#!/bin/sh
mongoimport -d mydbb -c Traffic_Violations --type csv --file /home/mongo/Traffic_Violations.csv --headerline