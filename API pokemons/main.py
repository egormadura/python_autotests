"""
Создание покемона 
"""

import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {
    'Content-Type': 'application/json',
    "trainer_token": "bba11228962d631b95fa30ca067860f2"
    }

body1 = {
    "name": "Pikachushkaaa",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

response = requests.post(url=f'{URL}/pokemons', json=body1, headers=HEADER, timeout=5)
print(response)


"""
Смена имени покемона 
"""

body2 = {
    "pokemon_id": "29672",
    "name": "Garfield",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
response = requests.put(url=f'{URL}/pokemons', json=body2, headers=HEADER, timeout=5)
print(response)

"""
Поймать покемона в покебол
"""

body3 = {
    "pokemon_id": "29672",
}
response = requests.put(url=f'{URL}/trainers/add_pokeball', json=body3, headers=HEADER, timeout=5)
print(response)
