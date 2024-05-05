import requests

import json
def get_curency():
    url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'

    source = requests.get(url).text
    jjson = json.loads(source)

    # soup = bs4.BeautifulSoup(source, 'lxml')
    return jjson

#     with open('currency.txt', 'w') as f:
#         for i in range(3):
#             f.write(f'{jjson[i]["Ccy"]} : {jjson[i]["Rate"]}\n')
# o = get_curency()
# cur = {}
# for i in range(3):
#     cur[o[i]['Ccy']] = o[i]['Rate']
# print(cur)
# print(type(cur))