# we need the alphabet because we convert letters into numerical values
# to be able to use mathematical operations (note we encrypt the spaces as well)
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 20


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
        if (ALPHABET[index] == '!'):
            print(ALPHABET[index])

    return cipher_text


def caesar_decrypt(cipher_text):

    plain_text = ''

    for c in cipher_text:
        index = ALPHABET.find(c)
        index = (index - KEY) % len(ALPHABET)
        plain_text = plain_text + ALPHABET[index]
        if (ALPHABET[index] == '!'):
            print('Decrypt:', ALPHABET[index])

    return plain_text


if __name__ == '__main__':

    m = "Shannon defined the quality of information as the reduction of uncertainty. The more uncertain you are about something, the more information you get when you learn it. For example, if you are trying to guess a word and you have no idea what it is, then every letter you learn gives you a lot of information. But if you already know the word, then learning each letter gives you very little information. So the quality of information depends on how much uncertainty it reduces."
    encrypted = caesar_encrypt(m)
    print(encrypted)
    print(caesar_decrypt(encrypted))

