import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
repeat_count = int(input('Enter count: '))
target_position = int(input('Enter position: '))-1


for i in range(repeat_count):
    # Retrieve HTML of the current URL
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve all of the anchor tags
    tags = soup('a')
    
    # Get the link
    tag =tags[target_position]
    url = tag.get('href', None)
    print("Retrieving:", url)
    
    # print(tag.get('href', None))
    
print("Last name:", tags[target_position].text)
# Steps 
# 1. Find the link at position 3
# 2. Follow that link and repeat this process 4 times.
# 3. Last link is the last name you retreive.