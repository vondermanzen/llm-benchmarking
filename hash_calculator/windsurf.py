import hashlib
import base64

def hash_chain(input_string):
    # Step 1: Convert to UTF-8 bytes
    utf8_bytes = input_string.encode('utf-8')
    
    # Step 2: Calculate SHA-256
    sha256_hash = hashlib.sha256(utf8_bytes).digest()
    
    # Step 3: Convert to Base64
    base64_str = base64.b64encode(sha256_hash).decode('ascii')
    
    # Step 4: Calculate RIPEMD-160
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(base64_str.encode())
    ripemd160_hex = ripemd160.hexdigest().upper()
    
    # Step 5: Calculate SHA-1
    sha1_hash = hashlib.sha1(ripemd160_hex.encode()).hexdigest()
    
    # Step 6: Calculate SHA-512
    sha512_hash = hashlib.sha512(sha1_hash.encode()).digest()
    
    # Step 7: Take first 32 bytes
    first_32_bytes = sha512_hash[:32]
    
    # Step 8: Calculate MD5
    md5_hash = hashlib.md5(first_32_bytes).hexdigest()
    
    # Step 9: Calculate SHA-384
    final_hash = hashlib.sha384(md5_hash.encode()).hexdigest()
    
    return final_hash

# Read input
input_string = input().strip()

# Calculate and print final hash
print(hash_chain(input_string))
