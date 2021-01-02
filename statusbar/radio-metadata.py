#!/bin/python3

from bs4 import BeautifulSoup
import urllib3
import sys
import json
urllib3.disable_warnings()

if len(sys.argv) < 2:
    print('ERROR: please provide player url where I can get the metadata')
    exit(-1)
url = sys.argv[1]

bbc6_url = 'https://www.bbc.co.uk/sounds/player/bbc_6music'
triple_j_url = 'https://music.abcradio.net.au/api/v1/plays/triplej/now.json'
triple_j_unearthed_url = 'https://music.abcradio.net.au/api/v1/plays/unearthed/now.json'
kexp_url = 'https://api.kexp.org/v2/plays/?format=json&limit=1&ordering=-airdate'

http = urllib3.PoolManager()

try:
    radio_response = http.request('GET', url)
except:
    print("no connection to " + url)
    sys.exit(1)

if url == bbc6_url:
    soup = BeautifulSoup(radio_response.data, 'lxml')
    for tag in soup.find_all('div', {'class': 'sc-c-track__artist gel-pica-bold sc-u-truncate'}):
        artist = tag.text
        break

    for tag in soup.find_all('div', {'class': 'sc-c-track__title gs-u-mt-- gel-brevier'}):
        title = tag.text
        break

elif url == triple_j_url or url == triple_j_unearthed_url:
    try:
        artist = json.loads(radio_response.data)['now']['recording']['artists'][0]['name']
        title = json.loads(radio_response.data)['now']['recording']['title']
    except:
        artist = json.loads(radio_response.data)['prev']['recording']['artists'][0]['name']
        title = json.loads(radio_response.data)['prev']['recording']['title']

elif url == kexp_url:
    artist = json.loads(radio_response.data)['results'][0]['artist']
    title = json.loads(radio_response.data)['results'][0]['song']


print(artist + ' - ' + title)
