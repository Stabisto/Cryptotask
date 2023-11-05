from Crypto.Cipher import DES
import os


with open('key.txt', 'r' , encoding='utf-8') as key_file:
    key = key_file.read()
cipher = DES.new(key.encode(),  DES.MODE_CFB, iv=None)
with open('mes.txt', 'r' , encoding='utf-8') as message_file:
    plaintext = message_file.read()

msg = cipher.encrypt(plaintext.encode('utf-8'))
with open('res.txt', 'wb') as output:
       output.write(msg)

print(plaintext)
print(key)
print(msg)
print(msg.decode(encoding='utf-8', errors='ignore'))


