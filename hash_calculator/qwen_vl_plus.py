import base64
from binascii import unhexlify
import hashlib

def crypt_hash_chain(input_string):
    # Step 1 & 2 - Convert String to UTF-8 Bytes
    utf8_bytes = input_string.encode("utf-8")
    
    # Step 3 - Calculate SHA-256 Hash
    sha_256 = hashlib.sha256(utf8_bytes).hexdigest()
    
    # Step 4 - Convert Result to Base64
    b64_encoded = base64.b64encode(unhexlify(sha_256)).decode().strip('=')
    
    # Step 5 - Calculate RIPEMD-160 Hash in Upper Case Hex
    ripemd_hex_upper = hashlib.new('ripemd160').digest()[:20].hex().upper()
    
    # Step 6 - Calculate SHA-1 Hash in Lower Case Hex
    sha_1_lower = hashlib.sha1(b64_encoded.encode()).hexdigest().lower()
    
    # Step 7 - Calculate SHA-512 Hash taking first 32 bytes
    sha_512_first_32 = hashlib.sha512(b64_encoded.encode()).digest()[::-1][:32][::-1].hex().lower()
    
    # Step 8 - Calculate MD5 Hash
    md5 = hashlib.md5(b64_encoded.encode()).hexdigest().lower()
    
    # Step 9 - Calculate SHA-384 Hash
    sha_384_final = hashlib.sha384(b64_encoded.encode()).hexdigest().lower()

    return sha_384_final

# Example usage
if __name__ == "__main__":
    s = 'Hello, World!'
    print(crypt_hash_chain(s))