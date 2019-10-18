import requests
from .models import RandomUsers


def _get_location(loc):
    return f'{loc["country"]} {loc["state"]} {loc["city"]} {loc["street"]["name"]} {loc["street"]["number"]}'


def save_users(n_users):
    url = 'https://randomuser.me/api/'
    users_count = 0
    for _ in range(n_users):
        if users_count >= 5:
            break

        resp = requests.get(url=url)
        if resp.status_code == 200:
            info = resp.json()['results'][0]
            if any(char in info['name']['first'] + info['name']['last'] for char in ('r', 'R')):  # Нет ли в имени буквы 'R'
                users_count += 1
                RandomUsers.objects.create(
                    first_name = info['name']['first'],
                    last_name = info['name']['last'],
                    gender = info['gender'],
                    location = _get_location(info['location']),
                    email = info['email']
                )
        else:
            return {'success': False, 'reasons': resp.text}
    return {'success': True, 'count': users_count}


def get_users():
    return RandomUsers.objects.all().order_by('first_name')
