import requests 
import json

#shuffling a new deck
shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(shuffle_url)

#parse the JSON response
data = response.json()

#identify each new deck
deck_id = data['deck_id']

print("Deck ID:", deck_id)