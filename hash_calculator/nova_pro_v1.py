import hashlib
import base64

def hash_chain(s):
    s_bytes = s.encode('utf-8')
    sha256_hash = hashlib.sha256(s_bytes).digest()
    base64_encoded = base64.b64encode(sha256_hash)
    ripemd160_hash = hashlib.new('ripemd160', base64_encoded).digest()
    ripemd160_hex = ripemd160_hash.hex().upper()
    sha1_hash = hashlib.sha1(ripemd160_hex.encode()).hexdigest()
    sha512_hash = hashlib.sha512(sha1_hash.encode()).digest()[:32]
    md5_hash = hashlib.md5(sha512_hash).hexdigest()
    final_hash = hashlib.sha384(md5_hash.encode()).hexdigest()
    return final_hash

input_string = input().strip()
print(hash_chain(input_string))