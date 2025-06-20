import sys
import hashlib
import base64

def cryptographic_hash_chain(s: str) -> str:
    # Step 2: Convert S to UTF-8 bytes
    b = s.encode('utf-8')

    # Step 3: Calculate SHA-256 hash
    sha256_digest = hashlib.sha256(b).digest()

    # Step 4: Convert the result to Base64
    b64 = base64.b64encode(sha256_digest)

    # Step 5: Calculate RIPEMD-160 hash (use hashlib.new('ripemd160'))
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(b64)
    ripemd160_digest = ripemd160.digest()

    # Step 6: Convert to uppercase hex string
    ripemd160_hex_upper = ripemd160_digest.hex().upper()

    # Step 7: Calculate SHA-1 hash
    sha1_digest = hashlib.sha1(ripemd160_hex_upper.encode('utf-8')).digest()

    # Step 8: Convert to lowercase hex string
    sha1_hex_lower = sha1_digest.hex()

    # Step 9: Calculate SHA-512 hash
    sha512_digest = hashlib.sha512(sha1_hex_lower.encode('utf-8')).digest()

    # Step 10: Take first 32 bytes
    sha512_first32 = sha512_digest[:32]

    # Step 11: Calculate MD5 hash
    md5_digest = hashlib.md5(sha512_first32).digest()

    # Step 12: Finally, calculate SHA-384 hash
    sha384_digest = hashlib.sha384(md5_digest).hexdigest()

    # Output: 64-character lowercase hex string
    return sha384_digest

if __name__ == "__main__":
    input_str = sys.stdin.readline().rstrip('\n')
    result = cryptographic_hash_chain(input_str)
    print(result)