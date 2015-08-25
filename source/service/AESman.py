#!/usr/bin/env python

#AES code thanks to:
#http://www.codekoala.com/posts/aes-encryption-python-using-pycrypto/


from Crypto.Cipher import AES
import base64
import os

# the block size for the cipher object; must be 16, 24, or 32 for AES
BLOCK_SIZE = 32

# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
PADDING = '{'

# one-liner to sufficiently pad the text to be encrypted
#pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
def pad(password):
    return password+(BLOCK_SIZE - len(password) % BLOCK_SIZE) * PADDING

def make_pass(password):
    return AES.new(pad(password))

# one-liners to encrypt/encode and decrypt/decode a string
# encrypt with AES, encode with base64
#EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
def encode(password, string):
    cipher = make_pass(password)
    encoded = base64.b64encode(cipher.encrypt(pad(string)))
    return encoded

#DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
def decode(password, string):
    cipher = make_pass(password)
    decoded = cipher.decrypt(base64.b64decode(string)).rstrip(PADDING)
    return decoded


# generate a random secret key
#secret = os.urandom(BLOCK_SIZE)

# create a cipher object using the random secret
#cipher = AES.new(secret)


# encode a string
#encoded = EncodeAES(cipher, 'password')
#print 'Encrypted string:', encoded

# decode the encoded string
#decoded = DecodeAES(cipher, encoded)
#print 'Decrypted string:', decoded
