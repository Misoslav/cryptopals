import cbc, os
import math

blocksize = 16
pad = lambda x: x + ((blocksize-len(x)%blocksize)*chr(blocksize-len(x)%blocksize)).encode()
unpad = lambda x: x[:-x[-1]]
xor = lambda x,y: bytes([a ^ b for a,b in zip(x,y)])
key = os.urandom(16)
iv = os.urandom(16)
pre = "comment1=cooking MCs;userdata="
post = ";comment2= like a pound of bacon"

def encrypt(p):
	global key, iv
	return cbc.encrypt(pad((pre + p + post).encode()), key, iv)

def decrypt(c):
	global key, iv
	return cbc.decrypt(c, key, iv)


ciphertext = encrypt((blocksize-len(pre)%blocksize)*"a")
message = ";admin=true;".encode()
prelen = math.ceil(len(pre)/blocksize)*blocksize - blocksize
msgxor = xor(message, post[:len(message)].encode())
ciphertext = ciphertext[:prelen] + xor(ciphertext[prelen:prelen+len(msgxor)], msgxor) + ciphertext[prelen+len(msgxor):]

print(decrypt(ciphertext))

"""
  5
1234
5^3=x
x^enc(2)
"""
