import urllib.request, urllib.parse
import json, ssl

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.hostname_checks_common_name = False
ctx.very_mdoe = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    
    address = address.strip()
    parms=dict()
    parms['q'] = address
    
    url = serviceurl+urllib.parse.urlencode(parms)
    
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    
    try:
        js=json.loads(data)
    except:
        js=None
    
    if not js or 'features' not in js:
        print('=== Download error ===')
        print(data)
        break
    
    if len(js['features'])==0:
        print('=== Object not found ===')
        print(data)
        break
    
    plus_code = js['features'][0]["properties"]["plus_code"]
    print('Plus code ', plus_code)