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



#drawing 5 cards of the deck_id
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response = requests.get(draw_url)
draw_data = response.json()
cards = draw_data["cards"]

#include value and suit
print("Your cards:")
for card in cards:
    print(f"{card['value']} of {card['suit']}")