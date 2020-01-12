import requests
from enums.ERROR import ERROR

def constructUrl(url, error = ERROR.GENERAL_ERROR.value, firstParam = ""):
    try:
        request = requests.get(url=url + str(firstParam)).json()
        if type(request) is list:
            request = requests.get(url=url + str(firstParam)).json()[0]
    except:
        return error
    return request