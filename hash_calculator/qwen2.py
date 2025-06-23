import hashlib
import base64

def hash_chain_calculator(input_string):
    # Step 2: Convert S to UTF-8 bytes
    utf8_bytes = input_string.encode('utf-8')
    
    # Step 3: Calculate SHA-256 hash
    sha256_hash = hashlib.sha256(utf8_bytes).digest()
    
    # Step 4: Convert the result to Base64
    base64_encoded = base64.b64encode(sha256_hash)
    
    # Step 5: Calculate RIPEMD-160 hash
    ripemd160_hash = hashlib.new('ripemd160', base64_encoded).digest()
    
    # Step 6: Convert to uppercase hex string
    ripemd160_hex = ripemd160_hash.hex().upper()
    
    # Step 7: Calculate SHA-1 hash
    sha1_hash = hashlib.sha1(ripemd160_hex.encode()).digest()
    
    # Step 8: Convert to lowercase hex string
    sha1_hex = sha1_hash.hex().lower()
    
    # Step 9: Calculate SHA-512 hash
    sha512_hash = hashlib.sha512(sha1_hex.encode()).digest()
    
    # Step 10: Take first 32 bytes
    sha512_first32 = sha512_hash[:32]
    
    # Step 11: Calculate MD5 hash
    md5_hash = hashlib.md5(sha512_first32).digest()
    
    # Step 12: Calculate SHA-384 hash
    sha384_hash = hashlib.sha384(md5_hash).hexdigest()
    
    return sha384_hash

# Example usage
input_string = "Hello, World!"
print(hash_chain_calculator(input_string))