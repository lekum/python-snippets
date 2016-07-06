import json

class JSONObject:

    def __init__(self, d):
        self.__dict__ = d

def json2object(j):
    return json.loads(j, object_hook=JSONObject)

if __name__ == '__main__':

    d = '{"name": "ACME", "shares": 50, "price": 490.1}'
    d1 = json2object(d)
    print(d1.name)
    print(d1.shares)
    print(d1.price)
