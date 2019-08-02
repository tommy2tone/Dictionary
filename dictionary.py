import json
from difflib import get_close_matches

# Load json test data
data = json.load(open("data.json"))

# Request word from user
word = input('Please enter a word: ')

# Test conditions


def lookup(word):
    if word in data:
        print(data[word])
    elif len(get_close_matches(word, data, cutoff=0.8)) > 0:
        closet_match = get_close_matches(word, data)[0]

    # Ask user if they meant the closet match
        choice = input(f'Did you mean {closet_match}?  Press Y for Yes or N for No: ')
        if choice.lower() == 'y':
            print(data[closet_match])
        else:
            word = input('Please enter a word or press Q to quit: ')
            if word.lower() != 'q':
                lookup(word)

    else:
        word = input('The word entered does not exist.  Please try again or Press Q to quit.')
        if word.lower() != 'q':
            lookup(word)



lookup(word)




