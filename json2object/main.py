import json

class JSONObject:

    def __init__(self, d):
        self.__dict__ = d

def json2object(j):
    return json.loads(j, object_hook=JSONObject)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__ }
    d.update(vars(obj))
    return d

classes = {
        'Point': Point
        }

def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls) # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d


if __name__ == '__main__':

    d = '{"name": "ACME", "shares": 50, "price": 490.1}'
    d1 = json2object(d)
    print(d1.name)
    print(d1.shares)
    print(d1.price)
    p = Point(2, 3)
    s = json.dumps(p, default=serialize_instance)
    print(s)
    a = json.loads(s, object_hook=unserialize_object)
    print(a.x)
    print(a.y)
