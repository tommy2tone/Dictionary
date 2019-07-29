import json
from difflib import get_close_matches

# Load json test data
data = json.load(open("data.json"))

# Request word from user
word = input('Please enter a word. ')

# Test conditions
if word in data:
    print(data[word])
elif len(get_close_matches(word, data, cutoff=0.8)) > 0:
    closet_match = get_close_matches(word, data)[0]
    print(f'Did you mean {closet_match}?')
else:
    print('The word entered does not exist.  Please try again.')

