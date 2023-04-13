import Crypto.Cipher.AES
import binascii
KEY = binascii.unhexlify('AAAABBBBCCCCDDDDEEEEFFFF00001111')
plaintext = binascii.unhexlify('11112222333344445555666677778888')
rijn = AES.new(KEY, AES.MODE_ECB)
ciphertext = rijn.encrypt(plaintext)
binascii.hexlify(ciphertext)
b'ec151e51fc722c06073928d17fa4f6da'
print(binascii.hexlify(ciphertext).decode('utf-8'))
