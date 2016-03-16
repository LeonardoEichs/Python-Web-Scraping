import requests

# Posts 'Ryan' in the form with name 'firstname'
# Posts 'Mitchell' in the form with name 'lastname'
params = {'firstname' : 'Ryan', 'lastname' : 'Mitchell'}
# Sends to the page listed in <form action='nameofpage.php'>
r = requests.post("http://pythonscraping.com/files/processing.php", params)
print(r.text)
