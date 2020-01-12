from apscheduler.schedulers.background import BackgroundScheduler
from controllers.GIOSController import getMeasuringStations

#TODO: remember to change scheduler to query after every 24h instead of 5 seconds
#TODO: also remeber to change current endpoint(getMeasuringStations) to the target one
def runScheduler():
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(getMeasuringStations, 'interval', seconds=5)
    #uncommented - starts
    #sched.start()
