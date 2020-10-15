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


def getv6():
        import socket
        url = 'http://cippv6.ustb.edu.cn/get_ip.php'
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(req).read()
        address = str(res)
        address = address[15:-11]
        print(address)
        return address

try:
    v6 = getv6()
except TimeoutError:
    v6 = ''
login('account', 'password', v6)
