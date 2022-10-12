from json import JSONEncoder

class UtilEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__