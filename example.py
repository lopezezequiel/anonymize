import urllib
import urllib2
import requests
from torify import enable_proxy, disable_proxy

#This url returns your ip as plain text
url = 'http://icanhazip.com'

def test_urllib():
    print 'urllib: %s' % urllib.urlopen(url).read()

def test_urllib2():
    print 'urllib2: %s' % urllib.urlopen(url).read()

def test_requests():
    print 'requests: %s' % requests.get(url).text


enable_proxy()

test_urllib()
test_urllib2()
test_requests()

disable_proxy()

test_urllib()
test_urllib2()
test_requests()
