from google.cloud import vision
from google.cloud.vision import types


class VisionFeeder:
    def __init__(self):
        self.__client = vision.ImageAnnotatorClient()

    def feedImage(self, imageUrl):
        pass
