import sys
import random

""" This sets up the allowed dictionary """
allowed_chars = {
    0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9",
    10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f", 16:"g", 17:"h", 18:"i", 19:"j", 20:"k", 21:"l", 22:"m", 23:"n", 24:"o", 25:"p", 26:"q", 27:"r", 28:"s", 29:"t", 30:"u", 31:"v", 32:"w", 33:"x", 34:"y", 35:"z",
    36:"A", 37:"B", 38:"C", 39:"D", 40:"E", 41:"F", 42:"G", 43:"H", 44:"I", 45:"J", 46:"K", 47:"L", 48:"M", 49:"N", 50:"O", 51:"P", 52:"Q", 53:"R", 54:"S", 55:"T", 56:"U", 57:"V", 58:"W", 59:"X", 60:"Y", 61:"Z",
    62:" ", 63:"."
}

""" This sets up the rotor seeds """
rotorSeed1 = 23061912 # the Turing rotor
rotorSeed2 = 22121905 # the Flowers rotor
rotorSeed3 = 16081905 # the Rejewski rotor
reflectorSeed1 = 30011974 # the Carey reflector
reflectorSeed2 = 99041975 # the Codling reflector

def validate_input(inputStr):
    """
    This function validates the input against a list of allowed characters
    and returns a boolean response.

    test this by sending:
    print validate_input("i am at number 471")
    """
    failure = 0
    for elem in inputStr:
        if elem not in allowed_chars.values():
            return(False)
    return(True)
    # test for this function:
    # print validate_input("I am at number 471")

def create_rotor(randSeed):
    """
    This function returns a tuple of allowed characters,
    randomly distributed using the seed provided as an argument.
    """
    random.seed(randSeed) # make sure the rotor setup can be reproduced
    res = []
    ret = {}
    counter = 0
    while len(res) < len(allowed_chars): # create a list with randomised integers
        x = random.randint(0,len(allowed_chars)-1)
        if x not in res: # only add to the list if the value isn't already there
            res.append(x)
    for i in res: # for all of the 64 integrs, replace them with the allowed characters
        ret[allowed_chars[counter]] = allowed_chars[res[i]]
        print(allowed_chars[counter] + " --- " + allowed_chars[res[i]])
        print(ret)
        counter += 1 # this needs to return pairs where the key is in the order of the allowed_chars
    return ret

def create_reflector(randSeed):
    """
    This function returns a reflector with key pairs from the
    allowed_chars list.  If 'i'='Z' then 'Z'='i'
    """
    # first create a rotor
    seedRotor = create_rotor(randSeed)
    # then fold the rotor up in half, making new key value pairs for each value pair
    return randSeed


print("-------------------------")
print("- Python Enigma - Pygma -")
print("-------------------------")
print("")

print(create_rotor(rotorSeed1))
print(create_rotor(rotorSeed2))
print(create_rotor(rotorSeed3))
print("---")
print(create_reflector(reflectorSeed1))
