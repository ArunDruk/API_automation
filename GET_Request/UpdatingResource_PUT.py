#POST request is used for creating a new resource on the server.
#PUT request is used for updating resource on the server.

import requests
import json
import jsonpath

#API URL
url="https://reqres.in/api/users/2"

# Reading data from the file
file=open('E:\\API_automation\\GET_Request\\CreateUser.json','r')
json_input=file.read()

#Converting into Json format
requests_json=json.loads(json_input)

print(requests_json)

#Make PUT request with Json Input body
response=requests.put(url,requests_json)
#print(response.content)

#Validating response code.
assert response.status_code==200,"Actual status code is different"

# Fetch header from response
#print(response.headers) # This prints all the header details present.

#print(response.headers.get("Content-Length")) # This gives information about the particular header, here content-length

# Parse response to Json Format
response_json=json.loads(response.text)


updated_time=jsonpath.jsonpath(response_json,'updatedAt') # This will return the list.
print(updated_time[0]) # Print(id)
