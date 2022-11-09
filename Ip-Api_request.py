import socket
import requests

ip = input("Введите IP-адрес")

request = requests.get(
    f"http://ip-api.com/json/{ip}"
)

requestJson = request.json()
if (requestJson['status'] == 'fail') :
    print("Таĸого IP не существует")
else : print(requestJson['country'])

