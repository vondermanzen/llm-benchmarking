import hashlib
import base64

def calculate_hash_chain(s):
    # Step 2: Convert S to UTF-8 bytes
    utf8_bytes = s.encode('utf-8')
    
    # Step 3: Calculate SHA-256 hash
    sha256_hash = hashlib.sha256(utf8_bytes).digest()
    
    # Step 4: Convert the result to Base64
    base64_bytes = base64.b64encode(sha256_hash)
    
    # Step 5: Calculate RIPEMD-160 hash
    ripemd160_hash = hashlib.new('ripemd160')
    ripemd160_hash.update(base64_bytes)
    ripemd160_hex = ripemd160_hash.hexdigest().upper()
    
    # Step 6: Convert to uppercase hex string (already done in previous step)
    
    # Step 7: Calculate SHA-1 hash
    sha1_hash = hashlib.sha1(ripemd160_hash.digest()).hexdigest().lower()
    
    # Step 8: Convert to lowercase hex string (already done in previous step)
    
    # Step 9: Calculate SHA-512 hash
    sha512_hash = hashlib.sha512(sha1_hash.encode('utf-8')).digest()
    
    # Step 10: Take first 32 bytes
    first_32_bytes = sha512_hash[:32]
    
    # Step 11: Calculate MD5 hash
    md5_hash = hashlib.md5(first_32_bytes).digest()
    
    # Step 12: Finally, calculate SHA-384 hash
    sha384_hash = hashlib.sha384(md5_hash).hexdigest()
    
    # Return the final 64-character hexadecimal hash
    return sha384_hash

# Example usage
input_string = input().strip()
output_hash = calculate_hash_chain(input_string)
print(output_hash)