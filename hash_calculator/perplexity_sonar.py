import sys, hashlib, base64

S = sys.stdin.readline().rstrip('\n')

data = S.encode('utf-8')

sha256_hash = hashlib.sha256(data).digest()

base64_encoded = base64.b64encode(sha256_hash)

ripemd160_hash = hashlib.new('ripemd160', base64_encoded).digest()

ripemd160_hex_upper = ripemd160_hash.hex().upper()

sha1_hash = hashlib.sha1(ripemd160_hex_upper.encode('utf-8')).digest()

sha1_hex_lower = sha1_hash.hex()

sha512_hash = hashlib.sha512(sha1_hex_lower.encode('utf-8')).digest()

first_32_bytes = sha512_hash[:32]

md5_hash = hashlib.md5(first_32_bytes).digest()

sha384_hash = hashlib.sha384(md5_hash).hexdigest()

print(sha384_hash)