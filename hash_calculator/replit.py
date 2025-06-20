#!/usr/bin/env python3
"""
Cryptographic Hash Chain Calculator

This program calculates a complex chain of cryptographic operations on an input string
following a 12-step process using standard library functions.
"""

import hashlib
import base64
import sys


def process_hash_chain(input_string):
    """
    Process the input string through a 12-step cryptographic hash chain.
    
    Args:
        input_string (str): The input string to process
        
    Returns:
        str: The final 64-character hexadecimal hash
    """
    try:
        # Step 1: Start with input string S
        current_data = input_string
        
        # Step 2: Convert S to UTF-8 bytes
        current_data = current_data.encode('utf-8')
        
        # Step 3: Calculate SHA-256 hash
        sha256_hash = hashlib.sha256(current_data)
        current_data = sha256_hash.digest()
        
        # Step 4: Convert the result to Base64 (encode hex string, not binary)
        sha256_hex = current_data.hex()
        base64_encoded = base64.b64encode(sha256_hex.encode('utf-8'))
        current_data = base64_encoded
        
        # Step 5: Calculate RIPEMD-160 hash
        ripemd160_hash = hashlib.new('ripemd160', current_data)
        current_data = ripemd160_hash.digest()
        
        # Step 6: Convert to uppercase hex string
        uppercase_hex = current_data.hex().upper()
        current_data = uppercase_hex.encode('utf-8')
        
        # Step 7: Calculate SHA-1 hash
        sha1_hash = hashlib.sha1(current_data)
        current_data = sha1_hash.digest()
        
        # Step 8: Convert to lowercase hex string
        lowercase_hex = current_data.hex().lower()
        current_data = lowercase_hex.encode('utf-8')
        
        # Step 9: Calculate SHA-512 hash
        sha512_hash = hashlib.sha512(current_data)
        current_data = sha512_hash.digest()
        
        # Step 10: Take first 32 bytes
        current_data = current_data[:32]
        
        # Step 11: Calculate MD5 hash
        md5_hash = hashlib.md5(current_data)
        current_data = md5_hash.digest()
        
        # Step 12: Finally, calculate SHA-384 hash
        sha384_hash = hashlib.sha384(current_data)
        final_hash = sha384_hash.hexdigest()
        
        return final_hash
        
    except Exception as e:
        raise ValueError(f"Error processing hash chain: {str(e)}")


def validate_input(input_string):
    """
    Validate the input string according to specifications.
    
    Args:
        input_string (str): The input string to validate
        
    Raises:
        ValueError: If the input is invalid
    """
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    if len(input_string) > 1000:
        raise ValueError("Input string must be 1000 characters or less")
    
    # Check if all characters are printable ASCII
    for char in input_string:
        if ord(char) < 32 or ord(char) > 126:
            raise ValueError("Input string must contain only printable ASCII characters")


def main():
    """
    Main function to handle user input and process the hash chain.
    """
    try:
        # Get input from user
        print("Cryptographic Hash Chain Calculator")
        print("Enter a string to process (1-1000 printable ASCII characters):")
        
        input_string = input().strip()
        
        # Validate input
        validate_input(input_string)
        
        # Process the hash chain
        result = process_hash_chain(input_string)
        
        # Output the result
        print(result)
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
