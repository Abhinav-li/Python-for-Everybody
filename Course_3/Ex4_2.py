from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
cnt = int(input('Enter Count- '))
pos = int(input('Enter Position- '))

for i in range(cnt):
	html = urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')

	# Retrieve all of the anchor tags
	tags = soup('a')
	lst = []
	for tag in tags:
		lst.append(tag.get('href', None))
	url = lst[pos-1]
	print(lst[pos-1])
