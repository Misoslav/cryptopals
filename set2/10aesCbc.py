from Crypto.Cipher import AES

from base64 import b64decode

f = open("10file.txt", "r")
fileContent = f.read()
fileContent = fileContent.replace("\n", "")
in1 = b64decode(fileContent)
in1len = len(in1)



blocksize = 16
key = b"YELLOW SUBMARINE"
IV = "\x00" * blocksize

ciphertext = in1 

pad = lambda x: x + ((blocksize-len(x)%blocksize)*chr(blocksize-len(x)%blocksize)).encode()
unpad = lambda x: x[:-x[-1]]
xor = lambda x,y: bytes([a ^ b for a,b in zip(x,y)])

def encrypt(p, k, iv):
	cipher = AES.new(k, AES.MODE_ECB)
	out = bytearray()
	p = [p[blocksize*i:blocksize*(i+1)] for i in range(len(p)//blocksize)]
	for i in range(len(p)):
		if i == 0:
			out.extend(cipher.encrypt(xor(p[0], iv)))
		else:
			out.extend(cipher.encrypt(xor(p[i], out[-blocksize:])))
	return bytes(out)

def decrypt(c, k, iv):
	cipher = AES.new(k, AES.MODE_ECB)
	out = []
	c = [c[blocksize*i:blocksize*(i+1)] for i in range(len(c)//blocksize)]
	for i in range(1,len(c)):
		out.append(xor(cipher.decrypt(c[-i]), c[-i-1]))
	else:
		out.append(xor(cipher.decrypt(c[0]), iv))
	return unpad("".join([out[-i-1].decode() for i in range(len(out))]).encode()).decode()

#ciphertext = encrypt(pad("Ahoj, jak se mas?").encode(), key, IV.encode())
plaintext = decrypt(ciphertext, key, IV.encode())
print(plaintext)
