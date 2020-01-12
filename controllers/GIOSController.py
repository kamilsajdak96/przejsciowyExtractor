from enums.ERROR import ERROR
from enums.URL import *
from services.PredictingService import prediction
from services.GIOSService import constructUrl

def getMeasuringStations():
    return constructUrl(URL.API_MEASURING_STATIONS.value)

def getMeasuringPositions(stationId):
    return constructUrl(URL.API_MEASURING_POSITIONS.value, ERROR.NO_SUCH_STATION_ID.value, stationId)

def getMeasuringData(sensorId):
    return constructUrl(URL.API_MEASURING_DATA.value, ERROR.NO_SUCH_SENSOR_ID.value, sensorId)

def getAirIndex(stationId):
    return constructUrl(URL.API_AIR_INDEX.value, ERROR.NO_SUCH_STATION_ID.value, stationId)

def mlResults():
    return prediction()
