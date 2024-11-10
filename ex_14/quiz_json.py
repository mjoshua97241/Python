import urllib.request, urllib.parse
import json,ssl

# data = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Brent"
#   }
# ]'''

url = input('Enter location: ')
if len(url)<1:
    url='http://py4e-data.dr-chuck.net/comments_2096336.json'
    
print('Retrieving', url)

# Read the data
uh=urllib.request.urlopen(url)
data = uh.read().decode()

print('Retrieved', len(data),'characters')

# Parsing the data
infor = json.loads(data)
info = infor["comments"]
# print(infor["comments"][0])

count = 0
num=list()
# Loop over the array and get the count.txt
for item in info:
    count=count+1
    num.append(int(item["count"]))
    
    # print(item["count"])
    
print('Count: ', count)
print('Sum: ', sum(num))
#     print('Id', item['id'])
#     print('Attribute', item['x'])