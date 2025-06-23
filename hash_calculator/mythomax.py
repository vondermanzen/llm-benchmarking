import hashlib

def generate_hash_chain(s):
    # Convert input string to UTF-8 bytes
    bytes_input = s.encode('utf-8')

    # Calculate SHA-256 hash
    sha256 = hashlib.sha256()
    sha256.update(bytes_input)
    sha256_hex = sha256.hexdigest()

    # Convert SHA-256 hash to Base64
    base64_sha256 = base64.b64encode(sha256_hex.encode('ascii'))
    base64_sha256_hex = base64_sha256.decode('ascii')

    # Calculate RIPEMD-160 hash
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(bytes_input)
    ripemd160_hex = ripemd160.hexdigest()

    # Convert RIPEMD-160 hash to uppercase hex string
    ripemd160_uppercase_hex = ripemd160_hex.upper()

    # Calculate SHA-1 hash
    sha1 = hashlib.sha1()
    sha1.update(bytes_input)
    sha1_hex = sha1.hexdigest()

    # Calculate SHA-1 hash to lowercase hex string
    sha1_lowercase_hex = sha1_hex.lower()

    # Calculate SHA-512 hash
    sha512 = hashlib.sha512()
    sha512.update(bytes_input)
    sha512_hex = sha512.hexdigest()

    # Extract first 32 bytes of SHA-512 hash
    sha512_first32 = sha512_hex[:32]

    # Calculate MD5 hash
    md5 = hashlib.md5()
    md5.update(bytes_input)
    md5_hex = md5.hexdigest()

    # Calculate final SHA-384 hash
    sha384 = hashlib.sha384()
    sha384.update(bytes_input)
    sha384_hex = sha384.hexdigest()

    # Print final 64-character hexadecimal hash
    print(f"{base64_sha256_hex}:{ripemd160_uppercase_hex}:{sha1_lowercase_hex}:{sha512_first32}:{md5_hex}:{sha384_hex}")

# Test program
generate_hash_chain('Hello, World!')