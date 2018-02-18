class Response:
    def __init__(self, data, klass):
        self.code = data["code"]
        self.status = data["status"]
        self.data = DataContainer(data["data"], klass)
        self.etag = data["etag"]
        self.copyright = data["copyright"]
        self.attributionText = data["attributionText"]
        self.attributionHtml = data["attributionHTML"]


class DataContainer:
    def __init__(self, data, klass):
        self.offset = data["offset"]
        self.limit = data["limit"]
        self.total = data["total"]
        self.count = data["count"]
        self.results = [klass(json) for json in data["results"]]
