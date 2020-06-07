#POST request is used for creating a new resource on the server.
#PUT request is used for updating resource on the server.

import requests
import json
import jsonpath

#API URL
url="https://reqres.in/api/users"

def test_creating_newUser():
    file=open('E:\\API_automation\\GET_Request\\CreateUser.json','r')
    json_input=file.read()
    requests_json=json.loads(json_input)
    response=requests.post(url,requests_json)
    #print(response.content)
    assert response.status_code==201,"Actual status code is different"
    # print(response.headers.get("Content-Length")) # This gives information about the particular header, here content-length
    # response_json=json.loads(response.text)
    # id=jsonpath.jsonpath(response_json,'id') # This will return the list.
    # print(id[0]) # Print(id)
