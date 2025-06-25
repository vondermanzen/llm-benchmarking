import sys
import base64
import hashlib


def main():
    # Read single line input
    input_data = sys.stdin.readline()
    # Remove trailing newline characters only
    input_data = input_data.rstrip('\n')

    # Step 2: convert to UTF-8 bytes
    data = input_data.encode('utf-8')
    
    # Step 3: SHA-256 hash
    data = hashlib.sha256(data).digest()

    # Step 4: convert to Base64 (bytes)
    data = base64.b64encode(data)

    # Step 5: RIPEMD-160 hash
    data = hashlib.new('ripemd160', data).digest()

    # Step 6: uppercase hex string
    data = data.hex().upper().encode('utf-8')

    # Step 7: SHA-1 hash
    data = hashlib.sha1(data).digest()

    # Step 8: lowercase hex string
    data = data.hex().lower().encode('utf-8')

    # Step 9: SHA-512 hash
    data = hashlib.sha512(data).digest()

    # Step 10: take first 32 bytes
    data = data[:32]

    # Step 11: MD5 hash
    data = hashlib.md5(data).digest()

    # Step 12: SHA-384 hash and output lowercase hex string
    result = hashlib.sha384(data).hexdigest()
    print(result)


if __name__ == "__main__":
    main()
