import requests
import json
import numpy as np

Today = 20230601
url = 'http://apis.data.go.kr/1160100/service/GetStocDiviInfoService/getDiviInfo'
Decoding_key = 'BQmxl6GE14imlHZHdA5c5Ho2h1J0tj/AcdNx5bFXmFWpguE4LoBN66xRb9naWkmoehRm7Pvu04mCXMu1FeW9bA=='

init_params = {'serviceKey' : Decoding_key,
          'pageNo' : '1',
          'numOfRows' : '1',
          'resultType' : 'json',
          '기준일자' : Today}

response = requests.get(url, params=init_params)
temp_db_data = response.text
temp_json = json.loads(temp_db_data)

max_count = temp_json['response']['body']['totalCount']
# max_count = 10000
page_count = 1
real_num = 0

json_total = []

while not max_count <= 0:

    params = {'serviceKey': Decoding_key,
                   'pageNo': str(page_count),
                   'numOfRows': '9999',
                   'resultType': 'json',
                   '기준일자': Today}

    response = requests.get(url, params=params)
    db_data = response.text
    json_api = json.loads(db_data)

    for value in json_api['response']['body']['items']['item']:
        if float(value['stckGenrDvdnAmt']) > 1: # and value['cashDvdnPayDt'] != ''
            json_total.append([value['stckIssuCmpyNm'], value['dvdnBasDt'], value['stckGenrDvdnAmt']])
            real_num += 1
        else:
            pass
        max_count -= 1
    print("now_page", page_count)
    print("Left count", max_count)
    page_count += 1

print('filtering_num : ', real_num)

np.save('meta_data', np.array(json_total))