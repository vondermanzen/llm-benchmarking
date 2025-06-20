import hashlib
import base64

def calculate_hash_chain(input_string):
    # Step 1: Start with input string (already done)
    
    # Step 2: Convert to UTF-8 bytes
    current = input_string.encode('utf-8')
    
    # Step 3: Calculate SHA-256 hash
    current = hashlib.sha256(current).digest()
    
    # Step 4: Convert to Base64
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
    final_hash = hashlib.sha384(current).hexdigest()
    
    return final_hash

def main():
    # Read input string
    try:
        input_string = input().strip()
        
        # Validate input length
        if not 1 <= len(input_string) <= 1000:
            print("Input string length must be between 1 and 1000 characters")
            return
            
        # Calculate and print the final hash
        result = calculate_hash_chain(input_string)
        print(result)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
