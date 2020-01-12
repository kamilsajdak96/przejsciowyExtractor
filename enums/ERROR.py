import enum
import json

class ERROR(enum.Enum):
   GENERAL_ERROR = json.dumps({'error': 'Upss... something went wrong'})
   NO_SUCH_STATION_ID = json.dumps({'error': 'There is no such station with given id'})
   NO_SUCH_SENSOR_ID = json.dumps({'error': 'There is no such sensor with given id'})


