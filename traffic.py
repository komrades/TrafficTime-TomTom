#!/usr/bin/python
##########################
# Author: Dushyant Singh #
##########################
import csv
import sys
import json
import requests
import urllib2
import time
from datetime import datetime
 
my_file = open("totaltime.csv", "wb")
csv_writer = csv.writer(my_file) #create csv named totaltime.csv
csv_writer.writerow(["Time to Destination (In Current Traffic) Minutes", "Total Miles" , "Current Location", "Destination" , "Current Date & Time", "Status Code"]) #create following rows
 
def main():
        try:
                response = requests.get("https://api.tomtom.com/routing/1/calculateRoute/{{DestinationLat, DestinationLon}}:{{OriginLat, OriginLon}}/json?maxAlternatives=0&routeType=fastest&traffic=true&travelMode=car&key={{API-Key}}}}") #API request to TomTom webservice
                print response
                json_response= json.loads(response.text) #get json response
                trip_time = json_response["routes"][0]["summary"]["travelTimeInSeconds"] #parse travelTimeInSeconds from json response
                trip_distance = json_response["routes"][0]["summary"]["lengthInMeters"] #parse lengthInMeters from json response
                convert_time = trip_time / 60 #travelTimeInSeconds to minutes conversion
                convert_distance = round(trip_distance / 1609.344) #lengthInMeters to miles conversion
                current_location = " " #Lat/Lon used in API request
                destination = " " #Lat/Lon used in API request
                current_time = str(datetime.now()) #get current date & time for later analysis
                print current_time
                csv_writer.writerow([convert_time, convert_distance, current_location, destination, current_time, response.status_code]) #write to csv
                my_file.flush()
        except:
                pass
while True:
   main()
   time.sleep(120) #execute script every 2 minutes
if __name__ == '__main__':
   main()
