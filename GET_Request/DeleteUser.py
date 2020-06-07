import requests

#API URL
url="https://reqres.in/api/users/2"

response=requests.delete(url)

print(response.status_code) # When the resource is getting deleted successfully the status code should be 204