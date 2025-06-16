import hashlib
import base64

S = input()

S = S.encode('utf-8')
S = hashlib.sha256(S).digest()
S = base64.b64encode(S)
S = hashlib.new('ripemd160', S).digest()
S = S.hex().upper()
S = hashlib.sha1(S.encode()).digest()
S = S.hex().lower()
S = hashlib.sha512(S.encode()).digest()[:32]
S = hashlib.md5(S).digest()
S = hashlib.sha384(S).digest().hex()

print(S)