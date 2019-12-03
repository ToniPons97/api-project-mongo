import requests


params = {"userName" : "ubuntu"}
res = requests.post("http://localhost:8080/user/create", data=params).text


params = {"idUser" : [2, 5, 7]}

res = requests.post("http://localhost:8080/chat/create", data=params).text

print(res)
