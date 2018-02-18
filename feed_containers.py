import base64

class BaseFeedContainer:
    pass


class CharacterFeedContainer(BaseFeedContainer):
    def __init__(self, data):
        self.title = data.get("name", "NO TITLE")
        self.id = str(data.get("id", base64.b64encode(self.title)))


class ComicFeedContainer:
    def __init__(self, data):
        self.title = data.get("title", "NO TITLE")
        self.id = str(data.get("id", base64.b64encode(self.title)))


class EventFeedContainer:
    def __init__(self, data):
        self.title = data.get("title", "NO TITLE")
        self.id = str(data.get("id", base64.b64encode(self.title)))


class SeriesFeedContainer:
    def __init__(self, data):
        self.title = data.get("title", "NO TITLE")
        self.id = str(data.get("id", base64.b64encode(self.title)))


class CreatorFeedContainer:
    def __init__(self, data):
        self.title = data.get("fullName", "NO TITLE")
        self.id = str(data.get("id", base64.b64encode(self.title)))


class StoryFeedContainer:
    def __init__(self, data):
        self.title = data.get("title", "NO TITLE")
        self.id = str(data.get("id", base64.b64encode(self.title)))
