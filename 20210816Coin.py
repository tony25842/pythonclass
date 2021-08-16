import requests
import json

headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
url = "https://api.coin360.com/coin/latest?coin=BTC&convert=usdt"
result = requests.get(url, headers=headers)
tmpData = json.loads(result.text)
price = tmpData['BTC']['quotes']['USDT']['price']
params = {"message": "BTC Price : " + str(price) + "元"}
headers = {
    "Authorization": "Bearer " + "diKSuFesH6OYmvxmP0Hx2qf0wo5HvhA7hldJw1U5Y4q",
    "Content-Type": "application/x-www-form-urlencoded"
}
r = requests.post("https://notify-api.line.me/api/notify",
                    headers=headers, params=params)
print(r.status_code)  #200
