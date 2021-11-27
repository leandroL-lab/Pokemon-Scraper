import json
import requests
from bs4 import BeautifulSoup as bs

url = 'https://pokemondb.net/pokedex/all'

page_response = requests.get(url, timeout=5)

page_content = bs(page_response.content, 'html.parser')

pokemonRows = page_content.find_all('tr')
pokemonDict = {}

for row in pokemonRows[1:]:
    
    statsHTML = row.find_all('td')[4:]
    statsArray = [data.contents[0] for data in statsHTML]
    
    typesHTML = row.find_all('a', attrs={'class':'type-icon'}) 
    typesArray = [data.contents[0] for data in typesHTML]
    
    name = row.find('a', attrs = {'class':'ent-name'}).text
    
    megaHTML = row.find('small',attrs={'class':'text-muted'})
    if megaHTML:
        name = megaHTML.contents[0]
    
    pokemonDict[name] = {
        'type1': typesArray[0],
        'hp': statsArray[0],
        'attack': statsArray[1],
        'defense': statsArray[2],
        'spattack': statsArray[3],
        'spdefense': statsArray[4],
        'speed': statsArray[5]
        
        
    }
    if len(typesArray)>1:
        pokemonDict[name]["type2"] = typesArray[1]  
        
with open('pokemon.json','w') as outfile:
    json.dump(pokemonDict,outfile)