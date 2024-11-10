import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url)<1:
    url='http://py4e-data.dr-chuck.net/comments_2096335.xml'
    
print('Retrieving', url)

# Read the XML data from the URL using urlib
uh=urllib.request.urlopen(url)

# Read the data
data=uh.read()
print('Retrieved', len(data),'characters')

# Parsing XML using 'fromstring'
tree = ET.fromstring(data)
counts = tree.findall('.//count')
nums = list()
for result in counts:
    nums.append(int(result.text))

print('Count:', len(nums))
print('Sum:', sum(nums))

