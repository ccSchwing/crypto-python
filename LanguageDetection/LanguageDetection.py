
# we store the english words in a list (maybe a dictionary would be better)
ENGLISH_WORDS = []
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY=5

# load the english words
def get_data():

    dictionary = open('english_words.txt', 'r')

    # initialize the ENGLISH_WORDS list with the words present in the file
    # every word is in a distinct line so that why we have to split('\n')
    for word in dictionary.read().split('\n'):
        ENGLISH_WORDS.append(word)

    dictionary.close()


# count the number of english words in a given text
def count_words(text):
    # upper case letters are needed
    text = text.upper()
    # transform the text into a list of words (split by spaces)
    words = text.split(' ')
    # matches counts the number of english words in the text
    matches = 0

    # consider all the words in the text and check whether the
    # given word is english or not
    for word in words:
        # OPTIMIZE THE DATA STRUCTURE !!!
        if word in ENGLISH_WORDS:
            matches += 1

    return matches


# decides whether a given text is english or not
def is_text_english(text):
    # number of English words in a given text
    matches = count_words(text)

    # you can define your own classification algorithm
    # in this case the assumption: if 50% of the words in the text are english words then
    # it is an english text
    if (float(matches) / len(text.split(' '))) * 100 >= 50:
        return True

    # not an english text
    return False

def caesar_encrypt(plain_text):
    # the encrypted message
    cipher_text = ''
    # we make the algorithm case insensitive
    plain_text = plain_text.upper()

    # consider all the letters in the plain_text
    for c in plain_text:
        # find the numerical representation (index) associated with
        # that character in the alphabet
        index = ALPHABET.find(c)
        # caesar encryption is just a simple shift of characters according
        # to the key use modular arithmetic to transform the values within
        # the range [0,num_of_letters_in_alphabet]
        index = (index + KEY) % len(ALPHABET)
        # keep appending the encrypted character to the cipher_text
        cipher_text = cipher_text + ALPHABET[index]
    return cipher_text

def caesarDecrypt(cipher_text,key):

    plain_text = ''
    print ("key: %s" % key)
    for c in cipher_text:
        index = ALPHABET.find(c)
        index = (index - key) % len(ALPHABET)
        plain_text = plain_text + ALPHABET[index]

    return plain_text
def frequencyAnalysis(text):
    text=text.upper()

    letterFrequencies={}
    for letter in ALPHABET:
        letterFrequencies[letter]=0

    for letter in text:
        if letter in ALPHABET:
            letterFrequencies[letter]+=1
    return letterFrequencies

def caesarCrack(cipherText):
    plainText= ''
    key=0
    frequencies = frequencyAnalysis(cipherText)
    frequencies= sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    print(frequencies)
    print (frequencies[1][0])
    print("Possible key value: %s" % (ALPHABET.find(frequencies[1][0]) - ALPHABET.find('E')))
    key=ALPHABET.find(frequencies[1][0]) - ALPHABET.find('E')

    plainText=caesarDecrypt(cipherText, key)
    print("Plaintext: %s" % plainText)

    return key

if __name__ == '__main__':

    get_data()
    plain_text = 'My name is Balazs Holczer from Budapest, Hungary. I am working as a software engineer software engineer software engineer at the moment'
    cipherText='MBUHHIHTXYZCHYXTNBYTKOUFCNSTIZTCHZILGUNCIHTUMTNBYTLYXOWNCIHTIZTOHWYLNUCHNSTTNBYTGILYTOHWYLNUCHTSIOTULYTUVIONTMIGYNBCHATTNBYTGILYTCHZILGUNCIHTSIOTAYNTQBYHTSIOTFYULHTCNTTZILTYRUGJFYTTCZTSIOTULYTNLSCHATNITAOYMMTUTQILXTUHXTSIOTBUPYTHITCXYUTQBUNTCNTCMTTNBYHTYPYLSTFYNNYLTSIOTFYULHTACPYMTSIOTUTFINTIZTCHZILGUNCIHTTVONTCZTSIOTUFLYUXSTEHIQTNBYTQILXTTNBYHTFYULHCHATYUWBTFYNNYLTACPYMTSIOTPYLSTFCNNFYTCHZILGUNCIHTTMITNBYTKOUFCNSTIZTCHZILGUNCIHTXYJYHXMTIHTBIQTGOWBTOHWYLNUCHNSTCNTLYXOWYMT'

    #cipherText=caesar_encrypt(plain_text)
    print(cipherText)
    key=caesarCrack(cipherText)
    plainText=caesarDecrypt(cipherText,20)
    print(plainText)
    #print(is_text_english(plain_text))