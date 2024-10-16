import time
import choose_quote
import requests

def comment(content, mid):
    headers = {
        "cookie": "SCF=AnlzcgfYchJBcs0QLAe-CmaWwUwK51wNMj1b2FiheAn0ZMzgP8TWzipcw6jGD0K6loWmpHAvXidk6aKtCqekfIE.; SUB=_2A25KDLHFDeRhGeFJ7lUT9yzJzTqIHXVpYEsNrDV6PUJbktAGLUH4kW1Nf4TyLSJeRpI6Bbwn-5Zq1qQp8FfwkXKV; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFcD0Zxavx0JMl70SskRya65NHD95QNS0-NeoMESKqcWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0MfS0zNeo-cSntt; ALF=1731219094; _T_WM=08b7c64ab86cf836aa86319b8caaaa7b; WEIBOCN_FROM=1110006030; MLOGIN=1; XSRF-TOKEN=faca74; M_WEIBOCN_PARAMS=oid%3D5089187093809415%26luicode%3D20000061%26lfid%3D5089187093809415%26uicode%3D20000061%26fid%3D5089187093809415; mweibo_short_token=21823e6545",
        "referer": f"https://m.weibo.cn/detail/{id}",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
    }

    data = {
        "content": content,
        "mid": mid,
        "st": 'faca74'
    }
    result = requests.post(url="https://m.weibo.cn/api/comments/create", headers=headers, data=data)
    print(result.content)



def send(content):
    headers = {
        "cookie": "SCF=AnlzcgfYchJBcs0QLAe-CmaWwUwK51wNMj1b2FiheAn0ZMzgP8TWzipcw6jGD0K6loWmpHAvXidk6aKtCqekfIE.; SUB=_2A25KDLHFDeRhGeFJ7lUT9yzJzTqIHXVpYEsNrDV6PUJbktAGLUH4kW1Nf4TyLSJeRpI6Bbwn-5Zq1qQp8FfwkXKV; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFcD0Zxavx0JMl70SskRya65NHD95QNS0-NeoMESKqcWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0MfS0zNeo-cSntt; ALF=1731219094; _T_WM=08b7c64ab86cf836aa86319b8caaaa7b; WEIBOCN_FROM=1110006030; MLOGIN=1; XSRF-TOKEN=faca74; mweibo_short_token=9c8731e7e6; M_WEIBOCN_PARAMS=lfid%3D1076037492558495%26luicode%3D20000174",
        "referer": "https://m.weibo.cn/compose/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
    }

    data = {
        "content": content,
        "st": 'faca74'
    }
    result = requests.post(url="https://m.weibo.cn/api/statuses/update", headers=headers, data=data)
    print(result.content)

#
# for i in range(0,5):
#     comment(choose_quote.choose_quote('quotes.txt'))
#     time.sleep(1)
