import json
import requests
import os

ENDPOINT = "http://127.0.0.1:8000/api/status/"
AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
REFRESH_ENDPOINT = AUTH_ENDPOINT+"refresh/"
image_path = os.path.join(os.getcwd(), "image-example.png")

headers ={
    'content-type':'application/json',
    # 'Authorization': "JWT "+"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjEzNzQ4ODM0LCJlbWFpbCI6ImFoa2hhbGlkLmtoYWxpZEBnbWFpbC5jb20iLCJvcmlnX2lhdCI6MTYxMzc0ODUzNH0.ptNy8xzho_dvULazh4WroLKYPZb6hT3GnNV_sTvsBtM"
}
data = {
    'username':'ahkhalid.khalid@gmail.com',
    'password':'Khalid2django'
}
r = requests.post(AUTH_ENDPOINT,data=json.dumps(data), headers=headers)
token = r.json()#['token']
print (token)

# refresh_data={
#     'token':token
# }
# new_response = requests.post(REFRESH_ENDPOINT,data=json.dumps(refresh_data), headers=headers)
# new_token = new_response.json()
# print (new_token)

# headers ={
#     # 'content-type':'application/json',
#     'Authorization': 'JWT '+token,
# }
# with open(image_path, 'rb') as image:
#     file_data = {
#         'image': image
#     }
#     data = {'content':'some random content'}
#     posted_response = requests.post(ENDPOINT, data =data, headers=headers, files=file_data)
#     print (posted_response.text)

# headers ={
#     'content-type':'application/json',
#     'Authorization': 'JWT '+token,
# }
# data = {'content':'updated random content'}
# json_data = json.dumps(data)
# posted_response = requests.put(ENDPOINT +'21/', data =json_data, headers=headers)
# print (posted_response.text)


# get_endpoint = ENDPOINT +str(13)
# post_data = json.dumps({'content':'some random content'})

# r = requests.get(get_endpoint)
# print (r.text)

# r2 = requests.get(ENDPOINT)
# print (r2.status_code)

# post_headers ={
#     'content-type': 'application/json'
# }
# post_response = requests.post(ENDPOINT, data=post_data, headers=post_headers)
# print(post_response)










# def do_img(method='get', data={}, is_json=True, img_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     if img_path is not None:
#         with open(image_path, 'rb') as image:
#             file_data = {
#                 'image': image
#             }
#             r = requests.request(method, ENDPOINT, data=data, files=file_data, headers=headers)
#     else:
#         r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r



# do_img(
#     method='post', 
#     data={'user': 1, "content": ""}, 
#     is_json=False, 
#     img_path=image_path
#     )




# def do(method='get', data={}, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r

# do(data={'id': 12})

# do(method='delete', data={'user':1, 'id': 10})

# do(method='put', data={'id': 11, "content": "update  new content from script ", 'user': 1})

# do(method='post', data={"content": "some cool new content from test script", 'user': 1})

# create
# retrieve / list
# update
# delete