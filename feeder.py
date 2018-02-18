from google.cloud.vision import types


class VisionFeeder:
    def __init__(self, visionClient, esClient):
        self.visionClient = visionClient
        self.esClient = esClient

    def feedImage(self, docId, docTitle, imageUrl, imageBytes):
        image = types.Image(content=imageBytes)
        r = self.visionClient.label_detection(image=image)
    
        stringAnnotations = []
    
        for ann in r.label_annotations:
            stringAnnotations.append(ann.description)
    
        r = self.visionClient.landmark_detection(image=image)
        for ann in r.landmark_annotations:
            stringAnnotations.append(ann.description)
    
        r = self.visionClient.logo_detection(image=image)
        for ann in r.logo_annotations:
            stringAnnotations.append(ann.description)
    
        r = self.visionClient.text_detection(image=image)
        for ann in r.text_annotations:
            stringAnnotations.append(ann.description)
    
        if len(stringAnnotations) > 0:
            doc = {
                "id": "event-"+docId,
                "name": docTitle,
                "url": imageUrl,
                "objects": stringAnnotations
            }
    
            try:
                print(imageUrl)
                print(stringAnnotations)
                self.esClient.index(index="marvel", doc_type="images", body=doc)
            except Exception as err:
                print("ERROR: " + err.message)
    
        # Facial detection (goes to different index)
        r = self.visionClient.face_detection(image=image)
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
                "id": "event-"+docId,
                "name": docTitle,
                "url": imageUrl,
                "objects": faceAnnotations
            }
    
            try:
                self.esClient.index(index="marvelfaces", doc_type="images", body=doc)
            except Exception as err:
                print("ERROR: " + err.message)
