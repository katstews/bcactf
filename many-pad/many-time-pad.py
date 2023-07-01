from Crypto.Util.number import *
# secret_key = open("secret_key.txt", "rb").read()

# def enc(bstr):
#     return long_to_bytes(bytes_to_long(bstr) ^ bytes_to_long(secret_key))

# # gotta encode my grocery list
# # break this by XOR the string groceries w the jumbled file, but how the FUCK
# groceries = b"I need to buy 15 eggs, 1.7 kiloliters of milk, 11000 candles, 12 cans of asbestos-free cereal, and 0.7 watermelons."
# out = open("grocery-list.out", "wb")
# out.write(enc(groceries))
# out.close()

# # # gotta encode my flag
# out = open("many-time-pad.out", "wb")
# out.write(enc(open("flag.txt", "rb").read()))
# out.close()
groceries = b"I need to buy 15 eggs, 1.7 kiloliters of milk, 11000 candles, 12 cans of asbestos-free cereal, and 0.7 watermelons."

## READ AS BYTESSS OMFG, duhhhhhhhhhHHHHHHHHHHHH
with open("grocery-list.out",'rb') as file:
    data = file.read()
    

with open("many-time-pad.out",'rb') as file:
    data1 = file.read()
    
val = bytes_to_long(data) ^ bytes_to_long(data1)
print(long_to_bytes(val)) ## this is the mf key "secret key"

# len of key is == groceries string, thus XOR the two strings of same length
# together
key = b'I need to buy 15 eggs, 1.7 kiloliters of milk, 11000 candles, 12 cans of asbestos-\x04\x11\x04\x06T\x05\x1e\x0bV\x003\x1cN\r\x17;Uc\x1dhT\x1fR\x07 -\\:\x18\x06\x03@S'

print(len(key))
print(len(groceries))

val = bytes_to_long(groceries) ^ bytes_to_long(key)
print(long_to_bytes(val))

# key1 = b'bcactf{y3a_0nly_uS3_th3sE_1_tim3}'
##OMGGGGG I GOT IT!!! flag = b'bcactf{y3a_0nly_uS3_th3sE_1_tim3}' 
# HOLY SHIT
