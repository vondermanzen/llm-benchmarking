import hashlib
import base64

def hash_chain(s: str) -> str:
    # Step 1: Convert input to UTF-8 bytes
    data = s.encode('utf-8')
    
    # Step 2: SHA-256 hash
    sha256_hash = hashlib.sha256(data).digest()
    
    # Step 3: Convert SHA-256 result to Base64
    base64_encoded = base64.b64encode(sha256_hash)
    
    # Step 4: RIPEMD-160 hash of Base64 result
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(base64_encoded)
    ripemd160_digest = ripemd160.digest()
    
    # Step 5: Convert to uppercase hex string
    uppercase_hex = ripemd160_digest.hex().upper()
    
    # Step 6: SHA-1 hash of the uppercase hex string (encoded to bytes)
    sha1_hash = hashlib.sha1(uppercase_hex.encode('utf-8')).digest()
    
    # Step 7: Convert to lowercase hex string
    sha1_hex = sha1_hash.hex()
    
    # Step 8: SHA-512 hash of the lowercase hex string (encoded to bytes)
    sha512_hash = hashlib.sha512(sha1_hex.encode('utf-8')).digest()
    
    # Step 9: Take the first 32 bytes
    first_32_bytes = sha512_hash[:32]
    
    # Step 10: MD5 hash of these 32 bytes
    md5_hash = hashlib.md5(first_32_bytes).digest()
    
    # Step 11: SHA-384 hash of the MD5 digest
    final_hash = hashlib.sha384(md5_hash).hexdigest()
    
    return final_hash

# Read input and print the final result
if __name__ == "__main__":
    S = input().strip()
    print(hash_chain(S))
