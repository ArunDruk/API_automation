import requests
import json

# res=requests.get("https://reqres.in/api/users?page=2")
# print(res.status_code)
# print(res.content)
#res.headers,res.content,res.status_code,res.ok

with open("E:\\API_automation\\GET_Request\\CreateUser.json",'r') as fr:
    json_input=fr.read()

#print(json_input)

req_input=json.loads(json_input)

#print(req_input)
res=requests.post("https://reqres.in/api/users",req_input)
# print(res.status_code)
# print(res.content)
# print(res.text)
res.json=json.loads(res.text)
print(res.json)