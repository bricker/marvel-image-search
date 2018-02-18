from datetime import datetime
import hashlib
import json


class ApiCredentials:
    def __init__(self):
        creds = json.loads(open("credentials.json"))
        self.publicKey = creds["public_key"]
        self.privateKey = creds["private_key"]


class ApiSigner:
    def __init__(self):
        self.__apiCredentials = ApiCredentials()
        pass

    def signature(self):
        ts = str(datetime.now())
        params = {
            "ts": ts,
            "hash": hashlib.md5(
                ts +
                self.__apiCredentials.privateKey +
                self.__apiCredentials.publicKey
            )
        }

        return params
[]