import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}

def test_get_trainers_200():
    """
    TEK-1 . Get response is 200
    """
    response = requests.get(url=f'{URL}/trainers', headers=HEADER, timeout=10)
    assert response.status_code == 200, 'Unexpected status code'
    


def test_get_trainers_by_id_3657():
    """
    TEK-2 . ID trainers=3657
    """

    response = requests.get(url=f'{URL}/trainers', headers=HEADER, params={'trainer_id': 3657}, timeout=10)
    assert response.json()['trainer_name'] == 'Арсен' , ''

    