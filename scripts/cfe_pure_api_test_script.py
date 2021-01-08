import json
import requests # http requests (a lib)

'''
A simple test, not a unit test
'''
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/updates/'

def get_list(id=None):
    data = json.dumps({})
    if id is not None:
        data = json.dumps({'id':id})
    r = requests.get(BASE_URL+ENDPOINT, data =data)
    print (r.status_code)
    data =r.json()
    # print(data)
    # print (type(data)) # type(json.dumps(data))
    # for a in data:
    #     # print (a['id'])
    #     if a ['id'] == 1: 
    #         r2 = requests.get (BASE_URL+ENDPOINT + str(a['id']))
    #         # print (dir(r2))
    #         print (r2.json())

    return data

print(get_list())

def create_update():
    new_data = {
        'user':1,
        'content':'more testing after upgrading django'
    }
    r =requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_data))
    print (r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        #print r.json()
        return r.json()
    return r.text # at first, will get authenication failed message (with html data), default django security
# print(create_update())

def do_obj_update():
    new_data = {
        'id':122,
        'content':' tesging after upgrade, modif - changed from script'
    }
    r =requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data))
    # new_data = {
    #     'id':1,
    #     'content':'Some more Update from test script'
    # }
    # r =requests.put(BASE_URL+ENDPOINT,data=new_data)
    # print (r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        #print r.json()
        return r.json()
    return r.text

# print (do_obj_update())

def do_obj_delete():
    new_data = {
        'id':10
    }
    r =requests.delete(BASE_URL+ENDPOINT, data = json.dumps(new_data))
    # to delete from detail view we just need this
    # r =requests.delete(BASE_URL+ENDPOINT + '4/')

    # new_data = {
    #     'id':1,
    #     'content':'Some more Update from test script'
    # }
    # r =requests.put(BASE_URL+ENDPOINT,data=new_data)
    # print (r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        #print r.json()
        return r.json()
    return r.text

# print (do_obj_delete())