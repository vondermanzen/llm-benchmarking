import hashlib
import base64

s = input()
s = s.encode('utf-8')
s = hashlib.sha256(s).digest()
s = base64.b64encode(s).decode('utf-8')
s = hashlib.new('ripemd160', s.encode('utf-8')).digest()
s = s.hex().upper()
s = hashlib.sha1(s.encode('utf-8')).digest()
s = s.hex()
s = hashlib.sha512(s.encode('utf-8')).digest()
s = s[:32]
s = hashlib.md5(s).digest()
s = hashlib.sha384(s).hexdigest()
print(s)