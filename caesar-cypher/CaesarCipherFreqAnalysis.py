import matplotlib.pylab as plt



LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def frequencyAnalysis(text):
    text=text.upper()

    letterFrequencies={}
    for letter in LETTERS:
        letterFrequencies[letter]=0

    for letter in text:
        if letter in LETTERS:
            letterFrequencies[letter]+=1
    return letterFrequencies


def plotDistribution(frequencies):
    plt.bar(frequencies.keys(),frequencies.values())
    plt.show()

def caesarCrack(cipherText):
    plainText= ''
    key=0
    frequencies = frequencyAnalysis(cipherText)
    frequencies= sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    print(frequencies)
    print("Possible key value: %s" % (LETTERS.find(frequencies[0][0]) - LETTERS.find('E')))
    key=LETTERS.find(frequencies[0][0]) - LETTERS.find('E')

    plainText=caesarDecrypt(cipherText, key)
    print("Plaintext: %s" % plainText)

def caesarDecrypt(cipher_text, key):

    plain_text = ''

    for c in cipher_text:
        index = LETTERS.find(c)
        index = (index - key) % len(LETTERS)
        plain_text = plain_text + LETTERS[index]
    return plain_text

if __name__ == '__main__':
    cypherText = 'MBUHHIHTXYZCHYXTNBYTKOUFCNSTIZTCHZILGUNCIHTUMTNBYTLYXOWNCIHTIZTOHWYLNUCHNSTTNBYTGILYTOHWYLNUCHTSIOTULYTUVIONTMIGYNBCHATTNBYTGILYTCHZILGUNCIHTSIOTAYNTQBYHTSIOTFYULHTCNTTZILTYRUGJFYTTCZTSIOTULYTNLSCHATNITAOYMMTUTQILXTUHXTSIOTBUPYTHITCXYUTQBUNTCNTCMTTNBYHTYPYLSTFYNNYLTSIOTFYULHTACPYMTSIOTUTFINTIZTCHZILGUNCIHTTVONTCZTSIOTUFLYUXSTEHIQTNBYTQILXTTNBYHTFYULHCHATYUWBTFYNNYLTACPYMTSIOTPYLSTFCNNFYTCHZILGUNCIHTTMITNBYTKOUFCNSTIZTCHZILGUNCIHTXYJYHXMTIHTBIQTGOWBTOHWYLNUCHNSTCNTLYXOWYM'
    frequencies = frequencyAnalysis(cypherText)
    caesarCrack(cypherText)