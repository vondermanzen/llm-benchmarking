import hashlib
import base64

def hash_chain(s):
    # Step 2: Convert S to UTF-8 bytes
    b = s.encode('utf-8')
    # Step 3: SHA-256 hash
    sha256 = hashlib.sha256(b).digest()
    # Step 4: Base64 encode
    b64 = base64.b64encode(sha256)
    # Step 5: RIPEMD-160 hash
    ripemd160 = hashlib.new('ripemd160', b64).digest()
    # Step 6: Uppercase hex string
    ripemd160_hex = ripemd160.hex().upper()
    # Step 7: SHA-1 hash
    sha1 = hashlib.sha1(ripemd160_hex.encode('utf-8')).digest()
    # Step 8: Lowercase hex string
    sha1_hex = sha1.hex()
    # Step 9: SHA-512 hash
    sha512 = hashlib.sha512(sha1_hex.encode('utf-8')).digest()
    # Step 10: First 32 bytes
    sha512_first32 = sha512[:32]
    # Step 11: MD5 hash
    md5 = hashlib.md5(sha512_first32).digest()
    # Step 12: SHA-384 hash
    sha384 = hashlib.sha384(md5).hexdigest()
    return sha384

if __name__ == "__main__":
    S = input().rstrip('\n')
    print(hash_chain(S))
