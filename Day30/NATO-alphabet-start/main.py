import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
import pandas as pd
data_df = pd.read_csv('Day26/NATO-alphabet-start/nato_phonetic_alphabet.csv')
data_dict = {row.letter:row.code for index,row in data_df.iterrows()}
# print(data_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

is_on=True
while is_on:
    user_input = input('Enter a word: ').upper()
    try: 
        list_of_words = [data_dict[letter] for letter in user_input]
    except KeyError:
        print('Sorry, only letters in alphabets please.')
    else:
        print(list_of_words)
        is_on=False