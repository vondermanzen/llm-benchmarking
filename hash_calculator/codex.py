import hashlib
import base64

# Step 1: Input string
s = input().strip()

# Step 2: UTF-8 encoding
utf8_bytes = s.encode('utf-8')

# Step 3: SHA-256 hash
sha256_hash = hashlib.sha256(utf8_bytes).digest()

# Step 4: Convert to Base64
b64_encoded = base64.b64encode(sha256_hash)

# Step 5: RIPEMD-160 hash
ripemd160_hash = hashlib.new('ripemd160', b64_encoded).digest()

# Step 6: Uppercase hex
ripemd160_hex_upper = ripemd160_hash.hex().upper()

# Step 7: SHA-1 hash of uppercase hex string
sha1_hash = hashlib.sha1(ripemd160_hex_upper.encode('utf-8')).digest()

# Step 8: Lowercase hex
sha1_hex_lower = sha1_hash.hex()

# Step 9: SHA-512 hash
sha512_hash = hashlib.sha512(sha1_hex_lower.encode('utf-8')).digest()

# Step 10: First 32 bytes
first_32_bytes = sha512_hash[:32]

# Step 11: MD5 hash
md5_hash = hashlib.md5(first_32_bytes).digest()

# Step 12: SHA-384 hash
sha384_hash = hashlib.sha384(md5_hash).hexdigest()

# Final output
print(sha384_hash)
