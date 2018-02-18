import marvel_api.endpoints
import marvel_api.authorization
from google.cloud import vision
from google.cloud.vision import types
import requests
import elasticsearch
import base64

# eventsRequest = marvel_api.endpoints.EventsListRequest(parameters={})
# eventsResponse = eventsRequest.send()
# feeder = VisionFeeder()

es = elasticsearch.Elasticsearch("10.19.189.64:9200")
visionClient = vision.ImageAnnotatorClient()

offset = 0
retries = 0
while True:
    params = {
        "offset": offset
    }

    response = requests.get("https://gateway.marvel.com/v1/public/events", marvel_api.authorization.Signature().sign(params))
    results = response.json().get("data", {}).get("results", [])

    if len(results) == 0:
        if retries > 3:
            print("NO RESULTS MAX RETRIES. EXITING")
            break
        else:
            print("NO RESULTS, TRY AGAIN")
            retries += 1
            continue

    for event in results:
        offset += 1
        imageJsonObject = event.get("thumbnail")

        if imageJsonObject:
            eventId = str(event.get("id", base64.b64encode(event.get("title", ""))))

            imageUrl = imageJsonObject["path"] + "." + imageJsonObject["extension"]
            imageResponse = requests.get(imageUrl)
            imageBytes = imageResponse.content

            image = types.Image(content=imageBytes)
            r = visionClient.label_detection(image=image)

            stringAnnotations = []

            for ann in r.label_annotations:
                stringAnnotations.append(ann.description)

            r = visionClient.landmark_detection(image=image)
            for ann in r.landmark_annotations:
                stringAnnotations.append(ann.description)

            r = visionClient.logo_detection(image=image)
            for ann in r.logo_annotations:
                stringAnnotations.append(ann.description)

            r = visionClient.text_detection(image=image)
            for ann in r.text_annotations:
                stringAnnotations.append(ann.description)

            if len(stringAnnotations) > 0:
                doc = {
                    "id": "event-"+eventId,
                    "name": event.get("title", "NO TITLE"),
                    "url": imageUrl,
                    "objects": stringAnnotations
                }

                print("[" + str(offset) + "] Indexing: " + event["title"])
                try:
                    es.index(index="marvel", doc_type="images", body=doc)
                except Exception as err:
                    print("ERROR: " + err.message)

            # Facial detection (goes to different index)
            r = visionClient.face_detection(image=image)
            faceAnnotations = []
            for ann in r.face_annotations:
                if ann.joy_likelihood == "VERY_LIKELY":
                    faceAnnotations.append("joy")
                    faceAnnotations.append("happy")
                    faceAnnotations.append("smile")

                if ann.sorrow_likelihood == "VERY_LIKELY":
                    faceAnnotations.append("sorrow")
                    faceAnnotations.append("sad")
                    faceAnnotations.append("frown")

                if ann.anger_likelihood == "VERY_LIKELY":
                    faceAnnotations.append("anger")
                    faceAnnotations.append("angry")
                    faceAnnotations.append("mad")

                if ann.surprise_likelihood == "VERY_LIKELY":
                    faceAnnotations.append("surprise")
                    faceAnnotations.append("surprised")

                if ann.headwear_likelihood == "VERY_LIKELY":
                    faceAnnotations.append("headwear")
                    faceAnnotations.append("helmet")
                    faceAnnotations.append("hat")

            if len(faceAnnotations) > 0:
                doc = {
                    "id": "event-"+eventId,
                    "name": event.get("title", "NO TITLE"),
                    "url": imageUrl,
                    "objects": faceAnnotations
                }

                print("[" + str(offset) + "] Indexing FACES: " + event["title"])
                try:
                    es.index(index="marvelfaces", doc_type="images", body=doc)
                except Exception as err:
                    print("ERROR: " + err.message)
