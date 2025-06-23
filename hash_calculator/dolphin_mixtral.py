import hashlib
import base64

s = input().strip()

s_utf8 = s.encode('utf-8')

sha256 = hashlib.sha256(s_utf8).digest()

base64_str = base64.b64encode(sha256).decode()

ripemd160 = hashlib.new('ripemd160')
ripemd160.update(base64_str.encode())

ripemd160_hex = ripemd160.hexdigest().upper()

sha1 = hashlib.sha1(ripemd160_hex.encode()).digest()

sha1_hex = sha1.hex()

sha512 = hashlib.sha512(sha1_hex.encode()).digest()

sha512_32 = sha512[:32]

md5 = hashlib.md5(sha512_32).digest()

sha384 = hashlib.sha384(md5).digest()

print(sha384.hex())