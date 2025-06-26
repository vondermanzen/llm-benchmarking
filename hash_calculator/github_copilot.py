import sys
import hashlib
import base64

def main():
    S = sys.stdin.readline().rstrip('\n')

    # Step 2: Convert S to UTF-8 bytes
    b = S.encode('utf-8')

    # Step 3: Calculate SHA-256 hash
    sha256_digest = hashlib.sha256(b).digest()

    # Step 4: Convert the result to Base64
    b64 = base64.b64encode(sha256_digest)

    # Step 5: Calculate RIPEMD-160 hash
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
    first_32_bytes = sha512_digest[:32]

    # Step 11: Calculate MD5 hash
    md5_digest = hashlib.md5(first_32_bytes).digest()

    # Step 12: Calculate SHA-384 hash
    sha384_final = hashlib.sha384(md5_digest).hexdigest()

    print(sha384_final)

if __name__ == "__main__":
    main()