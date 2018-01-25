import json, urllib.request, requests

#url = "http://httpbin.org/get?id=1&type=amilcar&lecture=kyle"
#page = urllib.request.urlopen(url)
#page_on_text = page.read()

#myJ = json.loads(page_on_text)

#print (myJ["args"])

#print (dir(requests))


url = 'http://httpbin.org/post'
data = {'key':'value','key2':'value2'}

#print (help(requests.post))
r = requests.post(url, json=data )
myJ2 = json.loads(r.text)
print (r.text)
print(myJ2.keys())
