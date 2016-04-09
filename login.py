import urllib.request
import urllib.parse


def login(username, passwd, v6):
    post_t = {
        '0MKKey': '123456789',
        'savePWD': 'on',
        'v6ip': v6,
        'DDDDD': username,
        'upass': passwd
    }

    post = urllib.parse.urlencode(post_t)
    post = post.encode('utf-8')
    url = 'http://202.204.48.66/v6'
    req = urllib.request.Request(url, data=post)
    res = urllib.request.urlopen(req)
    return res.getcode()


# print(req)
def getv6():
    url = 'http://[2001:da8:ad:3213::3]:9002/v6'
    req = urllib.request.Request(url)
    res = urllib.request.urlopen(req).read()
    address = str(res)
    start = int(address.find('value=')) + 7
    end = int(address.find('></FORM>')) - 1
    address = address[start:end]
    return address

try:
    v6 = getv6()
except TimeoutError:
    v6 = ''
login('replace with your student id', 'your password', v6)
