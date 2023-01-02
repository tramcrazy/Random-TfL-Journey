import requests
import json
import datetime
import random
import time
import os
from flask import Flask, render_template, url_for

appKey = os.environ.get("TFL_API_KEY")
app = Flask(__name__)

def travelRoute(startpoint, endpoint):
    # try/except block for error handling
    try:
        output = ""
        startingLong = startpoint
        endLong = endpoint
        # find the icsCode for the start and end destination - used to build another GET request
        # GET request
        getRequest = requests.get(f"https://api.tfl.gov.uk/journey/journeyresults/{startingLong}/to/{endLong}&app_key={appKey}")
        #print(f"Status code from GET is {getRequest.status_code}")
        rawData = getRequest.json()
        # finding icsCode for starting point
        startPoint = rawData['fromLocationDisambiguation']['disambiguationOptions'][0]['parameterValue']
        # finding icsCode for end point
        endPoint = rawData['toLocationDisambiguation']['disambiguationOptions'][0]['parameterValue']
        # building new GET request
        rawJourneyData = requests.get(f"https://api.tfl.gov.uk/journey/journeyresults/{startPoint}/to/{endPoint}&app_key={appKey}")
        #print(f"Status code from GET is {rawJourneyData.status_code}")
        fullRouteResponse = rawJourneyData.json()
        journeyTime = fullRouteResponse['journeys'][0]['duration']
        output += f"The overall journey time will be {journeyTime} minutes<br>The journey steps are:<br><br>"
        selectedRoute = fullRouteResponse['journeys'][0]['legs']
        for detail in selectedRoute:
            output += "From " + detail['departurePoint']['commonName'] + "<br>"
            output += detail['instruction']['detailed'] + "<br>"
            output += "Arrive at " + detail['arrivalPoint']['commonName'] + "<br><br>"
    # handling KeyError specifically - found this in testing
    except KeyError as e:
        print("Error (KeyError)! Please try again!")
    # handling TypeError
    except TypeError as e:
        print("Error (TypeError)! Please try again!")
    return output
allstops = open("c:\\Users\\jonat\\OneDrive\\Documents\\allstops.txt", "r")
allstopsdata = allstops.read().splitlines()

@app.route("/")
@app.route("/index")
def homepage():
    return render_template("index.html")

@app.route("/journey")
def route_page():
    startstop = random.choice(allstopsdata)
    stopstop = random.choice(allstopsdata)
    return "Journey starts at " + startstop + "<br>" + "Journey ends at " + stopstop + "<br>" + travelRoute(startstop, stopstop)