import hashlib
import base64

try:
    from Crypto.Hash import RIPEMD160
except ImportError:
    raise ImportError("You need to install pycryptodome (pip install pycryptodome)")

def hash_chain(s: str) -> str:
    # Step 2: Convert to UTF-8 bytes
    data = s.encode('utf-8')

    # Step 3: SHA-256 hash
    sha256_hash = hashlib.sha256(data).digest()

    # Step 4: Convert to Base64
    base64_encoded = base64.b64encode(sha256_hash)

    # Step 5: RIPEMD-160 hash
    ripemd160 = RIPEMD160.new()
    ripemd160.update(base64_encoded)
    ripemd160_digest = ripemd160.digest()

    # Step 6: Uppercase hex
    uppercase_hex = ripemd160_digest.hex().upper()

    # Step 7: SHA-1 hash
    sha1_hash = hashlib.sha1(uppercase_hex.encode('utf-8')).digest()

    # Step 8: Lowercase hex
    lowercase_hex = sha1_hash.hex()

    # Step 9: SHA-512 hash
    sha512_hash = hashlib.sha512(lowercase_hex.encode('utf-8')).digest()

    # Step 10: Take first 32 bytes
    first_32_bytes = sha512_hash[:32]

    # Step 11: MD5 hash
    md5_hash = hashlib.md5(first_32_bytes).digest()

    # Step 12: SHA-384 hash
    final_hash = hashlib.sha384(md5_hash).hexdigest()

    return final_hash

if __name__ == "__main__":
    import sys
    input_str = sys.stdin.readline().rstrip()
    result = hash_chain(input_str)
    print(result)