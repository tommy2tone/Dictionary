import json
from difflib import get_close_matches

# Load json test data
data = json.load(open("data.json"))

# Request word from user
word = input('Please enter a word: ')


# Test conditions


def lookup(word):
    word = word.lower()
    if word in data:
        actual_word = word
        return [actual_word, data[word]]
    elif len(get_close_matches(word, data, cutoff=0.8)) > 0:
        closet_match = get_close_matches(word, data)[0]

    # Ask user if they meant the closet match
        choice = input(f'Did you mean {closet_match}?  Press Y for Yes or N for No: ')
        if choice.lower() == 'y':
            actual_word = closet_match
            return [actual_word, data[closet_match]]
        else:
            new_word = input('Please enter a word or press Q to quit: ')
            if new_word.lower() != 'q':
                return lookup(new_word)

    else:
        new_word = input('The word entered does not exist.  Please try again or Press Q to quit: ')
        if new_word.lower() != 'q':
            return lookup(new_word)


output = lookup(word)

# if statement and for loop to display the word being defined, number of definitions,
# and the definitions

if type(output) == list:
    word = output[0].capitalize()
    num_defs = len(output)
    count = 1
    print(f'{word} has {num_defs} definitions:')
    for item in output[1]:
        print(f'{count}. {item}')
        count += 1




