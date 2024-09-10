import string
import random

alphabet=list(string.ascii_letters+string.digits+string.punctuation+" ")

def encrypt(alphabet):
    normal_text = input("Enter text to be encryped")
    e_text = ""
    key = []
    new_key = ""
    e_letter = len(alphabet) + 2
    for letter in normal_text:
        e_letter = random.choice(alphabet)
        e_number = alphabet.index(letter)-alphabet.index(e_letter)
        key.append(e_number)
        e_text += e_letter
    print("The normal text was : ",normal_text)
    print("The encrypted text is : ",e_text)
    for a in range(len(key)):
        new_key += str(key[a])
        new_key += ':'
    new_key = new_key[0:len(new_key)-1]
    key = new_key
    print("The key for this is : ",key)



def decrypt(alphabet):
    e_text = input("What is the encrypted text")
    key = input("What is the key?")
    de_text = ""
    text = ""
    key = key.split(':')
    
    print(key, "KEY\n")
    print(e_text, "ENCRYPTED TEXT\n")
    for a in range(len(e_text)):
        text += alphabet[alphabet.index(e_text[a]) + int(key[a])]
    print("The normal text is ",text)
        
        

de_en = "a"
while de_en != "E" or "D":
    de_en = input("Would you like to decrypt [d] or encrypt [e] text?")
    if de_en == "d":
        decrypt(alphabet)
    elif de_en == "e":
        encrypt(alphabet)
    else:
        print("That is not a valid input, please enter either [d] or [e]")
