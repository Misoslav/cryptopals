import os
from Crypto.Cipher import AES

blocksize = 16
pad = lambda x: x + ((blocksize-len(x)%blocksize)*chr(blocksize-len(x)%blocksize)).encode()
unpad = lambda x: x[:-x[-1]]
parse = lambda y: {x[0] : x[1] for x in [x.split("=") for x in y.split("&")]}
key = os.urandom(blocksize)
cipher = AES.new(key, AES.MODE_ECB)

def oracle(x):
	global cipher
	return cipher.encrypt(pad(("email=" + x + "&uid=10&role=user").encode()))

def decrypt(x):
	global cipher
	print(parse((unpad(cipher.decrypt(x))).decode()))
#----------------------------------------------------
block = lambda x, y: x[y*blocksize:(y+1)*blocksize]
def getPreLen():
	global blocksize
	orig = oracle("")
	prelen = 0
	while True:
		if block(orig, prelen) == block(oracle("a"), prelen):
			prelen += 1
		else:
			break
	#prelen *= blocksize
	for i in range(blocksize):
		if block(oracle("a"*i+"b"), prelen) == block(oracle("a"*i+"c"), prelen):
			prelen *= blocksize
			prelen += blocksize - i			
			break
	return prelen

email = "misa@misa.com"
prelen = getPreLen()
plaintext = pad("email=misa@misa.com&uid=10&role=admin".encode()).decode()
ciphertext = b""
for i in range(len(plaintext)//blocksize):
	ciphertext += block(oracle((blocksize-prelen)*"a"+block(plaintext, i)),1)
decrypt(ciphertext)
