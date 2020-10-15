import string


class Caesar:
    def __init__(self, key):
        self.key = key
        self.offset = 97

    def encrypt(self, plaintext):
        ciphertext = list()
        for l in plaintext:
            if l in string.ascii_letters:
                l_index = (ord(l.lower()) - self.offset)
                ciphered_l = ((l_index + self.key) % 26) + self.offset
                ciphertext.append(chr(ciphered_l))
            else:
                ciphertext.append(l)

        return ''.join(ciphertext)

    def decrypt(self, ciphertext):
        plaintext = list()
        for l in ciphertext:
            if l in string.ascii_letters:
                l_index = (ord(l.lower()) - self.offset)
                plained_l = ((l_index - self.key) % 26) + self.offset
                plaintext.append(chr(plained_l))
            else:
                plaintext.append(l)

        return ''.join(plaintext)
