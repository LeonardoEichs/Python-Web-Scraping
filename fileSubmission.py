import requests

params = {'uploadFile' : open('downloaded/img/lrg%20(1).jpg', 'rb')}
r = requests.post("http://pythonscraping.com/files/processing2.php", files=params)
print(r.text)
