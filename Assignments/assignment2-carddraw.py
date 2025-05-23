import requests 
import json


#SPECIFIC CARDS = "https://deckofcardsapi.com/api/deck/new/shuffle/?cards=AS,2S,3S,4S,5S"
#SHUFFLED DECK = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

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


#Extract card values and suits
values = [card["value"] for card in cards]
suits = [card["suit"] for card in cards]

#map each card value to a number
value_map = {
    "ACE": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "JACK": 11,
    "QUEEN": 12,
    "KING": 13
}
numeric_values = [value_map[v] for v in values]

#Manually count occurrences of each card value
value_counts = {}
for v in values:
    if v in value_counts:
        value_counts[v] += 1
    else:
        value_counts[v] = 1

print("Value counts:", value_counts)


#identify if there is a: pair; triple; four of a kind
has_pair = False
has_triple = False
has_quad = False

for count in value_counts.values():
    if count == 2:
        has_pair = True
    elif count == 3:
        has_triple = True
    elif count == 4:
        has_quad = True

if has_pair:
    print("You have a pair")
if has_triple:
    print("You have a triple")
if has_quad:
    print("You have four of a kind")

#identify if there is a straight
sorted_values = sorted(numeric_values)
is_straight = True
for i in range(len(sorted_values) - 1):
    if sorted_values[i] + 1 != sorted_values[i+1]:
        is_straight = False
        break

if is_straight:
    print("You have a straight")

#identify if there is a flush (same suit)
is_flush = (len(set(suits)) == 1)
if is_flush:
    print("You have a flush")
