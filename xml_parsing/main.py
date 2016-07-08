from urllib.request import urlopen
from xml.etree.ElementTree import parse

# Download the RSS feed and parse it
url = urlopen("http://planet.python.org/rss20.xml")
doc = parse(url)

# Extract and output tags of interest
for item in doc.iterfind("channel/item"):
    title = item.findtext("title")
    date = item.findtext("pubDate")
    link = item.findtext("link")

    print(title)
    print(date)
    print(link)
    print()
