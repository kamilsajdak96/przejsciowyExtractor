from flask import Flask
from helpers.RunScheduler import runScheduler
from controllers.GIOSController import *

app = Flask(__name__)
app.register_blueprint(gios_controller)

runScheduler()

if __name__ == '__main__':
    app.run()