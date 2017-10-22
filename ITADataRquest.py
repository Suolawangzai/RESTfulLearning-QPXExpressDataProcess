### This file is for sigle ITA data request and save the result into the file
### specified by user

### The functions in this module does not handl error from request or 
### file operations
import urllib.request
import json,io
import ITARequestClass

# Specify the Api key here
APIKEY = ""

# The request url to server when making http request
url =  "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + APIKEY

#----------------- Variables for sigle request -------------------------------
# This is the defualt request dictionary when run this script for single query
# Change the the field to make a query
reqBody = {
  "request": {
    "passengers": {
      "adultCount": 1,
      "childCount": 0,
      "infantInLapCount": 0,
      "infantInSeatCount": 0,
      "seniorCount": 0      
    },
    "slice": [
      {
        "kind": "qpxexpress#sliceInput",
        "origin": "BOS",
        "destination": "LAX",
        "date": "2017-11-22",
        "maxStops": 1,
        "maxConnectionDuration":360,
        "preferredCabin": 'COACH',   
      }
    ],
    "solutions": 20
  }
}

# Make a default  request object out of reqBody for manipulation
reqBodyObj = ITARequestClass.RequestObj(reqBody)

# This is a default format of the name for storing result 
# i.e OriginToDestination.json
# Change the field can make the result to store in a different location
flightResultFileName = reqBody["request"]["slice"][0]["origin"] + "To" + reqBody["request"]["slice"][0]["destination"] + ".json"
#-----------------------------------------------------------------------------

# Specify the directories to store request and its responses
responseDirName = "ITAResponseData/"
requestDirName = "ITARequestData/"

def make_request(resultFileName, reqBody):
    '''(str, dict) -> NoneType
    This function makes a single request to ITA database with specifed request body, and save the response infomation into the a file specified by resultFileName upon success.
    NOTE: the resultFileName must ended with ".json" extension'''
    # Make the http request with the url defined above
    req = urllib.request.Request(url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    reqBdyJson = json.dumps(reqBody)
    jsonDataBytes = reqBdyJson.encode('utf-8')
    # Send the http request for json data and save it to the file specified below
    response = urllib.request.urlopen(req, jsonDataBytes)
    flightinfo = response.read()
    file = open(responseDirName + resultFileName, 'wb')
    file.write(flightinfo)
    file.close()
    # Save the request json file into a json file with string 'Request'
    # appended to the resultFileName
    reqJsonFileName = resultFileName[:-5] + "Request" + ".json"
    _save_request(requestDirName + reqJsonFileName, reqBody)


def _save_request(reqJsonFileName, reqBody):
    '''(str, dict) -> NoneType
    This is a private function that save the request body (nested dictionary) specified into a json file (i.e serialize the structured data)'''
    with open(reqJsonFileName, "w") as f:
        json.dump(reqBody, f)




if __name__ == '__main__':
    make_request(flightResultFileName, reqBody)


'''with open("reqTest.json","w") as f:
        json.dump(reqBodyObj,f) '''
