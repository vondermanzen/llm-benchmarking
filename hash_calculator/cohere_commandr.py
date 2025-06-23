import base64
import hashlib

input_string = "Hello, World!"

# Step 1: Convert to UTF-8 bytes
utf8_bytes = input_string.encode("utf-8")

# Step 2: Calculate SHA-256 hash
sha256_hash = hashlib.sha256(utf8_bytes)

# Step 3: Convert to Base64
base64_str = base64.b64encode(sha256_hash.digest()).decode("utf-8")

# Step 4: Calculate RIPEMD-160 hash
ripemd160_hash = hashlib.new("ripemd160", base64_str.encode("utf-8"))
ripemd160_hash_hex = ripemd160_hash.hexdigest().upper()

# Step 5: Calculate SHA-1 hash
sha1_hash = hashlib.sha1(ripemd160_hash_hex.encode("utf-8"))
sha1_hash_hex = sha1_hash.hexdigest()

# Step 6: Calculate SHA-512 hash
sha512_hash = hashlib.sha512(sha1_hash_hex.encode("utf-8"))

# Step 7: Take first 32 bytes of SHA-512 hash
sha512_hash_bytes = sha512_hash.digest()
sha512_hash_hex = sha512_hash_bytes[:32].hex().lower()

# Step 8: Calculate MD5 hash
md5_hash = hashlib.md5(sha512_hash_hex.encode("utf-8"))
md5_hash_hex = md5_hash.hexdigest()

# Step 9: Calculate SHA-384 hash
sha384_hash = hashlib.sha384(md5_hash_hex.encode("utf-8"))
sha384_hash_hex = sha384_hash.hexdigest()

print(sha384_hash_hex)