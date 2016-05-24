import requests
from lxml.html import fromstring

def get_title(url):
    """ Get the url title """
    r = requests.get(url)
    tree = fromstring(r.content)
    return tree.findtext('.//title')
