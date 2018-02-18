import marvel_api.endpoints
import marvel_api.authorization
from vision_feeder.feeder import VisionFeeder
import requests

# eventsRequest = marvel_api.endpoints.EventsListRequest(parameters={})
# eventsResponse = eventsRequest.send()

response = requests.get("https://gateway.marvel.com/v1/public/events", marvel_api.authorization.Signature().sign({}))
feeder = VisionFeeder()

# print(response.json())
for event in response.json()["data"]["results"]:
    print(event)
# httpClient = requests.get(imageUrl)
