import hashlib
import base64

def crypto_hash_chain(input_string):
    """
    Calculate a complex chain of cryptographic operations on an input string.
    
    Args:
        input_string (str): The input string to process
        
    Returns:
        str: The final 64-character hexadecimal hash
    """
    # Step 1: Start with input string S
    # Step 2: Convert S to UTF-8 bytes
    current = input_string.encode('utf-8')
    
    # Step 3: Calculate SHA-256 hash
    current = hashlib.sha256(current).digest()
    
    # Step 4: Convert the result to Base64
    current = base64.b64encode(current)
    
    # Step 5: Calculate RIPEMD-160 hash
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(current)
    current = ripemd160.digest()
    
    # Step 6: Convert to uppercase hex string
    current = current.hex().upper().encode('utf-8')
    
    # Step 7: Calculate SHA-1 hash
    current = hashlib.sha1(current).digest()
    
    # Step 8: Convert to lowercase hex string
    current = current.hex().lower().encode('utf-8')
    
    # Step 9: Calculate SHA-512 hash
    current = hashlib.sha512(current).digest()
    
    # Step 10: Take first 32 bytes
    current = current[:32]
    
    # Step 11: Calculate MD5 hash
    current = hashlib.md5(current).digest()
    
    # Step 12: Finally, calculate SHA-384 hash
    current = hashlib.sha384(current).hexdigest()
    
    return current

def main():
    # Read the input string
    input_string = input().strip()
    
    # Calculate the hash chain
    result = crypto_hash_chain(input_string)
    
    # Print the result
    print(result)

if __name__ == "__main__":
    main()
