import hashlib
import base64

def hash_chain(s):
    # 1. Start with input string S
    # 2. Convert S to UTF-8 bytes
    data = s.encode('utf-8')
    
    # 3. Calculate SHA-256 hash
    data = hashlib.sha256(data).digest()
    
    # 4. Convert the result to Base64
    data = base64.b64encode(data)
    
    # 5. Calculate RIPEMD-160 hash
    data = hashlib.new('ripemd160', data).digest()
    
    # 6. Convert to uppercase hex string
    data = data.hex().upper().encode('utf-8')
    
    # 7. Calculate SHA-1 hash
    data = hashlib.sha1(data).digest()
    
    # 8. Convert to lowercase hex string
    data = data.hex().lower().encode('utf-8')
    
    # 9. Calculate SHA-512 hash
    data = hashlib.sha512(data).digest()
    
    # 10. Take first 32 bytes
    data = data[:32]
    
    # 11. Calculate MD5 hash
    data = hashlib.md5(data).digest()
    
    # 12. Finally, calculate SHA-384 hash
    result = hashlib.sha384(data).hexdigest()
    
    return result

def main():
    s = input()
    print(hash_chain(s))

if __name__ == "__main__":
    main()