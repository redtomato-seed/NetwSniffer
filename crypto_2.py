import unittest
import base64
from py3rijndael import Rijndael
import os
import codecs
#plain text
#a = input("Please Enter Plain text: ")
a = ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") #32
plain_text = a.encode('utf-8')
padded_text = plain_text.ljust(32, b'\x1b')



#key = input("enter key: ")
key = ("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb1") #35?
key_bytes =  codecs.encode(key, 'UTF-8')
#key_bytes = key.encode('utf-8') #two change string to byte
#base64_key_bytes = base64.b64encode(key_bytes) #base  64 encryption
key_bytes = key_bytes[2:-1]
print(key_bytes)

#encryption
rijndael_key = Rijndael(key_bytes, block_size=32)
cipher = rijndael_key.encrypt(padded_text)
print(cipher)

#decryption
cipher = rijndael_key.decrypt(cipher)
print(cipher)