import requests

class TestApiCookie:
    def test_chek_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")

        assert response.status_code == 200, f"Некоррекный статус код"

        expected_response_cookie = {'HomeWork': 'hw_value'}
        actual_response_cookie = dict(response.cookies)

        assert expected_response_cookie == actual_response_cookie, f"Некорректный куки"