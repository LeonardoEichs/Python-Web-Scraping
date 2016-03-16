import requests

session = requests.Session()

params = {'username':'anything','password':'password'}
s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print("Cookies is set to: ")
print(s.cookies.get_dict())
print("--------------------")
print("Going to profile page...")
s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(s.text)
