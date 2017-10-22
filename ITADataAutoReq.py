### This file is for multiple ITA data requests read from a txt file
import urllib.request
import json,io
import ITADataRquest, ITARequestClass

# This is the default request body, change fields or add fields
# according to api 
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


# Specify the directory for response data obtained
responseDirName = "ITAResponseData/"
# Specify the batch data request file here
# the request file shoud be in the format of sampleRequests.txt
# For IATA airport code refer to
# http://www.nationsonline.org/oneworld/IATA_Codes/airport_code_list.htm
requestDirName = "RequestTexts/"
requestFileName = "sampleRequests.txt"
requestFullFileName = requestDirName + requestFileName
requestFile = open(requestFullFileName, 'r')
requests = requestFile.readlines()

# Count the sucessful request numbers
sucessCount = 0

try:
    # Make individual request for each request recorded in the file just opened
    for req in requests:
        req = req.strip().split(' ')
        
        # Using default name specified in ITADataRquest
        reqBodyObj.request.slices[0].origin = req[0]
        reqBodyObj.request.slices[0].destination = req[1]
        reqBodyObj.request.slices[0].date = req[2]
        # Turn changed RequestObj to its dictionary representation
        reqBody = reqBodyObj.dictify()
        # Make the name for the file name that store the request
        # and its response with format of "OriginToDestinationData.json"
        dateStr = req[2].replace("-", "")
        resReqFileName = req[0] + "To" + req[1] + dateStr + ".json"
        # Make the request to server and save the request and response
        # in the files in the name format above
        ITADataRquest.make_request(resReqFileName, reqBody)
        sucessCount += 1
except Exception as e:
    print("Finished only " + str(sucessCount) + " requests")
    raise e

# When finished sucessfully print on the python shell
print("Fininshed " + str(sucessCount) + " requests in total.")
print("Done!")