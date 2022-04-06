import requests
import json 

f = open('keys.json')
keys = json.load(f)

get_headers = {
    "X-Parse-Application-Id": keys['appId'],
    "X-Parse-REST-API-Key": keys['apiKey']
}

post_headers = {
    "X-Parse-Application-Id": keys['appId'],
    "X-Parse-REST-API-Key": keys['apiKey'],
    "X-Parse-Master-Key": keys['masterKey'],
    "Content-Type": "application/json"
}

endpoint="https://parseapi.back4app.com/classes/maindb"

def get_data():
    r = requests.get(endpoint, headers=get_headers, timeout= 2000)
    r_j = r.json()
    res = r_j['results']
    return res

def write_data(sender, content):
    d = {
        "sender": sender,"content": content
    }
    d_j = json.dumps(d)
    print(d_j)
    r = requests.post(endpoint, headers=post_headers, data= d_j)
    return r.json()

