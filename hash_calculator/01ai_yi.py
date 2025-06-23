import hashlib
import base64

def calculate_hash_chain(input_str):
    S = input_str
    
    S_bytes = S.encode('utf-8')
    
    hash_256 = hashlib.sha256(S_bytes).digest()
    
    base64_encoded = base64.b64encode(hash_256)
    
    hash_ripemd = hashlib.new('ripemd160', base64_encoded).digest()
    
    upper_hex = hash_ripemd.hex().upper()
    
    hash_sha1 = hashlib.sha1(bytes.fromhex(upper_hex)).digest()
    
    lower_hex = hash_sha1.hex().lower()
    
    hash_512 = hashlib.sha512(bytes.fromhex(lower_hex)).digest()
    
    first_32_bytes = hash_512[:32]
    
    hash_md5 = hashlib.md5(first_32_bytes).digest()
    
    hash_384 = hashlib.sha384(hash_md5).digest()
    
    return hash_384.hex()

input_str = "Hello, World!"
output = calculate_hash_chain(input_str)
print(output)