from flask import Blueprint

from enums.ERROR import ERROR
from enums.URL import *
from services.GIOSService import constructUrl
from services.PredictingService import prediction

gios_controller = Blueprint('gios_controller', __name__)


@gios_controller.route('/measuring_stations', methods=['GET'])
def getMeasuringStations():
    return constructUrl(URL.API_MEASURING_STATIONS.value)


@gios_controller.route('/measuring_positions/<stationId>', methods=['GET'])
def getMeasuringPositions(stationId):
    return constructUrl(URL.API_MEASURING_POSITIONS.value, ERROR.NO_SUCH_STATION_ID.value, stationId)


@gios_controller.route('/measuring_data/<sensorId>', methods=['GET'])
def getMeasuringData(sensorId):
    return constructUrl(URL.API_MEASURING_DATA.value, ERROR.NO_SUCH_SENSOR_ID.value, sensorId)


@gios_controller.route('/air_index/<stationId>', methods=['GET'])
def getAirIndex(stationId):
    return constructUrl(URL.API_AIR_INDEX.value, ERROR.NO_SUCH_STATION_ID.value, stationId)


@gios_controller.route('/predicting_results', methods=['GET'])
def mlResults():
    return prediction()
