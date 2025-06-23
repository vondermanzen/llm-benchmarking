import hashlib
import base64

def hash_chain(s):
    # Step 1: Convert input string to UTF-8 bytes
    utf8_bytes = s.encode('utf-8')

    # Step 2: Calculate SHA-256 hash
    sha256_hash = hashlib.sha256(utf8_bytes).digest()

    # Step 3: Convert SHA-256 hash to Base64
    base64_str = base64.b64encode(sha256_hash).decode('utf-8')

    # Step 4: Calculate RIPEMD-160 hash
    ripemd160_hash = hashlib.new('ripemd160', base64_str.encode('utf-8')).hexdigest().upper()

    # Step 5: Calculate SHA-1 hash
    sha1_hash = hashlib.sha1(ripemd160_hash.encode('utf-8')).hexdigest().lower()

    # Step 6: Calculate SHA-512 hash
    sha512_hash = hashlib.sha512(sha1_hash.encode('utf-8')).digest()

    # Step 7: Take the first 32 bytes of SHA-512 hash
    first_32_bytes = sha512_hash[:32]

    # Step 8: Calculate MD5 hash
    md5_hash = hashlib.md5(first_32_bytes).hexdigest().lower()

    # Step 9: Calculate SHA-384 hash
    sha384_hash = hashlib.sha384(md5_hash.encode('utf-8')).hexdigest().lower()

    return sha384_hash

# Test the hash chain with an example input
input_string = input("Enter a string: ")
final_hash = hash_chain(input_string)
print(final_hash)