# -----------------------------------------------------------------------------
# The following 12 functions are stubbed for you. You must pass all of our
# test cases for these functions as part of the core. To run your functions
# with our test cases, run the file called runTests.py, which can be found in
# the warmup/ directory.

D = {'Oregon' : 'OR', 'Florida' : 'FL' , 'California' : 'CA' , 'New York' : 'NY' , 'Michigan' : 'MI'}

def returnDictionary(D):
	return D


print returnDictionary(D)

def keyInDict(D,K):
	if K in D:
		return True

print keyInDict(D, 'New York')

D['K'] = 'New York'


def returnKeyVal(D,K):
	return D[K]


def setKeyVal(D, K, V):
    """
    Requires: D is a dictionary
    Modifies: D
    Effects:  Sets the value associated with the key K in the dictionary D
              to be the value V. Returns the dictionary D.
    """
    D['K'] = 'V'
    return D

def setKeyValList(D, K, V1, V2, V3, V4):
    """
    Requires: D is a dictionary
    Modifies: D
    Effects:  Sets the value associated with the key K, which is a key in
              the input dictionary D, to be a list composed of V1 through
              V4, in that order. Returns the dictionary D.
    """

    D['K'] = (V1, V2, V3, V4)
    return D


def getColor(favoriteColors, name):
    """
    Requires: favoriteColors is a dictionary and name is a key in
              favoriteColors
    Modifies: Nothing
    Effects:  Returns the first element in the list associated with the
              key "name" in the input dictionary favoriteColors.
    """
    favoriteColors = {'name' : 'value'}
    return favoriteColors['name']

def asciiAssociate():
    """
    Requires: Nothing
    Modifies: Nothing
    Effects:  Makes a new dictionary, called asciiDict, whose keys are
              the lowercase characters from a to z, and whose values are
              the associated ascii values from 97 to 122. Returns the
              dictionary asciiDict.
    """
    asciiDict = {'a': 97,
                 'b': 98,
                 'c': 99,
                 'd': 100,
                 'e': 101,
                 'f': 102,
                 'g': 103,
                 'h': 104,
                 'i': 105,
                 'j': 106,
                 'k': 107,
                 'l': 108,
                 'm': 109,
                 'n': 110,
                 'o': 111,
                 'p': 112,
                 'q': 113,
                 'r': 114,
                 's': 115,
                 't': 116,
                 'u': 117,
                 'v': 118,
                 'w': 119,
                 'x': 120,
                 'y': 121,
                 'z': 122        
    }
    return asciiDict
    

def translate(vocab, word, language):
    """
    Requires: vocab is a 2-dimensional dictionary, word is a key in vocab,
              and language is a key in the dictionary that word maps to
    Modifies: Nothing
    Effects:  The input dictionary, vocab, could look something like this:
              { "hello": { "Spanish" : "hola", "French": "bonjour" } }
              Given the input dictionary, this function returns the
              value associated with the input word and language.
    """
              
    return vocab[word][language]

def nestedDictionary():
    """
    Requires: Nothing
    Modifies: Nothing
    Effects:  Creates a new dictionary, D, where its keys are the
              lowercase characters from a to z, and each key has a value
              of an empty dictionary. Returns the new dictionary D.
    """
    i=0
    D = {}
    for key in range(26):
        D[key] = chr(97+key)
    D = dict((v,k) for k,v in D.iteritems())
    for key, value in D.items():
        D[key] = {}
    return D

def nestedDictionary3D(L1, L2):
    """
    Requires: L1 and L2 are lists
    Modifies: Nothing
    Effects:  Creates a 3D dictionary, D, with keys of each item of list L1.
              The value for each key in D is a dictionary, which
              has keys of each item of list L2 and corresponding
              values of empty dictionaries. Returns the new dictionary D.
    """
    temp = {}
    temp = dict.fromkeys(L2,"")
    D = dict.fromkeys(L1, temp)

    
    return

def valueFrom3D(D, K1, K2, K3):
    """
    Requires: D is a 3D dictionary, K1 is a key in D, K2 is a key in the
              dictionary that K1 maps to, and K3 is a key in the dictionary
              that K2 maps to
    Modifies: Nothing
    Effects:  Given the 3D input dictionary D, returns the value associated
              with the innermost dictionary accessed using keys K1, K2, and K3,
              in that order.
    """
    
    return D[K1][K2][K3]


def keysIn2D(D, L1, L2):
    """
    Requires: D is a 2D dictionary, L1 is a list, and L2 is a list
    Modifies: Nothing
    Effects:  Given a 2D input dictionary D, returns True if and only
              if the last item of list L1 is a key in D, and that key
              is associated with a dictionary that contains the last
              item of list L2 as a key.
    """
    # Last item of L1: L1[len(L1)-1]
    if L1[len(L1)-1] in D:
        if L2[len(L2)-1] in D[L1[len(L1)-1]]:
            return True
        else:
            return False
    else:
        return False





# -----------------------------------------------------------------------------
# Example tests for your own benefit. Write as many test cases as you need!

if __name__ == '__main__':
    D = { 'question' : 'answer' , 'hello': 'goodbye', 'hot' : 'cold' }

    # This should print True if Function 3 is implemented correctly
    print 'goodbye' == returnKeyVal(D, 'hello')


