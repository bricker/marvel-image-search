import marvel_api.endpoints
import marvel_api.authorization
from google.cloud import vision
import feeder
import feed_containers
import requests
import elasticsearch
import base64

# eventsRequest = marvel_api.endpoints.EventsListRequest(parameters={})
# eventsResponse = eventsRequest.send()
# feeder = VisionFeeder()

esClient = elasticsearch.Elasticsearch("10.21.154.54:9200")
visionClient = vision.ImageAnnotatorClient()
visionFeeder = feeder.VisionFeeder(visionClient, esClient)


def runFeeder(entityName, entityContainerClass):
    offset = 0
    retries = 0

    while True:
        params = {
            "offset": offset
        }

        params = marvel_api.authorization.Signature().sign(params)
        response = requests.get("https://gateway.marvel.com/v1/public/"+entityName, params)
        results = response.json().get("data", {}).get("results", [])

        if len(results) == 0:
            if retries > 3:
                print("NO RESULTS MAX RETRIES. EXITING")
                break
            else:
                print("NO RESULTS, TRY AGAIN")
                retries += 1
                continue

        for obj in results:
            offset += 1
            imageJsonObject = obj.get("thumbnail")

            if imageJsonObject:
                if "image_not_available" in imageJsonObject["path"]:
                    print("NO IMAGE: SKIPPING")
                    continue
                try:
                    feederContainer = entityContainerClass(obj)
                    imageUrl = imageJsonObject["path"] + "." + imageJsonObject["extension"]
                    imageResponse = requests.get(imageUrl)
                    imageBytes = imageResponse.content

                    print("[" + str(offset) + "] Indexing: " + feederContainer.title)
                    visionFeeder.feedImage(feederContainer.id, feederContainer.title, imageUrl, imageBytes)
                except Exception as err:
                    print("ERROR: " + err.message)


if __name__ == "__main__":
    for entity in [
        # ["events", feed_containers.EventFeedContainer],
        ["comics", feed_containers.ComicFeedContainer],
        ["characters", feed_containers.CharacterFeedContainer],
        ["stories", feed_containers.StoryFeedContainer],
        ["series", feed_containers.SeriesFeedContainer],
        ["creators", feed_containers.CreatorFeedContainer]
    ]:
        print("Running " + entity[0])
        runFeeder(entity[0], entity[1])
