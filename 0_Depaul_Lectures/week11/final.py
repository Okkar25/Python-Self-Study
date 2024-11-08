# final.py
# CSC401


##### sentencesByLength #####

def sentencesByLength( filename ):

    with open(filename) as f:
        contents = f.read()
    contents = contents.replace('\n',' ')
    sentences = contents.split(".")
    d = {}
    for sentence in sentences:
        sentence = sentence.strip()         
        n = len(sentence.split())
        # print( n,sentence )

        if n==0:
            continue
        elif n in d:
            d[n].append(sentence.strip()+".")
        else:
            d[n] = [sentence.strip()+"."]
    return d



##### grid #####

# not actually used!!!
# think i like this version
def grid( rows, cols ):

    grid = ""
    seperator = cols * ('+' + 5*'-') + '+\n'    
    for r in range(rows):
        line = ""
        for c in range(cols):
            line += f"| {r},{c} "

        line += "|\n"
        grid += seperator + line
    return grid + seperator



##### RandomCode #####

import random
class RandomCode():

    def __init__(self,n,letters):
        self.code = "".join( [random.choice(letters) for i in range(n)])

    def __repr__(self):
        return f"RandomCode({repr(self.code)})"

    def getHint(self):
        return len(self.code)*"?"

    def getSecret(self):
        return self.code

    def correctLetters(self,guess):
        return sum([ min(self.code.count(letter), guess.count(letter)) for letter in set(self.code)])

    def correctPositions(self,guess):
        return sum( [self.code[i]==guess[i] for i in range(min(len(self.code),len(guess)))] )

    def correct(self,guess):
        return self.code == guess



##### guessCode #####

def guessCode(n,letters):

    secret = RandomCode(n,letters)
    print(f"Try to guess my secret code: {secret.getHint()} (QUIT to stop)\n")
    guesses=0
    
    while True:
        guess = input('What is your guess?: ')
        guesses+=1
        
        if secret.correct(guess):
            print(f'Congratulations, you got it in {guesses} guesses!')
            break
        elif guess=='QUIT':
            print( f"\nYou gave up after {guesses-1} guesses. \nThe secret code is {secret.getSecret()}.")
            break
        else:
            print(f"Your guess has {secret.correctLetters(guess)} correct letters, {secret.correctPositions(guess)} in the correct position.")
            print()

if __name__=='__main__':
    import doctest
    print( doctest.testfile('finalTEST.py'))







    
    
