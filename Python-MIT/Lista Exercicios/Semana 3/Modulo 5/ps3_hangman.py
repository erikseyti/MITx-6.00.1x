# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)


import random
WORDLIST_FILENAME = "words.txt"
secretWord = ""
lettersGuessed = []
mistakesMade = 0
availableLetters = []

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    palavraExtenso = list(secretWord)
    contador = 0
    tamanhoPalavra = len(secretWord)
   # print(palavraExtenso)
    for l in palavraExtenso:
        if l[0] in lettersGuessed:
            contador = contador + 1
   # print("Valor do Contado: "+str(contador))
   # print("Tamanho da Palavra: " + str(tamanhoPalavra))
    if contador == tamanhoPalavra:
        return True
    else:
        return False
    
    # FILL IN YOUR CODE HERE...



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    palavraExtenso = list(secretWord)
    palavraDescoberta = []
    for l in palavraExtenso:
        if l[0] in lettersGuessed:
            palavraDescoberta.extend(l[0])
        else:
            palavraDescoberta.extend(["_ "])
    palavraDescobertaString = ''.join(palavraDescoberta)
    return palavraDescobertaString
    
    # FILL IN YOUR CODE HERE...



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    
   # alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    import string
    alfabeto = string.ascii_lowercase
    alfabetoDisponivel =[]
    for l in alfabeto:
        if l[0] not in lettersGuessed:
            alfabetoDisponivel.extend(l[0])
    alfabetoDisponivelString = ''.join(alfabetoDisponivel)
    return alfabetoDisponivelString

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    contagemPalavra =len(secretWord)
    palavraDescoberta = False
    palavraOculta = ""
    lettersGuessed = []
    guess = ""
    mistakesMade = 8
    print("Welcome to the game, Hangman!")
    print(secretWord)
    print("I am Thinking of a word that is "+ str(contagemPalavra) + " letters long.")
    print("-------------")
    while mistakesMade > 0:
        print("You Have "+ str(mistakesMade) +" Guesses Left.")
        letrasDisponiveis = getAvailableLetters(lettersGuessed) 
        print("Available Letters: " + letrasDisponiveis)
        guess = input("Please guess a letter: ")
        guessInLowerCase = guess.lower()
        print(guessInLowerCase)
        lettersGuessed.append(guessInLowerCase)
        print(lettersGuessed)
        palavraParcial = getGuessedWord(secretWord, lettersGuessed)
        if palavraOculta != palavraParcial:
            palavraOculta = palavraParcial
            print("Good guess: "+ str(palavraOculta))
            palavraDescoberta = isWordGuessed(secretWord, palavraOculta)
        else:
            print("Oops! That letter is not in my word: " + str(palavraOculta))
            mistakesMade = mistakesMade - 1
        print("------------")
        if palavraDescoberta == True:
            print("Congratulations, You Won")
            return secretWord
    else:
        print("Sorry, you ran out of guesses. The word was: "+ secretWord)
        return secretWord

#print(isWordGuessed("mobiles",["b","m","w","i","o","s","l","p"]))
#print(getGuessedWord("piccolo",["m","c","l","o","s","r","y","z","t"]))
#print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
