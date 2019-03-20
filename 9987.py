import requests
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20140301191716/http://pokemondb.net/pokedex/national'

html = requests.get(url).text
pokemon_list = BeautifulSoup(html, 'html.parser').find_all('span', {
  'class': 'infocard-tall'
})

pokedex = [None]
for pokemon in pokemon_list:
  # number = pokemon.small.string.replace('#', '')
  name = pokemon.find(class_='ent-name').string
  types = [type.string for type in pokemon.findAll(class_='itype')]
  pokedex.append({
    'name': name,
    'types': types
  })

print(pokedex)

# 결과로 출력된 리스트를 다시 pokedex로 저장한다
pokemon = pokedex[int(input())]
print(pokemon['name'])
print(' '.join(pokemon['types']))
