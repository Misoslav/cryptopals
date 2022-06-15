in1 = "1c0111001f010100061a024b53535009181c"
in2 = "686974207468652062756c6c277320657965"
expRes = "746865206b696420646f6e277420706c6179"
in1b = bytes.fromhex(in1)
in2b = bytes.fromhex(in2)
print(bytes([a ^ b for a, b in zip(in1b, in2b)]).hex())
print(expRes)
