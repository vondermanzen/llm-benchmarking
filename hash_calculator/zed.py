import hashlib
import base64


def hash_chain_calculator(input_string):
    """
    Calculate a complex chain of cryptographic operations on an input string.

    Args:
        input_string (str): The input string to process

    Returns:
        str: The final 64-character hexadecimal hash
    """

    # Step 1: Start with input string S
    current = input_string

    # Step 2: Convert S to UTF-8 bytes
    current = current.encode('utf-8')

    # Step 3: Calculate SHA-256 hash
    current = hashlib.sha256(current).digest()

    # Step 4: Convert the result to Base64
    current = base64.b64encode(current)

    # Step 5: Calculate RIPEMD-160 hash
    current = hashlib.new('ripemd160', current).digest()

    # Step 6: Convert to uppercase hex string
    current = current.hex().upper()

    # Step 7: Calculate SHA-1 hash
    current = hashlib.sha1(current.encode('utf-8')).digest()

    # Step 8: Convert to lowercase hex string
    current = current.hex().lower()

    # Step 9: Calculate SHA-512 hash
    current = hashlib.sha512(current.encode('utf-8')).digest()

    # Step 10: Take first 32 bytes
    current = current[:32]

    # Step 11: Calculate MD5 hash
    current = hashlib.md5(current).digest()

    # Step 12: Finally, calculate SHA-384 hash
    current = hashlib.sha384(current).hexdigest()

    return current


def main():
    # Read input
    input_string = input().strip()

    # Calculate hash chain and output result
    result = hash_chain_calculator(input_string)
    print(result)


if __name__ == "__main__":
    main()

