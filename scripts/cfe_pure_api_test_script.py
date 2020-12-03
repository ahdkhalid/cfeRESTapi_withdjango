import json
import requests # http requests (a lib)

'''
A simple test, not a unit test
'''
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/updates/'

def get_list():
    r = requests.get(BASE_URL+ENDPOINT)
    print (r.status_code)
    data =r.json()
    print (type(data)) # type(json.dumps(data))
    for a in data:
        # print (a['id'])
        if a ['id'] == 1: 
            r2 = requests.get (BASE_URL+ENDPOINT + str(a['id']))
            # print (dir(r2))
            print (r2.json())

    return data

# get_list()

def create_update():
    new_data = {
        'user':1,
        'content':'Update from test script'
    }
    r =requests.delete(BASE_URL+ENDPOINT,data=new_data)
    print (r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        #print r.json()
        return r.json()
    return r.text # at first, will get authenication failed message (with html data), default django security
print(create_update())