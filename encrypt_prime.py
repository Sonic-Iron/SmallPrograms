import math

def getaprime():
    while True:
        number = 1000
        notaprime = False
        gotaprime = False
        number = number + 1
        for a in range(1,number):
            if (number % a == 0) and (a != 1):
                break
        if notaprime == False:
            if number > 1000:
                prime = number
                gotaprime = True
        if gotaprime == True:
            break
        return(prime)

def encrypt():
    gotaprime = False
    normal_text = input("Enter your normal text here")
    print(normal_text)
    prime1 = getaprime()
    prime2 = getaprime()

    print(prime1, prime2)
    
encrypt()
