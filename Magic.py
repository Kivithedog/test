import json

# Open and load the JSON file
with open('./Magic.json', 'r',  encoding='utf-8-sig') as file:
    data = json.load(file)

# Print the loaded data (optional)

#print all cards that have '10E' in printings

for card in data:
    if set in card:
        if set == '10e':
            print(card['name'])

# Print all cards where the card is restricted in the Paupercommander format

