"""
Создание покемона 
"""

import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}

body1 = {
    "trainer_token": "036fb521ea62690387868324920ba0f2",
    "name": "Pikachushkaaa",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

response = requests.post(url=f'{URL}/pokemons', json=body1, headers=HEADER, timeout=5)
print(response)


"""
Смена имени покемона 
"""

body2 = {
    "pokemon_id": "id_покемона",
    "name": "Garfield",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
response = requests.put(url=f'{URL}/pokemons', json=body2, headers=HEADER, timeout=5)
print(response)

"""
Поймать покемона в покебол
"""

body3 = {
    "pokemon_id": "id_покемона",
}
response = requests.put(url=f'{URL}/trainers/add_pokeball', json=body3, headers=HEADER, timeout=5)
print(response)
