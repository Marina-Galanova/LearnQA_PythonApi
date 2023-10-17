import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
history_response = response.history
final_response = response

print(history_response)
print(final_response.url)