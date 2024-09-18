#dictionary contianing alphabits, number and symbols as key and morse code as value
morse_code_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
    'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--', '/': '-..-.', 
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', ' ': '#', '#': " "
}




def encryption(messege):
    '''
    encrypt user messege into morse code
    >>> encryption("hi how are you")
    .... .. # .... --- .-- # .- .-. . # -.-- --- ..-
    '''

    output = []    
    
    for char_eny in messege:
        try:
            output.append(morse_code_dict[char_eny])
        
        except KeyError:
            return f"{char_eny} is not a valid input charecter"
    
    
    output = ' '.join(output)
    return output




# something wrong
def decryption(messege):
    '''
    encrypt user messege into morse code
    >>> encryption("hi how are you")
    .... .. # .... --- .-- # .- .-. . # -.-- --- ..-
    '''

    output = []

    for char_dec in messege.split(): 
        try:
            output.append(list(morse_code_dict.keys())[list(morse_code_dict.values()).index(char_dec)])
        except ValueError:
            return f"{char_dec} is not a valed input charecter"

    output = ''.join(output)
    return output



#taking messege from the user that has to be encode or decode
print("if encoded messege is enter then words are seperated by #",
      "please enter your messege here: ",
      sep = '\n', end = ' ')
mes = input()




#if error messege not recive then procede with encryption/decryption
print("if you want to encrypt your messege please enter 'en'",
    "if you want to decrypt your messege please enter 'de'",
    "your response: ",
    sep="\n", end=' ')
en_de = input().lower()

#encrypt messege
if en_de == 'en': #main if block
    print(encryption(mes))

#decrypt messege
elif en_de == 'de':
    print(decryption(mes))

else:
    print("please enter a valied reponse")

