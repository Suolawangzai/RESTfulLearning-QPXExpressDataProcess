import ITAClasses
import ITARequestClass
class DataManipulationContainer:
    '''A general class to hold the request and response data together'''
    
    def __init__(self, responseData, requestData=None):
        '''(TripsSearch, RequestObj) -> NonType
        Create a DataManipulationContainer to hold the responseData and requestData'''
        self.responseData = responseData
        self.requestData = requestData
             
    def __str__(self):
        '''() -> str
        Return the string representation of this DataManipulationContainer
        '''
        return DataManipulationContainer.dictify(self).__str__()
      
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this DataManipulationContainer'''
        dictionary= {}
        if self.responseData is not None:
            dictionary['responseData'] = ITAClasses.TripsSearch.dictify(self.responseData)
        if self.requestData is not None:
            dictionary['requestData'] = ITARequestClass.RequestObj.dictify(self.requestData)        
        return dictionary    