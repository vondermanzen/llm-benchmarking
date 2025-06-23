import hashlib
import base64

# Input string
S = input()

# 1. Start with input string S
# 2. Convert S to UTF-8 bytes
utf8_bytes = S.encode('utf-8')

# 3. Calculate SHA-256 hash
sha256_hash = hashlib.sha256(utf8_bytes).digest()

# 4. Convert the result to Base64
base64_str = base64.b64encode(sha256_hash).decode('utf-8')

# 5. Calculate RIPEMD-160 hash
ripemd160_hash = hashlib.new('ripemd160', base64_str.encode('utf-8')).digest()

# 6. Convert to uppercase hex string
uppercase_hex = ripemd160_hash.hex().upper()

# 7. Calculate SHA-1 hash
sha1_hash = hashlib.sha1(uppercase_hex.encode('utf-8')).digest()

# 8. Convert to lowercase hex string
lowercase_hex = sha1_hash.hex().lower()

# 9. Calculate SHA-512 hash
sha512_hash = hashlib.sha512(lowercase_hex.encode('utf-8')).digest()

# 10. Take first 32 bytes
first_32_bytes = sha512_hash[:32]

# 11. Calculate MD5 hash
md5_hash = hashlib.md5(first_32_bytes).digest()

# 12. Finally, calculate SHA-384 hash
sha384_hash = hashlib.sha384(md5_hash).hexdigest()

print(sha384_hash)