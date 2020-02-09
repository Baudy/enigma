import sys
import random

""" Set up the dictionary """
new_allowed_chars = {
    0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9",
    10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f", 16:"g", 17:"h", 18:"i", 19:"j", 20:"k", 21:"l", 22:"m", 23:"n", 24:"o", 25:"p", 26:"q", 27:"r", 28:"s", 29:"t", 30:"u", 31:"v", 32:"w", 33:"x", 34:"y", 35:"z",
    36:"A", 37:"B", 38:"C", 39:"D", 40:"E", 41:"F", 42:"G", 43:"H", 44:"I", 45:"J", 46:"K", 47:"L", 48:"M", 49:"N", 50:"O", 51:"P", 52:"Q", 53:"R", 54:"S", 55:"T", 56:"U", 57:"V", 58:"W", 59:"X", 60:"Y", 61:"Z",
    62:" ", 63:"."
}

trad_allowed_chars = {
    0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J", 10:"K", 11:"L", 12:"M", 13:"N", 14:"O", 15:"P", 16:"Q", 17:"R", 18:"S", 19:"T", 20:"U", 21:"V", 22:"W", 23:"X", 24:"Y", 25:"Z"
}

""" Choose between original enigma 26 character rotors, or new 64 character rotors """
allowed_chars = trad_allowed_chars
#allowed_chars = new_allowed_chars

""" Set up the rotor seeds """
rotorSeed1 = 23061912 # the Turing rotor
rotorSeed2 = 22121905 # the Flowers rotor
rotorSeed3 = 16081905 # the Rejewski rotor
reflectorSeed1 = 30011974 # the Carey reflector
reflectorSeed2 = 99041975 # the Codling reflector

""" Initiate the rotor position variables """
r1_pos = 1
r2_pos = 1
r3_pos = 1


def validate_input(inputStr):
    """
    This function validates the input against a list of allowed characters
    and returns a boolean response.
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
    random.seed(randSeed) # this ensures the rotor setup can be reproduced
    res = [] # a temporary list holding a randomised list of integers
    ret = () # an empty tuple which we'll populate with the contents of the res list at the end
    while len(res) < len(allowed_chars): # create a list with randomised integers
        x = allowed_chars.get(random.randint(0,len(allowed_chars)-1))
        if x not in res: # only add to the list if the value isn't already there
            res.append(x)
    ret = tuple(res) # flip the list res into a tuple called ret
    return ret

def create_notch(randSeed):
    random.seed(randSeed)
    x = allowed_chars.get(random.randint(0,len(allowed_chars)-1))
    return find_key(allowed_chars, x)


def create_reflector(randSeed):
    """
    This function returns a reflector with key pairs from the
    allowed_chars list.  If 'i'='Z' then 'Z'='i'
    """
    # first create a rotor
    seedRotor = create_rotor(randSeed)
    res = {} # a disctionary we will populate with reflections
    for x in seedRotor:
        if x not in res.keys():
            if seedRotor.index(x) < len(seedRotor)/2:
                res[x] = seedRotor[int(seedRotor.index(x) + len(seedRotor)/2)]
                res[seedRotor[int(seedRotor.index(x) + len(seedRotor)/2)]] = x
    return res


def find_key(input_dict, value):
    """
    This function returns the key from the input_dict
    which matches the provided value
    """
    # return input_dict.keys()[input_dict.values().index(value)]  # python 2
    return list(input_dict.keys())[list(input_dict.values()).index(value)]

def encode(char):
    n = find_key(allowed_chars, char)
    a = r1[n]
    n = r2.index(a)
    a = r3[n]
    a = reflector.get(a)
    n = r3.index(a)
    a = r2[n]
    n = r1.index(a)
    a = allowed_chars[n]
    return a


print("------------------------------")
print("- Python Enigma - Pythonigma -")
print("------------------------------")
print(sys.version)
print("")

r1 = create_rotor(rotorSeed1)
r2 = create_rotor(rotorSeed2)
r3 = create_rotor(rotorSeed3)
reflector = create_reflector(reflectorSeed1)

print("Rotor 1: " + str(r1))
print("Rotor 2: " + str(r2))
print("Rotor 3: " + str(r3))

print("Rotor 1 notch position: " + str(create_notch(12061995)))
print("Rotor 2 notch position: " + str(create_notch(22061998)))
print("Rotor 3 notch position: " + str(create_notch(15022008)))

print("---")
print(encode("T"),end="")
print(encode("I"),end="")
print(encode("M"))
print("---")
print(encode("Q"),end="")
print(encode("D"),end="")
print(encode("V"))
print("---")
