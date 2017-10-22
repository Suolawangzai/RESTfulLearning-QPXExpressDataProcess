### This file created the class object for Flight infomation of response 
### from the search request
class TripsSearch:
    '''A general class for a search response result'''
    
    def __init__(self, dictionary):
        '''(Dictionary) -> NonType
        Create a new tris search object with nested dictionary input'''
        self.kind = dictionary['kind']
        keys = dictionary.keys()
        if 'trips' in keys:
            self.trips = TripOptions(dictionary['trips'])
        else:
            self.trips = None 

    def __str__(self):
        '''() -> str
        Return the string representation of this TripsSearch
        '''
        return TripsSearch.dictify(self).__str__()
      
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this TripsSearch'''
        dictionary= {}
        if self.kind is not None:
            dictionary['kind'] = self.kind         
        if self.trips is not None:
            dictionary['trips'] = TripOptions.dictify(self.trips)       
        return dictionary            

          
class TripOptions:
    '''A general class for all trip options information get from one search response result'''
    
    def __init__(self, dictionary):
        '''(Dictionary) -> NonType
        Create a new trips entry object with nested dictionary input'''
        self.kind = dictionary['kind']
        keys = dictionary.keys()
        if 'requestId' in keys:
            self.requestId = dictionary['requestId']
        else:
            self.requestId = None        
        if 'data' in keys:
            self.data = TripData(dictionary['data'])
        else:
            self.data = None
        if 'tripOption' in keys:
            self.tripOption = []
            for subdict in dictionary['tripOption']:
                self.tripOption.append(TripOption(subdict))
        else:
            self.tripOption = None

    def __str__(self):
        '''() -> str
        Return the string representation of this TripOptions
        '''
        return TripOptions.dictify(self).__str__()
      
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this TripOptions'''
        dictionary= {}
        if self.kind is not None:
            dictionary['kind'] = self.kind
        if self.requestId is not None:
            dictionary['requestId'] = self.requestId
        if self.data is not None:
            dictionary['data'] = TripData.dictify(self.data)       
        if self.tripOption is not None:
            dictionary['tripOption'] = []
            for obj in self.tripOption:
                dictionary['tripOption'].append(TripOption.dictify(obj))     
        return dictionary 


class TripData:
    '''A general class for trip data for all trip solutions'''
    
    def __init__(self, dictionary):
        '''(Dictionary) -> NonType
        Create a new data entry object with nested dictionary input'''
        self.kind = dictionary['kind']
        keys = dictionary.keys()
        if 'airport' in keys:
            self.airport = [] 
            for subdict in dictionary['airport']:
                self.airport.append(AirportData(subdict))
        else:
            self.airport = None
        if 'city' in keys:
            self.city = []
            for subdict_1 in dictionary['city']:
                self.city.append(CityData(subdict_1))
        else:
            self.city = None
        if 'aircraft' in keys:
            self.aircraft = []
            for subdict_2 in dictionary['aircraft']:
                self.aircraft.append(AircraftData(subdict_2))  
        else:
            self.aircraft = None
        if 'tax' in keys:
            self.tax = []
            for subdict_3 in dictionary['tax']:
                self.tax.append(TaxData(subdict_3))  
        else:
            self.tax = None
        if 'carrier' in keys:
            self.carrier = []
            for subdict_4 in dictionary['carrier']:
                self.carrier.append(CarrierData(subdict_4))  
        else:
            self.carrier = None 

    def __str__(self):
        '''() -> str
        Return the string representation of this TripData
        '''
        return TripData.dictify(self).__str__()
      
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this TripData'''
        dictionary= {}
        if self.kind is not None:
            dictionary['kind'] = self.kind
        if self.airport is not None:
            dictionary['airport'] = [] 
            for obj in self.airport:
                dictionary['airport'].append(AirportData.dictify(obj))
        if self.city is not None:
            dictionary['city'] = []
            for obj_1 in self.city:
                dictionary['city'].append(CityData.dictify(obj_1))
        if self.aircraft is not None:
            dictionary['aircraft'] = []
            for obj_2 in self.aircraft:
                dictionary['aircraft'].append(AircraftData.dictify(obj_2))          
        if self.tax is not None:
            dictionary['tax'] = []
            for obj_3 in self.tax:
                dictionary['tax'].append(TaxData.dictify(obj_3))
        if self.carrier is not None:
            dictionary['carrier'] = []
            for obj_4 in self.carrier:
                dictionary['carrier'].append(CarrierData.dictify(obj_4))        
        return dictionary 


class AirportData:
    '''A general class for airport information'''
    
    def __init__(self, dictionary):
        '''(Dictionary) -> NonType
        Create a new airport entry with airport information'''
        self.kind = dictionary['kind']
        keys = dictionary.keys()
        if 'code' in keys:
            self.code = dictionary['code']
        else:
            self.code = None
        if 'city' in keys:
            self.city = dictionary['city']
        else:
            self.city = None
        if 'name' in keys:
            self.name = dictionary['name']
        else:
            self.name = None

    def __str__(self):
        '''() -> str
        Return the string representation of this AirportData
        '''
        return AirportData.dictify(self).__str__()
      
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this AirportData'''
        dictionary= {}
        if self.kind is not None:
            dictionary['kind'] = self.kind
        if self.code is not None:
            dictionary['code'] = self.code
        if self.city is not None:
            dictionary['city'] = self.city
        if self.name is not None:
            dictionary['name'] = self.name     
        return dictionary 


class CityData:
    '''A general class for city information'''
    
    def __init__(self, dictionary):
        '''(Dictionary) -> NonType
        Create a new city entry with city information'''
        self.kind = dictionary['kind']
        keys = dictionary.keys()
        if 'code' in keys:
            self.code = dictionary['code']
        else:
            self.code = None
        if 'country' in keys:
            self.country = dictionary['country']
        else:
            self.country = None
        if 'name' in keys:
            self.name = dictionary['name']
        else:
            self.name = None

    def __str__(self):
        '''() -> str
        Return the string representation of this CityData
        '''
        return CityData.dictify(self).__str__()
      
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this CityData'''
        dictionary= {}
        if self.kind is not None:
            dictionary['kind'] = self.kind
        if self.code is not None:
            dictionary['code'] = self.code
        if self.country is not None:
            dictionary['country'] = self.country
        if self.name is not None:
            dictionary['name'] = self.name     
        return dictionary 


class AircraftData:
        '''A general class for aircraft information'''
        
        def __init__(self, dictionary):
            '''(Dictionary) -> NonType
            Create a new aircraft entry with aircraft information'''
            self.kind = dictionary['kind']
            keys = dictionary.keys()
            if 'code' in keys:
                self.code = dictionary['code']
            else:
                self.code = None
            if 'name' in keys:
                self.name = dictionary['name']
            else:
                self.name = None

        def __str__(self):
            '''() -> str
            Return the string representation of this AircraftData
            '''
            return AircraftData.dictify(self).__str__()
          
        def dictify(self):
            '''() -> dict
            Return the dictionary representation of this AircraftData'''
            dictionary= {}
            if self.kind is not None:
                dictionary['kind'] = self.kind
            if self.code is not None:
                dictionary['code'] = self.code
            if self.name is not None:
                dictionary['name'] = self.name     
            return dictionary 


class TaxData:
        '''A general class for tax information'''
        
        def __init__(self, dictionary):
            '''(Dictionary) -> NonType
            Create a new tax entry with tax information'''
            self.kind = dictionary['kind']
            keys = dictionary.keys()
            # note the we use Id instead of id to avoid preserved keyword
            if 'id' in keys:
                self.Id = dictionary['id']
            else:
                self.Id = None
            if 'name' in keys:
                self.name = dictionary['name']
            else:
                self.name = None

        def __str__(self):
            '''() -> str
            Return the string representation of this TaxData
            '''
            return TaxData.dictify(self).__str__()
          
        def dictify(self):
            '''() -> dict
            Return the dictionary representation of this TaxData'''
            dictionary= {}
            if self.kind is not None:
                dictionary['kind'] = self.kind
            if self.Id is not None:
                dictionary['id'] = self.Id
            if self.name is not None:
                dictionary['name'] = self.name     
            return dictionary 
                
                
class CarrierData:
        '''A general class for carrier information'''
        
        def __init__(self, dictionary):
            '''(Dictionary) -> NonType
            Create a new carrier entry with carrier information'''
            self.kind = dictionary['kind']
            keys = dictionary.keys()
            if 'code' in keys:
                self.code = dictionary['code']
            else:
                self.code = None
            if 'name' in keys:
                self.name = dictionary['name']
            else:
                self.name = None

        def __str__(self):
            '''() -> str
            Return the string representation of this CarrierData
            '''
            return CarrierData.dictify(self).__str__()
          
        def dictify(self):
            '''() -> dict
            Return the dictionary representation of this CarrierData'''
            dictionary= {}
            if self.kind is not None:
                dictionary['kind'] = self.kind
            if self.code is not None:
                dictionary['code'] = self.code
            if self.name is not None:
                dictionary['name'] = self.name     
            return dictionary 
                
                
class TripOption:
    '''A general class for carrier information'''
    
    def __init__(self, dictionary):
        '''(dict) -> NonType
        Create a new trip option object with input nested dictionary'''
        self.kind = dictionary['kind']
        keys = dictionary.keys()
        if 'saleTotal' in keys:
            self.saleTotal = dictionary['saleTotal']
        else:
            self.saleTotal = None
        # note that we use Id instead of id to avoid preserved keyword
        if 'id' in keys:
            self.Id = dictionary['id']
        else:
            self.Id = None
        # note that we use slices instead of slice to avoid preserved keyword
        if 'slice' in keys:
            self.slices = []
            for subdict in dictionary['slice']:
                self.slices.append(SliceInfo(subdict))
        else:
            self.slices = None
        if 'pricing' in keys:
            self.pricing = []
            for subdict_1 in dictionary['pricing']:
                self.pricing.append(PricingInfo(subdict_1))
        else:
            self.pricing = None
    
    def __str__(self):
        '''() -> str
        Return the string representation of this TripOption
        '''
        return TripOption.dictify(self).__str__()
      
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this TripOption'''
        dictionary= {}
        if self.kind is not None:
            dictionary['kind'] = self.kind
        if self.saleTotal is not None:
            dictionary['saleTotal'] = self.saleTotal
        if self.Id is not None:
            dictionary['id'] = self.Id
        if self.slices is not None:
            dictionary['slice'] = []
            for obj in self.slices:
                dictionary['slice'].append(SliceInfo.dictify(obj))
        if self.pricing is not None:
            dictionary['pricing'] = []
            for obj_1 in self.pricing:
                dictionary['pricing'].append(PricingInfo.dictify(obj_1))        
        return dictionary 


class SliceInfo:
    '''A general class for slices that make up this trip's itinerary.'''
    
    def __init__(self, dictionary):
        '''(dict) -> NonType
        Create a new slice object with input nested dictionary'''
        self.kind = dictionary['kind']
        keys = dictionary.keys()
        if 'duration' in keys:
            self.duration = dictionary['duration']
        else:
            self.duration = None
        if 'segment' in keys:
            self.segment = []
            for subdict in dictionary['segment']:
                self.segment.append(SegmentInfo(subdict))
        else:
            self.segment = None   

    def __str__(self):
        '''() -> str
        Return the string representation of this SliceInfo
        '''
        return SliceInfo.dictify(self).__str__()
      
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this SliceInfo'''
        dictionary= {}
        if self.kind is not None:
            dictionary['kind'] = self.kind 
        if self.duration is not None:
            dictionary['duration'] = self.duration
        if self.segment is not None:
            dictionary['segment'] = []
            for obj in self.segment:
                dictionary['segment'].append(SegmentInfo.dictify(obj))
        return dictionary 
           
            
class SegmentInfo:
    '''A general class for segment(s) constituting the slice.'''
    
    def __init__(self, dictionary):
        '''(dict) -> NonType
        Create a new segment object with input dictionary'''
        self.kind = dictionary['kind']
        keys = dictionary.keys()
        if 'duration' in keys:
            self.duration = dictionary['duration']
        else:
            self.duration = None
        if 'flight' in keys:
            self.flight = FlightInfo(dictionary['flight'])
        else:
            self.flight = None
        # note that we use Id instead of id to avoid preserved keyword
        if 'id' in keys:
            self.Id = dictionary['id']
        else:
            self.Id = None
        if 'cabin' in keys:
            self.cabin = dictionary['cabin']
        else:
            self.cabin = None
        if 'bookingCode' in keys:
            self.bookingCode = dictionary['bookingCode']
        else:
            self.bookingCode = None
        if 'bookingCodeCount' in keys:
            self.bookingCodeCount = dictionary['bookingCodeCount']
        else:
            self.bookingCodeCount = None 
        if 'marriedSegmentGroup' in keys:
            self.marriedSegmentGroup = dictionary['marriedSegmentGroup']
        else:
            self.marriedSegmentGroup = None 
        if 'subjectToGovernmentApproval' in keys:
            self.subjectToGovernmentApproval = dictionary['subjectToGovernmentApproval']
        else:
            self.subjectToGovernmentApproval = None
        if 'leg' in keys:
            self.leg = []
            for subdict in dictionary['leg']:
                self.leg.append(LegInfo(subdict))
        else:
            self.leg = None
        if 'connectionDuration' in keys:
            self.connectionDuration = dictionary['connectionDuration']
        else:
            self.connectionDuration = None

    def __str__(self):
        '''() -> str
        Return the string representation of this SegmentInfo
        '''
        return SegmentInfo.dictify(self).__str__()
      
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this SegmentInfo'''
        dictionary= {}
        if self.kind is not None:
            dictionary['kind'] = self.kind 
        if self.duration is not None:
            dictionary['duration'] = self.duration
        if self.flight is not None:
            dictionary['flight'] = FlightInfo.dictify(self.flight)
        if self.Id is not None:
            dictionary['id'] = self.Id
        if self.cabin is not None:
            dictionary['cabin'] = self.cabin
        if self.bookingCode is not None:
            dictionary['bookingCode'] = self.bookingCode
        if self.bookingCodeCount is not None:
            dictionary['bookingCodeCount'] = self.bookingCodeCount      
        if self.marriedSegmentGroup is not None:
            dictionary['marriedSegmentGroup'] = self.marriedSegmentGroup
        if self.subjectToGovernmentApproval is not None:
            dictionary['subjectToGovernmentApproval'] = self.subjectToGovernmentApproval
        if self.leg is not None:
            dictionary['leg'] = []
            for obj in self.leg:
                dictionary['leg'].append(LegInfo.dictify(obj))
        if self.connectionDuration is not None:
            dictionary['connectionDuration'] = self.connectionDuration        
        return dictionary 
            

class FlightInfo:
    ''' A general class for the flight in a segment'''
    
    def __init__(self, dictionary):
        '''(dict) -> NonType
        Create a new flight infromation object with input dictionary'''
        keys = dictionary.keys()
        if 'carrier' in keys:
            self.carrier = dictionary['carrier']
        else:
            self.carrier = None
        if 'number' in keys:
            self.number = dictionary['number']
        else:
            self.number = None    

    def __str__(self):
        '''() -> str
        Return the string representation of this FlightInfo
        '''
        return FlightInfo.dictify(self).__str__()
      
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this FlightInfo'''
        dictionary= {}
        if self.carrier is not None:
            dictionary['carrier'] = self.carrier
        if self.number is not None:
            dictionary['number'] = self.number
        return dictionary 

                     
class LegInfo:
    '''A general class for leg. A leg is the smallest unit of travel, in the case of a flight a takeoff immediately followed by a landing at two set points on a particular carrier with a particular flight number.'''
    
    def __init__(self, dictionary):
        '''(dict) -> NonType
        Create a new leg object with input dictionary'''
        self.kind = dictionary['kind']
        keys = dictionary.keys()
        # note the we use Id instead of id to avoid preserved keyword
        if 'id' in keys:
            self.Id = dictionary['id']
        else:
            self.Id = None
        if 'aircraft' in keys:
            self.aircraft = dictionary['aircraft']
        else:
            self.aircraft = None
        if 'arrivalTime' in keys:
            self.arrivalTime = dictionary['arrivalTime']
        else:
            self.arrivalTime = None
        if 'departureTime' in keys:
            self.departureTime = dictionary['departureTime']
        else:
            self.departureTime = None
        if 'origin' in keys:
            self.origin = dictionary['origin']
        else:
            self.origin = None
        if 'destination' in keys:
            self.destination = dictionary['destination']
        else:
            self.destination = None 
        if 'originTerminal' in keys:
            self.originTerminal = dictionary['originTerminal']
        else:
            self.originTerminal = None 
        if 'destinationTerminal' in keys:
            self.destinationTerminal = dictionary['destinationTerminal']
        else:
            self.destinationTerminal = None
        if 'duration' in keys:
            self.duration = dictionary['duration']
        else:
            self.duration = None
        if 'operatingDisclosure' in keys:
            self.operatingDisclosure = dictionary['operatingDisclosure']
        else:
            self.operatingDisclosure = None
        if 'onTimePerformance' in keys:
            self.onTimePerformance = dictionary['onTimePerformance']
        else:
            self.onTimePerformance = None
        if 'mileage' in keys:
            self.mileage = dictionary['mileage']
        else:
            self.mileage = None
        if 'meal' in keys:
            self.meal = dictionary['meal']
        else:
            self.meal = None
        if 'secure' in keys:
            self.secure = dictionary['secure']
        else:
            self.secure = None
        if 'connectionDuration' in keys:
            self.connectionDuration = dictionary['connectionDuration']
        else:
            self.connectionDuration = None
        if 'changePlane' in keys:
            self.changePlane = dictionary['changePlane']
        else:
            self.changePlane = None        

    def __str__(self):
        '''() -> str
        Return the string representation of this LegInfo
        '''
        return LegInfo.dictify(self).__str__()
      
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this LegInfo'''
        dictionary= {}
        if self.kind is not None:
            dictionary['kind'] = self.kind 
        if self.Id is not None:
            dictionary['id'] = self.Id
        if self.aircraft is not None:
            dictionary['aircraft'] = self.aircraft 
        if self.arrivalTime is not None:
            dictionary['arrivalTime'] = self.arrivalTime
        if self.departureTime is not None:
            dictionary['departureTime'] = self.departureTime
        if self.origin is not None:
            dictionary['origin'] = self.origin
        if self.destination is not None:
            dictionary['destination'] = self.destination       
        if self.originTerminal is not None:
            dictionary['originTerminal'] = self.originTerminal
        if self.destinationTerminal is not None:
            dictionary['destinationTerminal'] = self.destinationTerminal
        if self.duration is not None:
            dictionary['duration'] = self.duration 
        if self.operatingDisclosure is not None:
            dictionary['operatingDisclosure'] = self.operatingDisclosure
        if self.onTimePerformance is not None:
            dictionary['onTimePerformance'] = self.onTimePerformance
        if self.mileage is not None:
            dictionary['mileage'] = self.mileage
        if self.meal is not None:
            dictionary['meal'] = self.meal
        if self.secure is not None:
            dictionary['secure'] = self.secure
        if self.connectionDuration is not None:
            dictionary['connectionDuration'] = self.connectionDuration
        if self.changePlane is not None:
            dictionary['changePlane'] = self.changePlane         
        return dictionary  


class PricingInfo:
    '''A general class for pricing for each slice of trip opption.'''
    
    def __init__(self, dictionary):
        '''(dict) -> NonType
        Create a new pricing info object with input dictionary'''
        self.kind = dictionary['kind']
        keys = dictionary.keys()
        if 'fare' in keys:
            self.fare = []
            for subdict in dictionary['fare']:
                self.fare.append(Fareinfo(subdict))
        else:
            self.fare = None        
        if 'segmentPricing' in keys:
            self.segmentPricing = []
            for subdict_1 in dictionary['segmentPricing']:
                self.segmentPricing.append(SegmentPricing(subdict_1))
        else:
            self.segmentPricing = None
        if 'baseFareTotal' in keys:
            self.baseFareTotal = dictionary['baseFareTotal']
        else:
            self.baseFareTotal = None
        if 'saleFareTotal' in keys:
            self.saleFareTotal = dictionary['saleFareTotal']
        else:
            self.saleFareTotal = None 
        if 'saleTaxTotal' in keys:
            self.saleTaxTotal = dictionary['saleTaxTotal']
        else:
            self.saleTaxTotal = None
        if 'saleTotal' in keys:
            self.saleTotal = dictionary['saleTotal']
        else:
            self.saleTotal = None 
        if 'passengers' in keys:
            self.passengers = PassengerCounts(dictionary['passengers'])
        else:
            self.passengers = None
        if 'tax' in keys:
            self.tax = []
            for subdict_2 in dictionary['tax']:
                self.tax.append(TaxInfo(subdict_2))
        else:
            self.tax = None
        if 'fareCalculation' in keys:
            self.fareCalculation = dictionary['fareCalculation']
        else:
            self.fareCalculation = None  
        if 'latestTicketingTime' in keys:
            self.latestTicketingTime = dictionary['latestTicketingTime']
        else:
            self.latestTicketingTime = None
        if 'ptc' in keys:
            self.ptc = dictionary['ptc']
        else:
            self.ptc = None
        if 'refundable' in keys:
            self.refundable = dictionary['refundable']
        else:
            self.refundable = None        

    def __str__(self):
        '''() -> str
        Return the string representation of this PricingInfo
        '''
        return PricingInfo.dictify(self).__str__()
      
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this PricingInfo'''
        dictionary= {}
        if self.kind:
            dictionary['kind'] = self.kind 
        if self.fare:
            dictionary['fare'] = [] 
            for obj in self.fare:
                dictionary['fare'].append(Fareinfo.dictify(obj))
        if self.segmentPricing:
            dictionary['segmentPricing'] = [] 
            for obj_1 in self.segmentPricing:
                dictionary['segmentPricing'].append(SegmentPricing.dictify(obj_1))
        if self.baseFareTotal:
            dictionary['baseFareTotal'] = self.baseFareTotal
        if self.saleFareTotal:
            dictionary['saleFareTotal'] = self.saleFareTotal     
        if self.saleTaxTotal:
            dictionary['saleTaxTotal'] = self.saleTaxTotal       
        if self.saleTotal:
            dictionary['saleTotal'] = self.saleTotal
        if self.passengers:
            dictionary['passengers'] = PassengerCounts.dictify(self.passengers)
        if self.tax:
            dictionary['tax'] = [] 
            for obj_2 in self.tax:
                dictionary['tax'].append(TaxInfo.dictify(obj_2))
        if self.fareCalculation:
            dictionary['fareCalculation'] = self.fareCalculation  
        if self.latestTicketingTime:
            dictionary['latestTicketingTime'] = self.latestTicketingTime
        if self.ptc:
            dictionary['ptc'] = self.ptc
        if self.refundable:
            dictionary['refundable'] = self.refundable         
        return dictionary           
            
            
class Fareinfo: 
    '''A general class for fare used to price one or more segments'''
    
    def __init__(self, dictionary):
        '''(dict) -> NonType
        Create a new fare info object with input dictionary'''
        self.kind = dictionary['kind']
        keys = dictionary.keys()
        # note that we use Id instead of id to avoid preserved keyword
        if 'id' in keys:
            self.Id = dictionary['id']
        else:
            self.Id = None        
        if 'carrier' in keys:
            self.carrier = dictionary['carrier']
        else:
            self.carrier = None
        if 'origin' in keys:
            self.origin = dictionary['origin']
        else:
            self.origin = None
        if 'destination' in keys:
            self.destination = dictionary['destination']
        else:
            self.destination = None 
        if 'basisCode' in keys:
            self.basisCode = dictionary['basisCode']
        else:
            self.basisCode = None
        if 'private' in keys:
            self.private = dictionary['private']
        else:
            self.private = None        

    def __str__(self):
        '''() -> str
        Return the string representation of this Fareinfo
        '''
        return Fareinfo.dictify(self).__str__()
      
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this Fareinfo'''
        dictionary= {}
        if self.kind is not None:
            dictionary['kind'] = self.kind 
        # note that we use Id instead of id to avoid preserved keyword
        if self.Id is not None:
            dictionary['id'] = self.Id       
        if self.carrier is not None:
            dictionary['carrier'] = self.carrier       
        if self.origin is not None:
            dictionary['origin'] = self.origin
        if self.destination is not None:
            dictionary['destination'] = self.destination      
        if self.basisCode is not None:
            dictionary['basisCode'] = self.basisCode       
        if self.private is not None:
            dictionary['private'] = self.private
        return dictionary


class SegmentPricing:
    '''A general class for segment pricing, representing the price of this segment'''
    
    def __init__(self, dictionary):
        '''(dict) -> NonType
        Create a new segment pricing object with input dictionary'''
        self.kind = dictionary['kind']
        keys = dictionary.keys()
        if 'fareId' in keys:
            self.fareId = dictionary['fareId']
        else:
            self.fareId = None
        if 'segmentId' in keys:
            self.segmentId = dictionary['segmentId']
        else:
            self.segmentId = None
        if 'freeBaggageOption' in keys:
            self.freeBaggageOption = []
            for subdict in dictionary['freeBaggageOption']:
                self.freeBaggageOption.append(FreeBaggageAllowance(subdict)) 
        else:
            self.freeBaggageOption = None
    
    def __str__(self):
        '''() -> str
        Return the string representation of this SegmentPricing
        '''
        return SegmentPricing.dictify(self).__str__()
      
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this SegmentPricing'''
        dictionary= {}
        if self.kind:
            dictionary['kind'] = self.kind
        if self.fareId:
            dictionary['fareId'] = self.fareId
        if self.segmentId:
            dictionary['segmentId'] = self.segmentId
        if self.freeBaggageOption:
            dictionary['freeBaggageOption'] = []
            for obj in self.freeBaggageOption:
                dictionary['freeBaggageOption'].append(FreeBaggageAllowance.dictify(obj))
        return dictionary

        
class FreeBaggageAllowance:
    '''A general class for free baggage option, allowed on one segment of a trip'''
    
    def __init__(self, dictionary):
        '''(dict) -> NonType
        Create a new free baggage option object with input dictionary'''
        self.kind = dictionary['kind']
        keys = dictionary.keys()
        if 'bagDescriptor' in keys:
            self.bagDescriptor = []
            for subdict in  dictionary['bagDescriptor']:
                self.bagDescriptor.append(BagDescriptor(subdict))
        else:
            self.bagDescriptor = None
        if 'kilos' in keys:
            self.kilos = dictionary['kilos']
        else:
            self.kilos = None
        if 'kilosPerPiece' in keys:
            self.kilosPerPiece = dictionary['kilosPerPiece']
        else:
            self.kilosPerPiece = None
        if 'pieces' in keys:
            self.pieces = dictionary['pieces']
        else:
            self.pieces = None
        if 'pounds' in keys:
            self.pounds = dictionary['pounds']
        else:
            self.pounds = None

    def __str__(self):
        '''() -> str
        Return the string representation of this FreeBaggageAllowance
        '''
        return FreeBaggageAllowance.dictify(self).__str__()
      
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this FreeBaggageAllowance'''
        dictionary= {}
        if self.kind:
            dictionary['kind'] = self.kind
        if self.bagDescriptor:
            dictionary['bagDescriptor'] = []
            for obj in self.bagDescriptor:
                dictionary['bagDescriptor'].append(BagDescriptor.dictify(obj))
        if self.kilos is not None:
            dictionary['kilos'] = self.kilos
        if self.kilosPerPiece is not None:
            dictionary['kilosPerPiece'] = self.kilosPerPiece
        if self.pieces is not None:
            dictionary['pieces'] = self.pieces          
        if self.pounds is not None:
            dictionary['pounds'] = self.pounds
        return dictionary


class BagDescriptor:
    '''A general class for bag descriptor'''
    
    def __init__(self, dictionary):
        '''(dict) -> NonType
        Create a new bag descriptor object with input dictionary'''
        self.kind = dictionary['kind']
        keys = dictionary.keys()
        if 'commercialName' in keys:
            self.commercialName = dictionary['commercialName']
        else:
            self.commercialName = None
        if 'count' in keys:
            self.count = dictionary['count']
        else:
            self.count = None
        if 'description' in keys:
            self.description = dictionary['description']
        else:
            self.description = None
        if 'subcode' in keys:
            self.subcode = dictionary['subcode']
        else:
            self.subcode = None

    def __str__(self):
        '''() -> str
        Return the string representation of this BagDescriptor
        '''
        return BagDescriptor.dictify(self).__str__()
      
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this BagDescriptor'''
        dictionary= {}
        if self.kind is not None:
            dictionary['kind'] = self.kind
        if self.commercialName is not None:
            dictionary['commercialName'] = self.commercialName
        if self.count is not None:
            dictionary['count'] = self.count
        if self.description is not None:
            dictionary['description'] = self.description
        if self.subcode is not None:
            dictionary['subcode'] = self.subcode          
        return dictionary


class PassengerCounts:
    '''A general class for passenger counts, representing the number of passengers'''
    
    def __init__(self, dictionary):
        '''(dict) -> NonType
        Create a new passenger infromation object with input dictionary'''
        keys = dictionary.keys()
        if 'kind' in keys:
            self.kind = dictionary['kind']
        else:
            self.kind = None
        if 'adultCount' in keys:
            self.adultCount = dictionary['adultCount']
        else:
            self.adultCount = None
        if 'childCount' in keys:
            self.childCount = dictionary['childCount']
        else:
            self.childCount = None
        if 'infantInLapCount' in keys:
            self.infantInLapCount = dictionary['infantInLapCount']
        else:
            self.infantInLapCount = None
        if 'infantInSeatCount' in keys:
            self.infantInSeatCount = dictionary['infantInSeatCount']
        else:
            self.infantInSeatCount = None
        if 'seniorCount' in keys:
            self.seniorCount = dictionary['seniorCount']
        else:
            self.seniorCount = None
    
    def __str__(self):
        '''() -> str
        Return the string representation of this PassengerCounts
        '''
        return PassengerCounts.dictify(self).__str__()
      
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this PassengerCounts'''
        dictionary= {}
        if self.kind is not None:
            dictionary['kind'] = self.kind
        if self.adultCount is not None:
            dictionary['adultCount'] = self.adultCount
        if self.childCount is not None:
            dictionary['childCount'] = self.childCount
        if self.infantInLapCount is not None:
            dictionary['infantInLapCount'] = self.infantInLapCount
        if self.infantInSeatCount is not None:
            dictionary['infantInSeatCount'] = self.infantInSeatCount           
        if self.seniorCount is not None:
            dictionary['seniorCount'] = self.seniorCount
        return dictionary
    
    
class TaxInfo:
    '''A general class for tax information'''
    
    def __init__(self, dictionary):
        '''(dict) -> NonType
        Create a new TaxInfo object with input dictionary'''
        self.kind = dictionary['kind']
        keys = dictionary.keys()
        # note the we use Id instead of id to avoid preserved keyword
        if 'id' in keys:
            self.Id = dictionary['id']
        else:
            self.Id = None
        if 'chargeType' in keys:
            self.chargeType = dictionary['chargeType']
        else:
            self.chargeType = None
        if 'code' in keys:
            self.code = dictionary['code']
        else:
            self.code = None
        if 'country' in keys:
            self.country = dictionary['country']
        else:
            self.country = None
        if 'salePrice' in keys:
            self.salePrice = dictionary['salePrice']
        else:
            self.salePrice = None

    def __str__(self):
        '''() -> str
        Return the string representation of this TaxInfo
        '''
        return TaxInfo.dictify(self).__str__()
       
    def dictify(self):
        '''() -> dict
        Return the dictionary representation of this TaxInfo'''
        dictionary= {}
        if self.kind is not None:
            dictionary['kind'] = self.kind
        # note the we use Id instead of id to avoid preserved keyword
        if self.Id is not None:
            dictionary['id'] = self.Id
        if self.chargeType is not None:
            dictionary['chargeType'] = self.chargeType
        if self.code is not None:
            dictionary['code'] = self.code
        if self.country is not None:
            dictionary['country'] = self.country
        if self.salePrice is not None:
            dictionary['salePrice'] = self.salePrice   
        return dictionary