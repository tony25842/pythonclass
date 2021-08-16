import requests
 
 
price = "8000"
 
headers = {
    "Authorization": "Bearer " + "diKSuFesH6OYmvxmP0Hx2qf0wo5HvhA7hldJw1U5Y4q",
    "Content-Type": "application/x-www-form-urlencoded"
}

params = {"message": "Python基礎班 已降價至" + price + "元"}

r = requests.post("https://notify-api.line.me/api/notify",
                    headers=headers, params=params)
print(r.status_code)  #200