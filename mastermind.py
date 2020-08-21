#For generating random code

import random
def gen_code():
    set_code=[]
    for i in range(4):
        set_code.append(random.randint(0,9))
    return set_code

#For giving input code

def input_code():
    code=input("Enter the code")
    return code

#Playing mastermind
def Easy():
    i=0
    while i<20:
        result=""
        inputcode=[int(c) for c in input_code()]
        if len(inputcode)!=4:
            print("Enter 4 digit code only")
        if inputcode==gencode:
            print("Your guess is right",gencode)
            break
        for element in inputcode:
            if element in gencode:
                if inputcode.index(element)==gencode.index(element):
                    result.append("R")
                else:
                    result.append("Y")
            else:
                result.append("N")
        print(result)
        i=i+1
    else:
        print("You ran out of tries",gencode)
def Medium():
    i=0
    while i<10:
        result=""
        inputcode=[int(c) for c in input_code()]
        if len(inputcode)!=4:
            print("Enter 4 digit code only")
        if inputcode==gencode:
            print("Your guess is right",gencode)
            break
        for element in inputcode:
            if element in gencode:
                if inputcode.index(element)==gencode.index(element):
                    result.append("R")
                else:
                    result.append("Y")
            else:
                result.append("N")
        print(result)
        i=i+1
    else:
        print("You ran out of tries",gencode)
def Hard():
    i=0
    while i<5:
        result=""
        inputcode=[int(c) for c in input_code()]
        if len(inputcode)!=4:
            print("Enter 4 digit code only")
        if inputcode==gencode:
            print("Your guess is right",gencode)
            break
        for element in inputcode:
            if element in gencode:
                if inputcode.index(element)==gencode.index(element):
                    result.append("R")
                else:
                    result.append("Y")
            else:
                result.append("N")
        print(result)
        i=i+1
    else:
        print("You ran out of tries",gencode)
def default():
    print("Invalid option")


gencode=gen_code()
print("Select your level")
print("1.Easy\n2.Medium\n3.Hard")
n=int(input())
if n==1:
    Easy()
elif n==2:
    Medium()
elif n==3:
    Hard()
else:
    default()
