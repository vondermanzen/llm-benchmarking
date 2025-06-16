import hashlib
import base64

def hash_chain(s):
    # 1. Input string S
    # 2. Convert S to UTF-8 bytes
    bytes_utf8 = s.encode('utf-8')
    # 3. Calculate SHA-256 hash
    sha256_hash = hashlib.sha256(bytes_utf8).digest()
    # 4. Convert the result to Base64
    base64_encoded = base64.b64encode(sha256_hash).decode('utf-8')
    # 5. Calculate RIPEMD-160 hash
    ripemd160_hash = hashlib.new('ripemd160', base64_encoded.encode('utf-8')).digest()
    # 6. Convert to uppercase hex string
    hex_uppercase = ripemd160_hash.hex().upper()
    # 7. Calculate SHA-1 hash
    sha1_hash = hashlib.sha1(hex_uppercase.encode('utf-8')).digest()
    # 8. Convert to lowercase hex string
    hex_lowercase = sha1_hash.hex()
    # 9. Calculate SHA-512 hash
    sha512_hash = hashlib.sha512(hex_lowercase.encode('utf-8')).digest()
    # 10. Take first 32 bytes
    first_32_bytes = sha512_hash[:32]
    # 11. Calculate MD5 hash
    md5_hash = hashlib.md5(first_32_bytes).digest()
    # 12. Calculate SHA-384 hash
    sha384_hash = hashlib.sha384(md5_hash).hexdigest()

    return sha384_hash

if __name__ == "__main__":
    s = input()
    result = hash_chain(s)
    print(result)