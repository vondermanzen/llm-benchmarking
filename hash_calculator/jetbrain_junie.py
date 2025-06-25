import hashlib
import base64

def hash_chain(input_string):
    """
    Calculate a complex chain of cryptographic operations on an input string.
    
    Args:
        input_string (str): The input string to process
        
    Returns:
        str: The final 64-character hexadecimal hash
    """
    # Step 1: Start with input string S
    # Step 2: Convert S to UTF-8 bytes
    data = input_string.encode('utf-8')
    
    # Step 3: Calculate SHA-256 hash
    sha256_hash = hashlib.sha256(data).digest()
    
    # Step 4: Convert the result to Base64
    base64_encoded = base64.b64encode(sha256_hash)
    
    # Step 5: Calculate RIPEMD-160 hash
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(base64_encoded)
    ripemd160_hash = ripemd160.digest()
    
    # Step 6: Convert to uppercase hex string
    uppercase_hex = ripemd160_hash.hex().upper()
    
    # Step 7: Calculate SHA-1 hash
    sha1 = hashlib.sha1(uppercase_hex.encode('utf-8'))
    sha1_hash = sha1.digest()
    
    # Step 8: Convert to lowercase hex string
    lowercase_hex = sha1_hash.hex().lower()
    
    # Step 9: Calculate SHA-512 hash
    sha512 = hashlib.sha512(lowercase_hex.encode('utf-8'))
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

if __name__ == '__main__':
    # Read input
    input_string = input().strip()
    
    # Calculate hash chain
    result = hash_chain(input_string)
    
    # Print result
    print(result)
