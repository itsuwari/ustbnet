import urllib.request
import urllib.parse


def login(username, passwd, v6):
    post_t = {
        '0MKKey': '123456789',
        'savePWD': 'on',
        'v6ip': v6,
        'DDDDD': username,
        'upass': passwd,
        'callback': 'dr1004',
        'R1': 0,
        'R2': 0,
        'R3': 0,
        'R6': 0,
        'para': 00,
        'terminal_type': 1
    }

    url = 'http://202.204.48.66/drcom/login?' + urllib.parse.urlencode(post_t)
    req = urllib.request.Request(url)
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
