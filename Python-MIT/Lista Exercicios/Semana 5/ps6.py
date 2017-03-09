import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        #pass #delete this line and replace with your code here
        dictionaryShift = {1: "a",2:"b",3: "c",4:"d",5:"e",6:"f",7: "g",8:"h",9: "i",10: "j",11:"k",12:"l"
                            , 13:"m",14:"n",15:"o",16:"p",17:"q",18: "r", 19:"s",20: "t",21: "u",22:"v",23:"w"
                            , 24:"x",25:"y",26:"z",27:"A",28:"B",29:"C",30:"D",31:"E",32:"F",33:"G",34:"H",35:"I"
                            ,36:"J", 37:"K", 38:"L",39:"M",40:"N",41:"O",42:"P",43:"Q",44:"R",45:"S",46:"T"
                            ,47:"U",48:"V",49:"W",50:"X",51:"Y",52:"Z"}
        dicionarioTroca={"a":1,"b":2 ,"c":3 ,"d": 4, "e": 5, "f": 6,"g":7,"h": 8, "i": 9, "j": 10, "k": 11,
                         "l": 12, "m": 13, "n": 14, "o": 15,"p": 16, "q": 17, "r": 18, "s": 19, "t": 20,"u": 21
                         , "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "A": 27, "B": 28, "C": 29, "D": 30, 
                         "E":31,"F": 32, "G": 33,"H": 34,"I": 35, "J": 36,"K": 37, "L": 38, "M": 39,"N": 40
                         ,"O": 41, "P": 42, "Q": 43, "R": 44, "S": 45,"T": 46,"U": 47, "V":48,"W":49, "X": 50
                         , "Y": 51, "Z": 52}                
        listaAtual = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w"
                      ,"x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"
                      ,"U","V","W","X","Y","Z"]                
                          
        #valor referente a cada letra da palavra que será encriptada, alterando por sua vez, para "converter"
        # a letra em numero: a = 1, b= 2; seguindo o dicionario de Troca
        valorLetra = 0
        letraValor = ""
        somaShift = 0
        #lista da primeira conversão; de letras para numeros: a = 1, b = 2; seguindo o dicionario de troca
        listaTrocaValor = []
        #lista da segunda conversão; de numeros para letras
        listaTrocaLetra = []
        
        #dicionarioRelacional ={}


        #mensagem = self.message_text
        #print(mensagem)
        #mensagemExtenso = list(mensagem)
        #print(mensagemExtenso)
        for k in dictionaryShift:
            if k in dicionarioTroca:
                valorLetra= valorLetra + dicionarioTroca[k]
                listaTrocaValor.append(valorLetra)
                valorLetra = 0
            else:
                listaTrocaValor.append(k)
        #print(listaTrocaValor)
                
        for m in listaTrocaValor:
            somaShift = 0
            if m in dictionaryShift:
                if m> 26:
                    somaShift =m + shift
                    if somaShift > 52:
                        somaShift = somaShift - 26
                        letraValor = dictionaryShift[somaShift]
                        listaTrocaLetra.append(letraValor)
                    else:
                        letraValor = dictionaryShift[somaShift]
                        listaTrocaLetra.append(letraValor)   
                else:
                    somaShift =m + shift
                    if somaShift > 26:
                        somaShift = somaShift - 26
                        letraValor = dictionaryShift[somaShift]
                        listaTrocaLetra.append(letraValor)
                    else:
                        letraValor = dictionaryShift[somaShift]
                        listaTrocaLetra.append(letraValor)
#            else:
#                listaTrocaLetra.append(m)
        #print(listaAtual)
        #print(listaTrocaLetra)
        dicionarioCompletoTroca = dict( zip(listaAtual, listaTrocaLetra))
        #print(dicionarioCompletoTroca)    
        return dicionarioCompletoTroca   
                            
                            

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        dictionaryShift = {1: "a",2:"b",3: "c",4:"d",5:"e",6:"f",7: "g",8:"h",9: "i",10: "j",11:"k",12:"l"
                            , 13:"m",14:"n",15:"o",16:"p",17:"q",18: "r", 19:"s",20: "t",21: "u",22:"v",23:"w"
                            , 24:"x",25:"y",26:"z",27:"A",28:"B",29:"C",30:"D",31:"E",32:"F",33:"G",34:"H",35:"I"
                            ,36:"J", 37:"K", 38:"L",39:"M",40:"N",41:"O",42:"P",43:"Q",44:"R",45:"S",46:"T"
                            ,47:"U",48:"V",49:"W",50:"X",51:"Y",52:"Z"}
        dicionarioTroca={"a":1,"b":2 ,"c":3 ,"d": 4, "e": 5, "f": 6,"g":7,"h": 8, "i": 9, "j": 10, "k": 11,
                         "l": 12, "m": 13, "n": 14, "o": 15,"p": 16, "q": 17, "r": 18, "s": 19, "t": 20,"u": 21
                         , "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "A": 27, "B": 28, "C": 29, "D": 30, 
                         "E":31,"F": 32, "G": 33,"H": 34,"I": 35, "J": 36,"K": 37, "L": 38, "M": 39,"N": 40
                         ,"O": 41, "P": 42, "Q": 43, "R": 44, "S": 45,"T": 46,"U": 47, "V":48,"W":49, "X": 50
                         , "Y": 51, "Z": 52}
        #valor referente a cada letra da palavra que será encriptada, alterando por sua vez, para "converter"
        # a letra em numero: a = 1, b= 2; seguindo o dicionario de Troca
        valorLetra = 0
        letraValor = ""
        somaShift = 0
        #lista da primeira conversão; de letras para numeros: a = 1, b = 2; seguindo o dicionario de troca
        listaTrocaValor = []
        #lista da segunda conversão; de numeros para letras
        listaTrocaLetra = []
        mensagemExtensoModificada = ""
        mensagem = self.message_text
        #print(mensagem)
        mensagemExtenso = list(mensagem)
        #print(mensagemExtenso)
        for k in mensagemExtenso:
            if k in dicionarioTroca:
                valorLetra= valorLetra + dicionarioTroca[k]
                listaTrocaValor.append(valorLetra)
                valorLetra = 0
            else:
                listaTrocaValor.append(k)
        #print(listaTrocaValor)
        for m in listaTrocaValor:
            somaShift = 0
            if m in dictionaryShift:
                if m> 26:
                    somaShift =m + shift
                    if somaShift > 52:
                        somaShift = somaShift - 26
                        letraValor = dictionaryShift[somaShift]
                        listaTrocaLetra.append(letraValor)
                    else:
                        letraValor = dictionaryShift[somaShift]
                        listaTrocaLetra.append(letraValor)
                        
                else:
                    somaShift =m + shift
                    if somaShift > 26:
                        somaShift = somaShift - 26
                        letraValor = dictionaryShift[somaShift]
                        listaTrocaLetra.append(letraValor)
                    else:
                        letraValor = dictionaryShift[somaShift]
                        listaTrocaLetra.append(letraValor)
            else:
                listaTrocaLetra.append(m)
        #print(listaTrocaLetra)
        mensagemExtensoModificada =''.join(listaTrocaLetra)
        #print(mensagemExtensoModificada)
        return mensagemExtensoModificada
        

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        #Message.__init__(self,text)
        self.message_text = text
        #Message.get_valid_words(self,valid_words)
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.apply_shift(self.shift)

    def get_shift(self):   
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift
        #pass #delete this line and replace with your code here

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
#        x = self.text
#        x = self.encrypting_dict.copy()
#        x.self.build_shift_dict(self.shift)
#        encrypting_dict = x.copy()
#        x = self.encrypting_dict.copy()
#
#        x.self.build_shift_dict(self.shift)
#
#        #encrypting_dict = x.copy()

#        return encrypting_dict
        
        return self.build_shift_dict(self.shift)
        #pass #delete this line and replace with your code here

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.apply_shift(self.shift)
        #pass #delete this line and replace with your code here

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.apply_shift(self.shift)
        #print("shift "+ str(self.shift))
        #pass #delete this line and replace with your code here


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        
        #pass #delete this line and replace with your code here

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        shift = 0
        valorShift = 0
        melhorValorShift =0
        melhorShift = 0
        melhorCombinacaoPalavra = ""
        tuplaMensagemCodificada = []
        while shift <27:
            valorShift = 0
            mensagemEncriptada = self.apply_shift(shift)
            #print(mensagemEncriptada)
            # transforma a mensagemEncriptada em uma List
            mensagemSplit = mensagemEncriptada.split(" ")
            #print(mensagemSplit)
            for mens in mensagemSplit:
                #print(mens)
                if mens in self.valid_words:
                    #print(mens)
                    valorShift = valorShift + 1
                    if valorShift > melhorValorShift:
                        melhorValorShift = valorShift
                        melhorShift = shift
                        melhorCombinacaoPalavra = mensagemEncriptada
            #print(shift)
            valorShift = 0
            shift = shift + 1
        tuplaMensagemCodificada.append(melhorShift)
        tuplaMensagemCodificada.append(melhorCombinacaoPalavra)
        #print(melhorCombinacaoPalavra)
        #print(melhorValorShift)
        #print(tuplaMensagemCodificada)
        return tuplaMensagemCodificada
            
        
        #pass #delete this line and replace with your code here

        
#def decrypt_story():
#    mensagem = get_story_string()
#    textoEncriptado = CiphertextMessage(mensagem)
#    mensagemDescriptada = textoEncriptado.decrypt_message()
#    return mensagemDescriptada

        
        
        
#Example test case (PlaintextMessage)
d = Message("I Agree week")
#print(d.build_shift_dict(5))
print(d.apply_shift(3))
#print(d.get_message_text())
e = PlaintextMessage("suco",0)
#print(e.get_shift())
#print(e.get_encrypting_dict())
#print(e.change_shift(2))
#print(e.get_shift())
#print(e.get_encrypting_dict())
#print(e.get_message_text_encrypted())
#print(e.get_message_text_encrypted)
#print(d)

#f = CiphertextMessage("Hello")
#print(f.decrypt_message())
#x = decrypt_story()
#print(x)
#
#plaintext = PlaintextMessage('hello', 2)
#print('Expected Output: jgnnq')
#print('Actual Output:', plaintext.get_message_text_encrypted())
#    
##Example test case (CiphertextMessage)
ciphertext = CiphertextMessage("L Djuhh zhhn")
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())
