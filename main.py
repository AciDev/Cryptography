from ciphers.caesar import Caesar


def main(key, plaintext):
    c = Caesar(key)

    ciphertext = c.encrypt(plaintext)

    print(ciphertext)

    plaintext = c.decrypt(ciphertext)

    print(plaintext)


if __name__ == '__main__':
    main(28, 'Hello World')
