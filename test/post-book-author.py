import requests

data = {
    "name": "Ариет",
    "books": [{
        "titel":"Привет"
    }]
}
for i in range(123):
    print(i)
    response = requests.post('http://127.0.0.1:8000/in/', json=data)
    print(response.status_code)