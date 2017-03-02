# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    valorPalavra =0
    numeroLetras = len(word)
    palavraExtenso = list(word)
    for l in palavraExtenso:
        x= SCRABBLE_LETTER_VALUES
        if l in x:
            valorPalavra = valorPalavra + x.get(l)
            print(valorPalavra)
    valorPalavra = valorPalavra * numeroLetras
    if numeroLetras == n:
        valorPalavra = valorPalavra+ 50
    #himprint(valorPalavra)
    return valorPalavra



#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

def alternativedisplayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    letrasDisponiveis = ""
    for letter in hand.keys():
        for j in range(hand[letter]):
            letrasDisponiveis = letrasDisponiveis + letter + " "
            #print(letter,end=" ")       # print all on the same line
    #print()                             # print an empty line
    print("Current Hand: " +letrasDisponiveis)
#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    palavraLista = list(word)
    handCopy = hand.copy()
    for h in handCopy:
        if h in palavraLista:
            handCopy[h] -=1
            palavraLista.remove(h)
    for h in handCopy:
        if h in palavraLista:
            handCopy[h] -=1
            palavraLista.remove(h)
    return handCopy


#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.
    
    fazer uma validação se a palavra é uma palvara valida, presente no arquivo word.txt
    verificar se é possivel criar a palavra com as letras presentes na mão
    retorna true se for verdade ambas as condições
    retorna falso de outra forma

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    #fazer uma validação se a palavra é uma palvara valida, presente no arquivo word.txt
    #verificar se é possivel criar a palavra com as letras presentes na mão
    #retorna true se for verdade ambas as condições
    #retorna falso de outra forma
    palavraLista = list(word)
    handCopy = hand.copy()
    listaTemp = palavraLista[:]
    if word in wordList:
        for h in palavraLista:
            if h in handCopy:
                handCopy[h]-=1
                if handCopy[h] >=0:
                    listaTemp.remove(h)
        if listaTemp == []:
            return True
        else:
            return False
    else:
        return False
    
#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    tamanhoMao = []
    handCopy = hand.copy()
    for h in handCopy:
        if handCopy[h] == 1:
            tamanhoMao.append(h)
        elif handCopy[h] == 2:
            tamanhoMao.append(h)
            tamanhoMao.append(h)
        elif handCopy[h] == 3:
            tamanhoMao.append(h)
            tamanhoMao.append(h)
            tamanhoMao.append(h)
        elif handCopy[h] == 4:
            tamanhoMao.append(h)
            tamanhoMao.append(h)
            tamanhoMao.append(h)
            tamanhoMao.append(h)
    return len(tamanhoMao)

    


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    
    # Keep track of the total score
    letrasMao = n
    palavraValida = False
    valorTotal = 0
    valorPalavra = 0
    palavra = ""
    tamanhoMao = calculateHandlen(hand)
    # As long as there are still letters left in the hand:
     
    while palavra != ".":
        #print(letrasMao)
        # Display the hand
        #adicionar a função alternativedisplayHand
        tamanhoMao = calculateHandlen(hand) 
        if tamanhoMao == 0:
            print("")
            print(" Run out of letters. Total score: "+ str(valorTotal)+ " points")
            break
        mostrarMao = alternativedisplayHand(hand)
        #print(tamanhoMao)
       # print(mostrarMao)
        
        # Ask user for input
        palavra = input("Enter word, or a ""."" to indicate that you are finished: ")
        # If the input is a single period:
        for n in palavra:
            if n == " ":
                break

            # End the game (break out of the loop) 
        if n == " ":
            break
        # Otherwise (the input is not a single period):
            # If the word is not valid:
        if palavra == "." or mostrarMao=="":
            print("Goodbye! Total score: "+ str(valorTotal))
            break
        palavraValida = isValidWord(palavra,hand,wordList)
        if palavraValida == False:
                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please try again.")
                print("")
            # Otherwise (the word is valid):
        else:
            valorPalavra = getWordScore(palavra, letrasMao)
            #print(valorPalavra)
            valorTotal = valorTotal + valorPalavra
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            print("'"+str(palavra)+"'"+ " earned "+ str(valorPalavra) + " points. Total: "+ str(valorTotal) +" points")
                # Update the hand 
            hand = updateHand(hand, palavra)
            #print(hand)
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score


#
# Problem #5: Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    variavelMao = ""
    #variavel criada para armazenar o valor anterior da mão jogada
    maoAntiga = {}
    hand = {}
    tamanhoMao = HAND_SIZE
    while variavelMao !="e":
        variavelMao = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if variavelMao == "n":
            #print("nova Mão")
            if hand == {}:
                hand = dealHand(tamanhoMao)
                playHand(hand,wordList,tamanhoMao)
                #print("chamar Função")
            else:
                #print("ero")
                #apagar valor atual da mão Antiga
                maoAntiga.clear()
                #atribuir o valor de hand para mão Antiga
                maoAntiga = hand.copy()
                #provavelmente dar um clear no Hand
                #print(hand)
                #print(maoAntiga)
                hand.clear()
                #atribuir um novo valor para a mão
                #chamar dealHand(HandSize)
                hand = dealHand(tamanhoMao)
                #chamar PlayHand
                playHand(hand,wordList,tamanhoMao)   
        elif variavelMao == "r":
            if hand == {}:
                print("You have not played a hand yet. Please play a new hand first!")
            else:
                #print("pegando mão Antiga")
                #chamar a mão antiga a variavel Play Hand
                #hand.clear()
                #hand = maoAntiga.copy()
                #chamar Play Hand
                maoAntiga.clear()
                maoAntiga = hand.copy()
                playHand(maoAntiga,wordList, tamanhoMao)
        elif variavelMao == "e":
            break
        else:
            print("Invalid command.")

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
x = getWordScore("play", 7)
print(x)
#y = displayHand({'a':1, 'x':2, 'l':3, 'e':1})
#print(y)
#z = dealHand(7)
#print(z)
#y = alternativedisplayHand({'h': 1, 'e': 1, 'k': 1, 'b': 1, 'o': 1, 'g': 1, 'x': 1})
#y = displayHand({'i': 1, 'm': 1, 'u': 1, 'l': 2, 'a': 1, 'q': 1})
#print(y)
#handOrig = {'o': 3, 'u': 3, 'r': 3, 'w': 3, 't': 3, 'i': 3, 'q': 3, 'p': 3, 'y': 3, 'e': 3}
#handCopy = handOrig.copy()
##print(handCopy)
#word = 'typewriter'
#hand2 = updateHand(handCopy, word)
#print(hand2)
#print(wordList)
#
wordList = loadWords()
#s = isValidWord('rapture',{'e': 1, 'p': 2, 't': 1, 'a': 3, 'u': 1, 'r': 1},wordList)
#print(s)

#c = calculateHandlen({'e': 1, 'p': 2, 't': 1, 'a': 3, 'u': 1, 'r': 1})
#print(c)

#p = playHand({'n':1, 'e':1, 't':1, 'a':1, 'r':1, 'i':2}, wordList, 7)

# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
