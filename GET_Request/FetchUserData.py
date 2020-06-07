import requests
import json
import jsonpath

#API URL
url="https://reqres.in/api/users?page=2"

#Send Get request
response=requests.get(url)

#print(response)
print(response.status_code)

#print(response.content)
#print(response.headers)

#parse response to Json format
json_response=json.loads(response.text)
#print(json_response)

#Fetch value using Json Path
pages=jsonpath.jsonpath(json_response,"total")
# The above pages is going to return the list and we are going to take the first element.
print(pages[0])

