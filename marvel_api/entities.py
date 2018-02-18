class URL:
    def __init__(self, data):
        self.type = data["type"]
        self.url = data["url"]


class TextObject:
    def __init__(self, data):
        self.type = data["type"]
        self.language = data["language"]
        self.text = data["text"]


class SummaryView:
    def __init__(self, data):
        self.resourceUri = data["resourceURI"]
        self.name = data["name"]


class SeriesSummary(SummaryView):
    pass


class ComicSummary(SummaryView):
    pass


class EventSummary(SummaryView):
    pass


class ComicDate:
    def __init__(self, data):
        print("Got ComicData - wat do")
        pass


class ComicPrice:
    def __init__(self, data):
        print("Got ComicPrice - wat do")
        pass


class ResourceList:
    def __init__(self, data, klass):
        self.available = data["available"]
        self.returned = data["returned"]
        self.collectionUri = data["collectionURI"]
        self.items = [klass(json) for json in data["items"]]


class Image:
    # https://developer.marvel.com/documentation/images
    def __init__(self, data):
        self.path = data["path"]
        self.extension = data["extension"]

    def fullPath(self, variant):
        if variant == "full-size":
            return self.path + "." + self.extension
        else:
            return self.path + "/" + variant + "." + self.extension


class Comic:
    def __init__(self, data):
        self.id = data["id"]
        self.digitalId = data["digitalId"]
        self.title = data["title"]
        self.issueNumber = data["issueNumber"]
        self.variantDescription = data["variantDescription"]
        self.description = data["description"]
        self.modified = data["modified"]
        self.isbn = data["isbn"]
        self.upc = data["upc"]
        self.diamondCode = data["diamondCode"]
        self.ean = data["ean"]
        self.issn = data["issn"]
        self.format = data["format"]
        self.pageCount = data["pageCount"]
        self.textObjects = [TextObject(json) for json in data["textObjects"]]
        self.resourceUri = data["resourceUri"]
        self.urls = [URL(json) for json in data["urls"]]
        self.series = SeriesSummary(data["series"])
        self.variants = [ComicSummary(json) for json in data["variants"]]
        self.collections = [ComicSummary(json) for json in data["collections"]]
        self.collectedIssues = [ComicSummary(json) for json in data["collectedIssues"]]
        self.dates = [ComicDate(json) for json in data["dates"]]
        self.prices = [ComicPrice(json) for json in data["prices"]]
        self.thumbnail = Image(data["thumbnail"])
        self.images = [Image(json) for json in data["images"]]
        self.creators = ResourceList(data["creators"], Creator)
        self.characters = ResourceList(data["characters"], Character)
        self.stories = ResourceList(data["stories"], Story)
        self.events = ResourceList(data["events"], Event)


class Series:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.description = data["description"]
        self.resourceUri = data["resourceURI"]
        self.urls = [URL(json) for json in data["urls"]]
        self.startYear = data["startYear"]
        self.endYear = data["endYear"]
        self.rating = data["rating"]
        self.modified = data["modified"]
        self.thumbnail = Image(data["thumbnail"])
        self.comics = ResourceList(data["comics"], Comic)
        self.stories = ResourceList(data["stories"], Story)
        self.events = ResourceList(data["events"], Event)
        self.characters = ResourceList(data["characters"], Character)
        self.creators = ResourceList(data["creators"], Creator)
        self.next = SeriesSummary(data["next"])
        self.prev = SeriesSummary(data["prev"])


class Event:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.description = data["description"]
        self.resourceUri = data["resourceURI"]
        self.urls = [URL(json) for json in data["urls"]]
        self.modified = data["modified"]
        self.start = data["start"]
        self.end = data["end"]
        self.thumbnail = Image(data["thumbnail"])
        self.comics = ResourceList(data["comics"], Comic)
        self.stories = ResourceList(data["stories"], Story)
        self.series = ResourceList(data["series"], Series)
        self.characters = ResourceList(data["characters"], Character)
        self.creators = ResourceList(data["creators"], Creator)
        self.next = EventSummary(data["next"])
        self.prev = EventSummary(data["prev"])


class Story:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.description = data["description"]
        self.resourceUri = data["resourceURI"]
        self.type = data["type"]
        self.modified = data["modified"]
        self.thumbnail = Image(data["thumbnail"])
        self.comics = ResourceList(data["comics"], Comic)
        self.series = ResourceList(data["series"], Series)
        self.events = ResourceList(data["events"], Event)
        self.characters = ResourceList(data["characters"], Character)
        self.creators = ResourceList(data["creators"], Creator)
        self.originalissue = ComicSummary(data["originalissue"])


class Creator:
    def __init__(self, data):
        self.id = data["id"]
        self.firstName = data["firstName"]
        self.middleName = data["middleName"]
        self.lastName = data["lastName"]
        self.suffix = data["suffix"]
        self.fullName = data["fullName"]
        self.modified = data["modified"]
        self.resourceUri = data["resourceURI"]
        self.urls = [URL(json) for json in data["urls"]]
        self.thumbnail = Image(data["thumbnail"])
        self.series = ResourceList(data["series"], Series)
        self.stories = ResourceList(data["stories"], Story)
        self.comics = ResourceList(data["comics"], Comic)
        self.events = ResourceList(data["events"], Event)


class Character:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.modified = data["modified"]
        self.resourceUri = data["resourceURI"]
        self.urls = [URL(url_json) for url_json in data["urls"]]
        self.thumbnail = data["thumbnail"]
        self.comics = [Comic(json) for json in data["comics"]]
        self.stories = [Story(json) for json in data["stories"]]
        self.events = [Event(json) for json in data["events"]]
        self.series = [Series(json) for json in data["series"]]
