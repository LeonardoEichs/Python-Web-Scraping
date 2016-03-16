from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)

nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    #print(name)
    print(name.get_text()) # get_text() strips all tags

# Number of times the prince appears
print("\nNumber of times \"the prince\" appears: ")
princeNumb = bsObj.findAll(text = "the prince")
print(len(princeNumb))

print("")
titleList = bsObj.findAll({"h1","h2","h3","h4","h5","h6"})
for titles in titleList:
    print(titles.get_text())
