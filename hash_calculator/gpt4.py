import hashlib
import base64

def hash_chain(s):
    s = s.encode('utf-8')
    s = hashlib.sha256(s).digest()
    s = base64.b64encode(s)
    s = hashlib.new('ripemd160', s).digest()
    s = s.hex().upper().encode('utf-8')
    s = hashlib.sha1(s).digest()
    s = s.hex().lower().encode('utf-8')
    s = hashlib.sha512(s).digest()[:32]
    s = hashlib.md5(s).digest()
    s = hashlib.sha384(s).hexdigest()
    return s

print(hash_chain("Hello, World!"))