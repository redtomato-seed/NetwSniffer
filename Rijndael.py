
import pkcs7

import py3rijndael.rijndael
from rijndael.cipher.blockcipher import MODE_CBC


class Rijndael():
    def __init__(self, key, iv):
       self.KEY = key
       self.IV = iv
       self.BLOCKSIZE = 32

    def encrypt(self, plain_text):
        rjn = crypt.new(self.KEY, MODE_CBC , self.IV,
        blocksize=self.BLOCKSIZE)
        pad_text = pkcs7.PKCS7Encoder.encode(plain_text)
        return rjn.encrypt(pad_text).encode()

    def decrypt(self, cipher_text):
       rjn = crypt.new(self.KEY, MODE_CBC , self.IV,
       blocksize=self.BLOCKSIZE)
       cipher_text = cipher_text.decode()
       return rjn.decrypt(cipher_text)

r = Rijndael('abcdefghijklmnopqrstuvwxyz123456','abcdefghijklmnopqrstuvwxyzgh3456')
test_text = "this is a test :)"
encrypt = r.encrypt(test_text)
decrypt = r.decrypt(encrypt)
print(test_text)
print(encrypt)
print(decrypt)