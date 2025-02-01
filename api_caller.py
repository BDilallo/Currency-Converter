import requests
class API_Caller:

    def __init__(self, response):
        self.response = None

    def makeCall(key: str):
        call = "https://v6.exchangerate-api.com/v6/"+key+"/latest/"+"USD"
        response = requests.get(call)
        return response
        
    