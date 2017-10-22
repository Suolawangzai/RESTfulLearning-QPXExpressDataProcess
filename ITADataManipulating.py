### This file is for simple data manipulation of ITA data obtain by request script. Assume that all responses files are in the same directory and all requests files are also in the same directory
import json,io, os
import ITAClasses, ITARequestClass, DataManipulationClass

# Read data from the directories store the data
responseDataDirName = "ITAResponseData/"
requestDataDirName = "ITARequestData/"
# The Array contain data objects
data = []

# Get the list of files in the directory store repsonse json files
responseDataFilelst = os.listdir(responseDataDirName)

# Record how many files has been successfully extracted
sucessCount = 0
# Read each json file from the response json file and convert into a object
for filename in responseDataFilelst:
    # check if it is a json file
    if filename[-4:] == 'json':
        with open(responseDataDirName + filename) as response_data_file:
            responseData = json.load(response_data_file)
            # Turn the dictionary format data into object
            responseDataObj = ITAClasses.TripsSearch(responseData)
            
        # Get corresponding request json file name
        corReqFileName = filename[:-5] + "Request" + ".json"
        with open(requestDataDirName + corReqFileName) as request_data_file:
            requestData = json.load(request_data_file)         
            # Turn the dictionary format data into object
            requestDataObj = ITARequestClass.RequestObj(requestData)
            
        # Make object contain both the response and request object
        # Store the object into data array
        dataObj = DataManipulationClass.DataManipulationContainer(responseDataObj, requestDataObj)
        data.append(dataObj)
        sucessCount += 1

print("Finish extract data!")
print(str(sucessCount) + "request&responses have been extracted!")
        