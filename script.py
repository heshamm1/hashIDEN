import hashlib
from hashlib import sha1,sha224,sha256,sha384,sha512,md5,algorithms_available

hash = input("Put your Hash: ")
digits = len(hash)

if digits == 40:
    print("hash is: SHA1 or SHA224 or ripemd160")
elif digits == 64:
    print("hash is: SHA265")
elif digits == 96:
    print("hash is: SHA384")
elif digits == 128:
    print("hash is: SHA512")
elif digits == 32: 
    print("hash is: MD5")
elif digits == 56:
    print('hash is: SHA512/224')
# elif digits != 40 or 64 or 96 or 128 or 32:
#     hash = algorithms_available._hash
#     print("hash is: " + str(hash))
else:
    print("hash not found")

print("D0n3")