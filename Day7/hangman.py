
import random
import hangman_words
import hangman_art
words_list=hangman_words.word_list
hangmans = hangman_art.stages

choosen_word = random.choice(words_list)

lives = 6

blank_letters = ['_' for i in range(len(choosen_word))]
#print(choosen_word)
end_of_game = False
print(hangman_art.logo)
while not end_of_game:
    guess = input('Guess a letter: ').lower()
    
    if guess in blank_letters:
        print(f"you have already guessed letter '{guess}'")

    for i,letter in enumerate(choosen_word):
        if letter == guess:
            blank_letters[i]= guess
            
    if guess not in choosen_word:
        print(f"Your guessed {guess}. Thant's not in a word. You lose a life.")
        lives-=1
        if lives==0:
            print('You Lost!')
            end_of_game=True

    if '_' not in blank_letters:
        print('You Won!')
        end_of_game=True
    print(hangmans[lives])
    print(blank_letters)
    
print(f'Right word was: {choosen_word}')