import requests

class TestApiHeader:
    def test_chek_header(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")

        assert response.status_code == 200, f"Некоррекный статус код"

        response_header = response.headers

        assert "x-secret-homework-header" in response_header, f"Некорректный хедер"