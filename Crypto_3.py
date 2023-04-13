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

text_data = b'\xcb\x1ax\xa7W^\x8a\xedjD\x0b\xfe\x00\x9a\xa5\xcf\x80<j\xafS\xecSA?\x9a}\xb2\xd2;\x552'
            #b'\x85kJD:'
            #b'\xf5V'
            #b'\x01\xb2\xfdj\xab:U2x'
          #  b'\xdf\xf3\xb0 Y\x87\xce\x8a\xfc\x9a\xe0'
        #    b'\xb1h\x1e\x02\x11z\xa7\x15\xaeU\x1a\x0cw\xc9\xc1\xe3\xafz\xcb<>\xecc\x11\xfeiW#\x8a\x96\x9d{.\xc1\xb0,ma\xbbb\xec8\xea\x07T!=\x18l\xb7\xae\xbf0\xd6P5w\xa5\xeb\xa6\x01{Z\x0c\xb0\x8b\xd6\x16\xf30\x0f\xa7\xc6?O J\xf22\xf1\x86}\x0b\xd2\xba\xf5\xf5Y\x11 \xe7\xe8*\x99\x1a\xce\xa26\xb2IG\x7f\xe4'

#key = input("enter key: ")
key = ("\xde\x0b") #35?
key_bytes =  codecs.encode(key, 'UTF-8')
#key_bytes = key.encode('utf-8') #two change string to byte
#base64_key_bytes = base64.b64encode(key_bytes) #base  64 encryption
key_bytes = key_bytes[2:-1]
print(key_bytes)

#encryption
rijndael_key = Rijndael(key_bytes, block_size=32)
#cipher = rijndael_key.encrypt(padded_text)
print(text_data)

#decryption
cipher = rijndael_key.decrypt(text_data)
print(cipher)