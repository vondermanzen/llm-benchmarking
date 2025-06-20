import hashlib
import base64

def calculate_hash_chain(input_string: str) -> str:
    current_hash = input_string

    # 1. SHA-256
    sha256_hasher = hashlib.sha256()
    sha256_hasher.update(current_hash.encode('utf-8'))
    current_hash = sha256_hasher.hexdigest()

    # 2. Base64 encode
    # Python's b64encode works on bytes. First, convert hex to bytes.
    hex_bytes = bytes.fromhex(current_hash)
    base64_encoded_bytes = base64.b64encode(hex_bytes)
    current_hash = base64_encoded_bytes.decode('utf-8')

    # 3. RIPEMD-160
    ripemd160_hasher = hashlib.new('ripemd160')
    ripemd160_hasher.update(current_hash.encode('utf-8'))
    current_hash = ripemd160_hasher.hexdigest()

    # 4. SHA-1
    sha1_hasher = hashlib.sha1()
    sha1_hasher.update(current_hash.encode('utf-8'))
    current_hash = sha1_hasher.hexdigest()

    # 5. SHA-512
    sha512_hasher = hashlib.sha512()
    sha512_hasher.update(current_hash.encode('utf-8'))
    current_hash = sha512_hasher.hexdigest()

    # 6. MD5
    md5_hasher = hashlib.md5()
    md5_hasher.update(current_hash.encode('utf-8'))
    current_hash = md5_hasher.hexdigest()

    # 7. SHA-384
    sha384_hasher = hashlib.sha384()
    sha384_hasher.update(current_hash.encode('utf-8'))
    current_hash = sha384_hasher.hexdigest()

    # Final: Truncate to 64 characters
    final_hash = current_hash[:64]
    
    return final_hash

# Example usage:
input_str = "your_string_here"
result_hash = calculate_hash_chain(input_str)
print(f"Input: {input_str}")
print(f"Final Hash: {result_hash}")