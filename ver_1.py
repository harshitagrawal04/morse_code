#dictionary contianing alphabits, number and symbols as key and morse code as value
morse_code_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
    'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--', '/': '-..-.', 
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', ' ': '#', '#': " "
}


def val_int(messege):
    '''
    check if the input contains valid charectes or not
    >>> a
    valid charectes
    >>> @
    invalid charectes
    '''

    # for encoding messege checking if input is valid or not
    for char in messege:
        if (char in morse_code_dict.keys()) == False: 
            return f"{char} is not a invalid charecter"
        
        else:
            return True
    

    # for decoding messege checking if input is valid or not


def encryption(messege):
    '''
    encrypt user messege into morse code
    if messege is already in encrypted form then ask to encrypt or decrypt or exit
        if encrypt then proced to encrypt
        if decrypt then proced to decrypt
        else exit the code
    >>> encryption("hi how are you")
    .... .. # .... --- .-- # .- .-. . # -.-- --- ..-
    '''

    output = []
    encrypt = 0
    
    '''
    checking if the input is already encoded or not
    if the value of 'a' is zero then is it already encoded
    '''

    #checking if the imput messege is already encrypted or not
    for char in mes:
        if (char != ' ') and (char != '.') and (char != '-') and (char != '#'):
            encrypt+=1
    
    # asking user if he/she wants to still encode, decode or exit
    if encrypt == 0:
        print("messege is already encoded",
                    "if you want to encode enter 'en'",
                    "if you want to decode enter 'de'",
                    "if you want to exit then enter 'ex'",
                    "please enter your reponse: ",
                    sep="\n", end=" ")
        en_de_ex = input().lower()
        if en_de_ex == "en":
            for char in messege:
                output.append(morse_code_dict[char])
        elif en_de_ex == "de":
            return decryption(messege)
        elif en_de_ex == "ex":
            exit
        else:
            print("please enter valid input")
    
    else:
        for char in messege:
            output.append(morse_code_dict[char])
        
    
    '''
    for each charecter in messege it will take the value from the dictionay and append it to the output
    each charecter will act as a key
    '''
    
    # as the output is in list it will convert it to the list
    output = ' '.join(output)
    return output




def decryption(messege):
    '''
    decrypt user messege form the morse code 
    if code is not present in dictionary then give error messege
    >>> decryption('-----')
    ----- is not a valid input
    >>> decryption('.... .. # .... --- .-- # .- .-. . # -.-- --- ..-')
    hi how are you
    '''


    invalid = 0
    output = []


    # checking if invalid input is enter or not
    for i in messege.split('#'):
        for j in i.split():
            if any([True for v in morse_code_dict.values() if v == j]):
                pass
            else:
                invalid +=1
                return f"'{j}' is not a valid input"
                

    # decoding the messege
    if invalid ==0:
        for i in messege.split(): 
            output.append(list(morse_code_dict.keys())[list(morse_code_dict.values()).index(i)])

    output = ''.join(output)
    return output



#taking messege from the user that has to be encode or decode
print("if encoded messege is enter then words are seperated by #",
      "please enter your messege here: ",
      sep = '\n', end = ' ')
mes = input()



# if invalid charecter (not in dic) then print error messege 
if val_int(mes) != True:
    print(val_int(mes))

#if error messege not recive then procede with encryption/decryption
else:
    print("if you want to encrypt your messege please enter 'en'",
        "if you want to decrypt your messege please enter 'de'",
        "your response:",
        sep="\n", end=' ')
    en_de = input().lower()

    #encrypt messege
    if en_de == 'en': #main if block
        print(encryption(mes))

    #decrypt messege
    elif en_de == 'de':
        print(decryption(mes))

    # if invalid en/de input is given
    else:
            print("please enter a valied reponse")


