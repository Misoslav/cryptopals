from Crypto.Cipher import AES
from base64 import b64decode

f = open("7file.txt", "r")
fileContent = f.read()
fileContent = fileContent.replace("\n", "")
in1 = b64decode(fileContent)
in1len = len(in1)

key = b"YELLOW SUBMARINE"

cipher = AES.new(key, AES.MODE_ECB)
print(cipher.decrypt(in1).decode())
