Set-ups:
    1. In order to use QPX Express api, you need to have an API-KEY. Go to https://developers.google.com/qpx-express/v1/prereqs, check the the steps to get an API key. After getting the API key, copy it to the variable APIKEY int ITADataRquest.py
    
    2. Specify the directory that you want to store request response file in. Change the variable responseDirName in ITADataRquest.py. Specify the directory that you want to store request body file in. Change the variable requestDirName in ITADataRquest.py.
    
    3. Specify multiple requests in the text file of the given format (sampleRequest.txt). Change the variables requestDirName and requestFileName  in ITADataAutoReq.py to this directory and file name of this requests text file.


Class Scheme:
    The class schemes in ITAClasses and ITADataRquest are made corresponding to data's json structure.
    
    Classes in ITAClasses are based on the response json data structure.
    Classes in ITARequestClass are based on the request json data structure.
    
    For details , refer to https://developers.google.com/qpx-express/v1/trips/search.