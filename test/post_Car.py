import requests


data = {
    'name': 'bmw',
    'Author': 'bmw man',
    'info': 'who?'
}
for k in range(120):
    print(k)
    response = requests.post(url='http://127.0.0.1:8000/cars/cars/', json=data)
    print(response.status_code)
    print(response.text)