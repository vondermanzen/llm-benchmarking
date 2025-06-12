import hashlib
import base64

def hash_chain(s):
    data = s.encode('utf-8')
    
    data = hashlib.sha256(data).digest()
    
    data = base64.b64encode(data)
    
    data = hashlib.new('ripemd160', data).digest()
    
    data = data.hex().upper().encode('utf-8')
    
    data = hashlib.sha1(data).digest()
    
    data = data.hex().encode('utf-8')
    
    data = hashlib.sha512(data).digest()
    
    data = data[:32]
    
    data = hashlib.md5(data).digest()
    
    data = hashlib.sha384(data).hexdigest()
    
    return data

s = input().strip()

result = hash_chain(s)
print(result)