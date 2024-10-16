# import requests
#
# headers = {
# "cookie": "SCF=AnlzcgfYchJBcs0QLAe-CmaWwUwK51wNMj1b2FiheAn0ZMzgP8TWzipcw6jGD0K6loWmpHAvXidk6aKtCqekfIE.; SUB=_2A25KDLHFDeRhGeFJ7lUT9yzJzTqIHXVpYEsNrDV6PUJbktAGLUH4kW1Nf4TyLSJeRpI6Bbwn-5Zq1qQp8FfwkXKV; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFcD0Zxavx0JMl70SskRya65NHD95QNS0-NeoMESKqcWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0MfS0zNeo-cSntt; ALF=1731219094; _T_WM=08b7c64ab86cf836aa86319b8caaaa7b; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D5088715557045605%26luicode%3D20000061%26lfid%3D5088715557045605%26uicode%3D20000061%26fid%3D5088715557045605; XSRF-TOKEN=5385ab; mweibo_short_token=45a345b9ae",
# "referer": "https://m.weibo.cn/detail/5088715557045605",
# "sec-fetch-dest": "empty",
# "sec-fetch-mode": "cors",
# "sec-fetch-site": "same-origin",
# "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
#     }
#
# data = {
#     "content": "ybybyyb",
#     "mid": '5088715557045605',
#     "st": '8b32e8'
# }
# result = requests.post(url = "https://m.weibo.cn/api/comments/create",headers = headers, data = data)
# print(result.content)




import requests

headers = {
"cookie": "SCF=AnlzcgfYchJBcs0QLAe-CmaWwUwK51wNMj1b2FiheAn0ZMzgP8TWzipcw6jGD0K6loWmpHAvXidk6aKtCqekfIE.; SUB=_2A25KDLHFDeRhGeFJ7lUT9yzJzTqIHXVpYEsNrDV6PUJbktAGLUH4kW1Nf4TyLSJeRpI6Bbwn-5Zq1qQp8FfwkXKV; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFcD0Zxavx0JMl70SskRya65NHD95QNS0-NeoMESKqcWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0MfS0zNeo-cSntt; ALF=1731219094; _T_WM=08b7c64ab86cf836aa86319b8caaaa7b; WEIBOCN_FROM=1110006030; MLOGIN=1; XSRF-TOKEN=5385ab; M_WEIBOCN_PARAMS=oid%3D5088715557045605%26lfid%3D5088715557045605%26luicode%3D20000174; mweibo_short_token=a7d403d66a",
"referer": "https://m.weibo.cn/compose/",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
    }

data = {
    "content": "试试",
    "st": '5385ab'
}
result = requests.post(url = "https://m.weibo.cn/api/statuses/update",headers = headers, data = data)
print(result.content)
