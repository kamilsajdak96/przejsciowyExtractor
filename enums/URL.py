import enum

class URL(enum.Enum):
    GIOS_API_URL = "http://api.gios.gov.pl/pjp-api/rest"
    API_MEASURING_STATIONS = GIOS_API_URL + "/station/findAll"
    API_MEASURING_POSITIONS = GIOS_API_URL + "/station/sensors/"
    API_MEASURING_DATA = GIOS_API_URL + "/data/getData/"
    API_AIR_INDEX = GIOS_API_URL + "/aqindex/getIndex/"