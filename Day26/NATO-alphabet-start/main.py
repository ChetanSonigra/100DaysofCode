student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    print(key)
    print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    print(index)
    print(row,row.student)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
import pandas as pd
data_df = pd.read_csv('Day26/NATO-alphabet-start/nato_phonetic_alphabet.csv')
data_dict = {row.letter:row.code for index,row in data_df.iterrows()}
# print(data_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input('Enter a word: ').upper()
list_of_words = [data_dict[letter] for letter in user_input]

print(list_of_words)