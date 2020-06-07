#POST request is used for creating a new resource on the server.
#PUT request is used for updating resource on the server.

import requests
import json
import jsonpath

#API URL
url="https://reqres.in/api/users"

# Reading data from the file
file=open('E:\\API_automation\\GET_Request\\CreateUser.json','r')
json_input=file.read()

#Converting into Json format
requests_json=json.loads(json_input)

#For POST request we need to pass JSON as input
#print(requests_json)

#Make POST request with Json Input body
response=requests.post(url,requests_json)
print(response.content)

#Validating response code.
assert response.status_code==201,"Actual status code is different"

# Fetch header from response
#print(response.headers) # This prints all the header details present.

print(response.headers.get("Content-Length")) # This gives information about the particular header, here content-length

# Parse response to Json Format
response_json=json.loads(response.text)

#Pick Id using Json Path
id=jsonpath.jsonpath(response_json,'id') # This will return the list.
print(id[0]) # Print(id)
