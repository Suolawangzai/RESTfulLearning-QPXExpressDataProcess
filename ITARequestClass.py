### This file created the class object for Flight infomation of response 
### from the search request

import ITAClasses

class RequestObj:
    '''A general class for a search formatted json request'''
    
    def __init__(self, dictionary):
        '''(dict) -> NonType
        Create a new formatted search request object with nested dictionary input'''
        keys = dictionary.keys()
        if 'request' in keys:
            self.request = RequestBodyObj(dictionary['request'])
        else:
            self.request = None
        
    def __str__(self):
        '''() -> str
        Return the string representation of this RequestObj
        '''
        return RequestObj.dictify(self).__str__()
      
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this RequestObj'''
        dictionary= {}
        if self.request is not None:
            dictionary['request'] = RequestBodyObj.dictify(self.request)
        return dictionary
    
    
class RequestBodyObj:
    '''A general class for a search formatted json request body'''
    
    def __init__(self, dictionary):
        '''(dict) -> NonType
        Create a new request body object with nested dictionary input'''
        keys = dictionary.keys()
        if 'passengers' in keys:
            self.passengers = ITAClasses.PassengerCounts(dictionary['passengers'])
        else:
            self.passengers = None
        # note that we use slices instead of slice to avoid preserved keyword
        if 'slice' in keys:
            self.slices = []
            for subdict in dictionary['slice']:
                self.slices.append(SliceInput(subdict))
        else:
            self.slices = None
        if 'maxPrice' in keys:
            self.maxPrice = dictionary['maxPrice']
        else:
            self.maxPrice = None
        if 'saleCountry' in keys:
            self.saleCountry = dictionary['saleCountry']
        else:
            self.saleCountry = None
        if 'ticketingCountry' in keys:
            self.ticketingCountry = dictionary['ticketingCountry']
        else:
            self.ticketingCountry = None
        if 'refundable' in keys:
            self.refundable = dictionary['refundable']
        else:
            self.refundable = None           
        if 'solutions' in keys:
            self.solutions = dictionary['solutions']
        else:
            self.solutions = None
        
    def __str__(self):
        '''() -> str
        Return the string representation of this RequestBodyObj
        '''
        return RequestBodyObj.dictify(self).__str__()
      
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this RequestBodyObj'''
        dictionary= {}
        if self.passengers is not None:
            dictionary['passengers'] = ITAClasses.PassengerCounts.dictify(self.passengers)
        if self.slices is not None:
            dictionary['slice'] = []
            for obj in self.slices:
                dictionary['slice'].append(SliceInput.dictify(obj))
        if self.maxPrice is not None:
            dictionary['maxPrice'] = self.maxPrice
        if self.saleCountry is not None:
            dictionary['saleCountry'] = self.saleCountry
        if self.ticketingCountry is not None:
            dictionary['ticketingCountry'] = self.ticketingCountry           
        if self.refundable is not None:
            dictionary['refundable'] = self.refundable
        if self.solutions is not None:
            dictionary['solutions'] = self.solutions       
        return dictionary            
            
class SliceInput:
    '''A general class for slice entry in the search formatted json request'''
    
    def __init__(self, dictionary):
        '''(dict) -> NonType
        Create a new slice input object with nested dictionary input'''  
        keys = dictionary.keys()
        if 'kind' in keys:
            self.kind = dictionary['kind']
        else:
            self.kind = None        
        if 'origin' in keys:
            self.origin = dictionary['origin']
        else:
            self.origin = None
        if 'destination' in keys:
            self.destination = dictionary['destination']
        else:
            self.destination = None
        if 'date' in keys:
            self.date = dictionary['date']
        else:
            self.date = None
        if 'maxStops' in keys:
            self.maxStops = dictionary['maxStops']
        else:
            self.maxStops = None
        if 'maxConnectionDuration' in keys:
            self.maxConnectionDuration = dictionary['maxConnectionDuration']
        else:
            self.maxConnectionDuration = None
        if 'preferredCabin' in keys:
            self.preferredCabin = dictionary['preferredCabin']
        else:
            self.preferredCabin = None           
        if 'permittedDepartureTime' in keys:
            self.permittedDepartureTime = TimeOfDayRange(dictionary['permittedDepartureTime'])
        else:
            self.permittedDepartureTime = None
        if 'permittedCarrier' in keys:
            self.permittedCarrier = dictionary['permittedCarrier']
        else:
            self.permittedCarrier = None             
        if 'alliance' in keys:
            self.alliance = dictionary['alliance']
        else:
            self.alliance = None
        if 'prohibitedCarrier' in keys:
            self.prohibitedCarrier = dictionary['prohibitedCarrier']
        else:
            self.prohibitedCarrier = None  
            
    def __str__(self):
        '''() -> str
        Return the string representation of this SliceInput
        '''
        return SliceInput.dictify(self).__str__()
      
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this SliceInput'''
        dictionary= {}
        if self.kind is not None:
            dictionary['kind'] = self.kind
        if self.origin is not None:
            dictionary['origin'] = self.origin
        if self.destination is not None:
            dictionary['destination'] = self.destination
        if self.date is not None:
            dictionary['date'] = self.date
        if self.maxStops is not None:
            dictionary['maxStops'] = self.maxStops           
        if self.maxConnectionDuration is not None:
            dictionary['maxConnectionDuration'] = self.maxConnectionDuration
        if self.preferredCabin is not None:
            dictionary['preferredCabin'] = self.preferredCabin
        if self.permittedDepartureTime is not None:
            dictionary['permittedDepartureTime'] = TimeOfDayRange.dictify(self.permittedDepartureTime)
        if self.permittedCarrier is not None:
            dictionary['permittedCarrier'] = self.permittedCarrier
        if self.alliance is not None:
            dictionary['alliance'] = self.alliance
        if self.prohibitedCarrier is not None:
            dictionary['prohibitedCarrier'] = self.prohibitedCarrier         
        return dictionary
    
            
class TimeOfDayRange:
    '''A general class for permitted departure time entry in the request object '''
    
    def __init__(self, dictionary):
        '''(dict) -> NonType
        Create a new  TimeOfDayRange object with nested dictionary input''' 
        
        self.kind = dictionary['kind']
        keys = dictionary.keys()
        if 'earliestTime' in keys:
            self.earliestTime = dictionary['earliestTime']
        else:
            self.earliestTime = None
        if 'latestTime' in keys:
            self.latestTime = dictionary['latestTime']
        else:
            self.latestTime = None

    def __str__(self):
        '''() -> str
        Return the string representation of this TimeOfDayRange
        '''
        return TimeOfDayRange.dictify(self).__str__()
      
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this TimeOfDayRange'''
        dictionary= {}
        if self.kind is not None:
            dictionary['kind'] = self.kind
        if self.earliestTime is not None:
            dictionary['earliestTime'] = self.earliestTime
        if self.latestTime is not None:
            dictionary['latestTime'] = self.clatestTime
        return dictionary