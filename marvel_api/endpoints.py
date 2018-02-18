import requests
import marvel_api.response
import marvel_api.entities
import marvel_api.authorization


class Util:
    BASE_URL = "https://gateway.marvel.com"

    def __init__(self):
        pass

    @staticmethod
    def apiUrl(path):
        return Util.BASE_URL + path

# class ListParameters:
#     def __init__(self, parameters):
#         self.parameters = parameters
#         self.name = parameters["name"]
#         self.nameStartsWith = parameters["nameStartsWith"]
#         self.modifiedSince = parameters["modifiedSince"]
#         self.comics = parameters["comics"]
#
#     def toQuery(self):
#         return self.parameters


class CharactersListRequest:
    def __init__(self, parameters):
        self.parameters = parameters

    def run(self):
        pass


class EventsListRequest:
    PATH = "/v1/public/events"

    def __init__(self, parameters):
        self.parameters = marvel_api.authorization.Signature().sign(parameters)

    def send(self):
        response = requests.get(Util.apiUrl(EventsListRequest.PATH), self.parameters)
        print(response.json())
        return marvel_api.response.Response(response.json(), marvel_api.entities.Event)
