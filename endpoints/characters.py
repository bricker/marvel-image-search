
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

