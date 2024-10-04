import requests





for i in range(4):
    data = {'name': f'bmw{i}', 'brands_car': 'e34  ', 'info': 'motor and engine'}

    response = requests.post('http://127.0.0.1:8000/ini/', json=data)
    if response.status_code == 201:
        print('User created successfully')
        user = response.json()

        print(user)
    else:
        print(f'Failed to create user. Status code: {response.status_code}')
        print(response.text)







