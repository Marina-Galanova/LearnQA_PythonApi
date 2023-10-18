import requests

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(f"Ответ для http-запроса без параметра method - {response.text}. Статус-код {response.status_code}")

method = {"method": "HEAD"}
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
print(f"Ответ для http-запроса не из списка - {response.text}. Статус-код {response.status_code}")

method1 = {"method": "PUT"}
response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method1)
print(f"Ответ для правильного значения method - {response.text}. Статус-код {response.status_code}")

# цикл проверяющий все возможные сочетания реальных типов запросов
methods = [{"method": "POST"}, {"method": "GET"}, {"method": "PUT"}, {"method": "DELETE"}]

for i in methods:
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
    print(response.text + f" - Ответ для параметра POST и типа запроса {i['method']}")
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=i)
    print(response.text + f" - Ответ для параметра GET и типа запроса {i['method']}")
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
    print(response.text + f" - Ответ для параметра PUT и типа запроса {i['method']}")
    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=i)
    print(response.text + f" - Ответ для параметра DELETE и типа запроса {i['method']}")