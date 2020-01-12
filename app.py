from flask import Flask, jsonify
from helpers.RunScheduler import runScheduler
from controllers.GIOSController import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"hehe": "Hello World!"})

@app.route('/measuring_stations', methods=['GET'])
def executeGetMeasuringStations():
    return getMeasuringStations()

@app.route('/measuring_positions/<stationId>', methods=['GET'])
def executeGetMeasuringPositions(stationId):
    return getMeasuringPositions(stationId)

@app.route('/measuring_data/<sensorId>', methods=['GET'])
def executeGetMeasuringData(sensorId):
    return getMeasuringData(sensorId)

@app.route('/air_index/<stationId>', methods=['GET'])
def executeGetAirIndex(stationId):
    return getAirIndex(stationId)

@app.route('/predicting_results', methods=['GET'])
def executePrediction():
    return prediction()

runScheduler()

if __name__ == '__main__':
    app.run()

