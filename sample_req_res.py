####################################################################################################

# import requests
#
# url="http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?wsdl"
#
# response=requests.get(url)
# #print(response.headers)
# print(response.content.find(10))
####################################################################################################
# import requests
# import shutil  # Shell Utilities module (manipulate the filesystem, make archives, etc.)
# # This is the image url.
# image_url="https://upload.wikimedia.org/wikipedia/commons/2/20/Namma_Metro_Phase_1_line_map.png"
# # Open the url image, set stream to True, this will return the stream content.
# resp = requests.get(image_url, stream=True)
# # Open a local file with wb ( write binary ) permission.
# local_file = open('Metro_image.jpg', 'wb')
# # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
# resp.raw.decode_content = True
# # Copy the response stream raw data to local image file.
# shutil.copyfileobj(resp.raw, local_file)
# # Remove the image url response object.
# del resp

####################################################################################################
import requests
#httpbin.org
####################################################################################################
# #To see the available options inside the response object by using help and dir functions
#r=requests.get("https://xkcd.com/353/")
#print(dir(r))
#print(help(r))
#print(r.text)

####################################################################################################
# TO Download the image using r.content
#r=requests.get("https://imgs.xkcd.com/comics/python.png")
# with open("comic_python.png",'wb') as f:
#     f.write(r.content)

####################################################################################################
# # To check the status code and OK, Ok will return TRUE for status code less than 400
# print(r.ok)
# print(r.status_code)
####################################################################################################
# payload={'page':2,'count':25}
# r=requests.get("https://httpbin.org/get",params=payload)
# #print(r.text)
# print(r.url)
####################################################################################################
# # To POST information, POST Method
# payload={"Username":"ARUN DRUK","Password":"Testing123"}
# r=requests.post("https://httpbin.org/post",data=payload)
# #print(r.text) # The response comes as a JSON, so we can use JSON method instead of text
#
# r.dic1=r.json()
# print(r.dic1["form"])
####################################################################################################
# For Auth request
r=requests.get("https://httpbin.org/basic-auth/ArunDruk/Testing123",auth=("ArunDruk","Testing123"))
print(r.text)





