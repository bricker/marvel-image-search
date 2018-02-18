class URL:
    def __init__(self, data):
        self.type = data.get("type")
        self.url = data.get("url")


class TextObject:
    def __init__(self, data):
        self.type = data.get("type")
        self.language = data.get("language")
        self.text = data.get("text")


class SummaryView:
    def __init__(self, data):
        if data:
            self.resourceUri = data.get("resourceURI")
            self.name = data.get("name")


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
        self.available = data.get("available")
        self.returned = data.get("returned")
        self.collectionUri = data.get("collectionURI")
        self.items = [klass(json) for json in data.get("items", {})]


class Image:
    # https://developer.marvel.com/documentation/images
    def __init__(self, data):
        self.path = data.get("path")
        self.extension = data.get("extension")

    def fullPath(self, variant):
        if variant == "full-size":
            return self.path + "." + self.extension
        else:
            return self.path + "/" + variant + "." + self.extension


class Comic:
    def __init__(self, data):
        self.id = data.get("id")
        self.digitalId = data.get("digitalId")
        self.title = data.get("title")
        self.issueNumber = data.get("issueNumber")
        self.variantDescription = data.get("variantDescription")
        self.description = data.get("description")
        self.modified = data.get("modified")
        self.isbn = data.get("isbn")
        self.upc = data.get("upc")
        self.diamondCode = data.get("diamondCode")
        self.ean = data.get("ean")
        self.issn = data.get("issn")
        self.format = data.get("format")
        self.pageCount = data.get("pageCount")
        self.textObjects = [TextObject(json) for json in data.get("textObjects", {})]
        self.resourceUri = data.get("resourceUri")
        self.urls = [URL(json) for json in data.get("urls", {})]
        self.series = SummaryView(data.get("series", {}))
        self.variants = [SummaryView(json) for json in data.get("variants", {})]
        self.collections = [SummaryView(json) for json in data.get("collections", {})]
        self.collectedIssues = [SummaryView(json) for json in data.get("collectedIssues", {})]
        self.dates = [ComicDate(json) for json in data.get("dates", {})]
        self.prices = [ComicPrice(json) for json in data.get("prices", {})]
        self.thumbnail = Image(data.get("thumbnail", {}))
        self.images = [Image(json) for json in data.get("images", {})]
        self.creators = ResourceList(data.get("creators", {}), Creator)
        self.characters = ResourceList(data.get("characters", {}), Character)
        self.stories = ResourceList(data.get("stories", {}), Story)
        self.events = ResourceList(data.get("events", {}), Event)


class Series:
    def __init__(self, data):
        self.id = data.get("id")
        self.title = data.get("title")
        self.description = data.get("description")
        self.resourceUri = data.get("resourceURI")
        self.urls = [URL(json) for json in data.get("urls", {})]
        self.startYear = data.get("startYear")
        self.endYear = data.get("endYear")
        self.rating = data.get("rating")
        self.modified = data.get("modified")
        self.thumbnail = Image(data.get("thumbnail", {}))
        self.comics = ResourceList(data.get("comics", {}), Comic)
        self.stories = ResourceList(data.get("stories", {}), Story)
        self.events = ResourceList(data.get("events", {}), Event)
        self.characters = ResourceList(data.get("characters", {}), Character)
        self.creators = ResourceList(data.get("creators", {}), Creator)
        self.next = SummaryView(data.get("next", {}))
        self.prev = SummaryView(data.get("prev", {}))


class Event:
    def __init__(self, data):
        self.id = data.get("id")
        self.title = data.get("title")
        self.description = data.get("description")
        self.resourceUri = data.get("resourceURI")
        self.urls = [URL(json) for json in data.get("urls", {})]
        self.modified = data.get("modified")
        self.start = data.get("start")
        self.end = data.get("end")
        self.thumbnail = Image(data.get("thumbnail", {}))
        self.comics = ResourceList(data.get("comics", {}), Comic)
        self.stories = ResourceList(data.get("stories", {}), Story)
        self.series = ResourceList(data.get("series", {}), Series)
        self.characters = ResourceList(data.get("characters", {}), Character)
        self.creators = ResourceList(data.get("creators", {}), Creator)
        self.next = SummaryView(data.get("next", {}))
        self.prev = SummaryView(data.get("prev", {}))


class Story:
    def __init__(self, data):
        self.id = data.get("id")
        self.title = data.get("title")
        self.description = data.get("description")
        self.resourceUri = data.get("resourceURI")
        self.type = data.get("type")
        self.modified = data.get("modified")
        self.thumbnail = Image(data.get("thumbnail", {}))
        self.comics = ResourceList(data.get("comics", {}), Comic)
        self.series = ResourceList(data.get("series", {}), Series)
        self.events = ResourceList(data.get("events", {}), Event)
        self.characters = ResourceList(data.get("characters", {}), Character)
        self.creators = ResourceList(data.get("creators", {}), Creator)
        self.originalissue = SummaryView(data.get("originalissue", {}))


class Creator:
    def __init__(self, data):
        self.id = data.get("id")
        self.firstName = data.get("firstName")
        self.middleName = data.get("middleName")
        self.lastName = data.get("lastName")
        self.suffix = data.get("suffix")
        self.fullName = data.get("fullName")
        self.modified = data.get("modified")
        self.resourceUri = data.get("resourceURI")
        self.urls = [URL(json) for json in data.get("urls", {})]
        self.thumbnail = Image(data.get("thumbnail", {}))
        self.series = ResourceList(data.get("series", {}), Series)
        self.stories = ResourceList(data.get("stories", {}), Story)
        self.comics = ResourceList(data.get("comics", {}), Comic)
        self.events = ResourceList(data.get("events", {}), Event)


class Character:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.description = data.get("description")
        self.modified = data.get("modified")
        self.resourceUri = data.get("resourceURI")
        self.urls = [URL(url_json) for url_json in data.get("urls", {})]
        self.thumbnail = data.get("thumbnail")
        self.comics = [Comic(json) for json in data.get("comics", {})]
        self.stories = [Story(json) for json in data.get("stories", {})]
        self.events = [Event(json) for json in data.get("events", {})]
        self.series = [Series(json) for json in data.get("series", {})]
