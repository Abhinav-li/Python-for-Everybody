import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET 
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
	address = input ('Enter Location ')
	if len(address) < 1: break

	data = urllib.request.urlopen(address, context = ctx).read()
	print('Retrieved ',len(data), ' characters')
	

	tree = ET.fromstring(data)

	comments = tree.findall('.//count')
	cnt = 0
	for item in comments:
		print("Count ", item.text)
		cnt = cnt + int(item.text)

	print(cnt)
	