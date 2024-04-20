from cipher_art import logo
alphabets = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

def caesar(text,shifts,direction):
    new_text = ''
    
    if direction=='decode':
        shifts *= -1
        
    for i in text:
        if i in alphabets:
            new_text += alphabets[alphabets.index(i)+shifts]
        else:
            new_text += i
            
    print(f"The {direction}d text is {new_text}")


print(logo)
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input('Type your text:\n').lower()
    shifts = int(input('Type the shift number:\n'))%26        

    caesar(text,shifts,direction)
    try_again = input("Type 'yes' to continue again. Type 'no' to exit.\n").lower()
    if try_again=='no':
        should_continue=False