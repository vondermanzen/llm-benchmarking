import hashlib
import base64

def hash_chain(input_string):
    # Step 1: Start with input string
    # Step 2: Convert to UTF-8 bytes
    data = input_string.encode('utf-8')

    # Step 3: Calculate SHA-256 hash
    sha256_hash = hashlib.sha256(data).digest()

    # Step 4: Convert to Base64
    base64_result = base64.b64encode(sha256_hash).decode('ascii')

    # Step 5: Calculate RIPEMD-160 hash
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(base64_result.encode('ascii'))
    ripemd_hash = ripemd160.digest()

    # Step 6: Convert to uppercase hex string
    hex_upper = ripemd160.hexdigest().upper()

    # Step 7: Calculate SHA-1 hash
    sha1 = hashlib.sha1(hex_upper.encode('ascii'))
    sha1_hash = sha1.digest()

    # Step 8: Convert to lowercase hex string
    hex_lower = sha1.hexdigest().lower()

    # Step 9: Calculate SHA-512 hash
    sha512 = hashlib.sha512(hex_lower.encode('ascii'))
    sha512_hash = sha512.digest()

    # Step 10: Take first 32 bytes
    first_32_bytes = sha512_hash[:32]

    # Step 11: Calculate MD5 hash
    md5 = hashlib.md5(first_32_bytes)
    md5_hash = md5.digest()

    # Step 12: Finally, calculate SHA-384 hash
    sha384 = hashlib.sha384(md5_hash)
    final_hash = sha384.hexdigest()

    return final_hash

def main():
    # Read a single line of input
    input_string = input().strip()

    # Calculate the hash chain
    result = hash_chain(input_string)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()