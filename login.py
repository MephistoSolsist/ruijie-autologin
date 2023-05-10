import requests
def login():
    url = 'http://10.80.253.2:9090/zportal/login/do' 
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '330',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'JSESSIONID=B26E5C4F48ADEE085943A643255CB478; rememberPassword=true; serviceId=; username=xxxxxx; password=xxxxxx; failCounter=0',
        'Host': '10.80.253.2:9090',
        'Origin': 'http://10.80.253.2:9090',
        'Referer': 'http://10.80.253.2:9090/zportal/loginForWeb?wlanuserip=c1c826bb9a2d5fed6036ade83c023bbb&wlanacname=001e78ceef4e1aa23efbe25d2ac3a27e&ssid=6b5b6e00645c8116&nasip=c77443f80d97f4f46315ab96e6638a81&snmpagentip=&mac=7887f589f7a7a80b77c98857b14e0b8d&t=wireless-v2&url=c9673a58c390d256016fcd5e988d3caf65b35707911972c279f763c4cfe3fad1&apmac=&nasid=001e78ceef4e1aa23efbe25d2ac3a27e&vid=4ceed730fc506a0b&port=d772a640b80f6f88&nasportid=5b9da5b08a53a540871303b4f6662eb2404ade801be007504c364e90642be0e5',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/113.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }
    data = {
        "username": "xxxxxxx",
        "pwd": "xxxxxx",
        "validCode": "",
        "validCodeFlag": "false",
        "ssid": "6b5b6e00645c8116",
        "mac": "7887f589f7a7a80b77c98857b14e0b8d",
        "t": "wireless-v2",
        "wlanacname": "001e78ceef4e1aa23efbe25d2ac3a27e",
        "url": "c9673a58c390d256016fcd5e988d3caf65b35707911972c279f763c4cfe3fad1",
        "nasip": "c77443f80d97f4f46315ab96e6638a81",
        "wlanuserip": "c1c826bb9a2d5fed6036ade83c023bbb"
    }
    return requests.post(url=url, data=data, headers=headers)
