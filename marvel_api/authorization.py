from datetime import datetime
import hashlib
import json


class ApiCredentials:
    def __init__(self):
        creds = json.loads(open("marvel-credentials.json").read())
        self.publicKey = creds["public_key"]
        self.privateKey = creds["private_key"]


class Signature:
    def __init__(self):
        self.__apiCredentials = ApiCredentials()
        pass

    def sign(self, parameters):
        ts = str(datetime.now())
        hash = hashlib.md5(
            ts +
            self.__apiCredentials.privateKey +
            self.__apiCredentials.publicKey
        ).hexdigest()

        parameters["ts"] = ts
        parameters["hash"] = hash
        parameters["apikey"] = self.__apiCredentials.publicKey
        return parameters
