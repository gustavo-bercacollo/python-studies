#Python Exercise #114 - Is the website accessible?

import urllib.request
from urllib.error import URLError

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except URLError:
    print(f'The site is not able in the moment')
else:
    print('It\'s ok!')