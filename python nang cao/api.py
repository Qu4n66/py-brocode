import requests

base_url = "https://pokeapi.co/api/v2/"

def get_poke(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        print('Data retrieved!')
        poke_data = response.json()
        return poke_data
    else:
        print(f'Fail to retrieve data {response.status_code} ')

# 
pokemon_name = input('Enter Your pokemon name:')
poke_inf = get_poke(pokemon_name)

if poke_inf:
    print(f"{poke_inf['name']}")
    print(f"{poke_inf['id']}")
    print(f"{poke_inf['height']}")


