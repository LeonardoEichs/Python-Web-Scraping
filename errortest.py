from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
else:
    if html is None:
        print("URL is not found")
    else:
        bsObj = BeautifulSoup(html.read())
        try:
            content = bsObj.h1
        except AttributeError as e:
            print("Tag was not found")
        else:
            if content == None:
                print("Tag was not found")
            else:
                print(content)
