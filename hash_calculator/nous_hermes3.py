import hashlib
import base64

def hash_chain(s):
    s = s.encode('utf-8')
    s = hashlib.sha256(s).digest()
    s = base64.b64encode(s)
    s = hashlib.new('ripemd160', s).digest()
    s = s.hex().upper()
    s = hashlib.sha1(s.encode()).hexdigest()
    s = s.lower()
    s = hashlib.sha512(s.encode()).digest()[:32]
    s = hashlib.md5(s).digest()
    s = hashlib.sha384(s).hexdigest()
    return s

s = input()
print(hash_chain(s))