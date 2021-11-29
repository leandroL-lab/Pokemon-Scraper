import os
import requests
from bs4 import BeautifulSoup as bs

url = 'https://pokemondb.net/sprites'

def beautifulRequests(url):
    try:
        page_response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException as e:
        print(e)

    return bs(page_response.content, 'html.parser')

page_content = beautifulRequests(url)

pokemonLinks = page_content.find_all('a',attrs={'class':'infocard'})

for link in pokemonLinks:
    
    pokemonName = link['href'].split('/')[-1]
    
    # if pokemonName == 'chespin':
    #     #break on 5th generation because it's the last one with a 2D sprite
    #     break
    
    pokemonDetailUrl = f'{url}/{pokemonName}'
        
    page_content_pokemon = beautifulRequests(pokemonDetailUrl)
    
    pokemonSprites = page_content_pokemon.find_all('span',attrs={'class':'img-sprite-v11'})
    
    
    if not os.path.exists('pokemonImages'):
        os.makedirs('pokemonImages')
    
    for sprite in pokemonSprites:
        
        srcString = sprite['data-src']
        
        print(srcString)
        
        type = srcString.split('/')[-2]
        
        if type == 'shiny':
            os.system(f'wget {srcString} -O pokemonImages/{pokemonName}-shiny.png')  
        elif type == 'normal':
            os.system(f'wget {srcString} -O pokemonImages/{pokemonName}.png')
        elif type == 'back-normal':
            os.system(f'wget {srcString} -O pokemonImages/{pokemonName}-back.png')
        elif type == 'back-shiny':
            os.system(f'wget {srcString} -O pokemonImages/{pokemonName}-back-shiny.png')
