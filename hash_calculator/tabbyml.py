import hashlib

def calculate_sha_hash(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

def calculate_base64_hash(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest() + "=="

def calculate_ripemd160_hash(s):
    ripemd = hashlib.new('ripemd160')
    ripemd.update(s.encode('utf-8'))
    return ripemd.hexdigest()

def calculate_uppercase_hex(s):
    return s.upper()

def calculate_sha1_hash(s):
    return hashlib.sha1(s.encode('utf-8')).hexdigest()

def calculate_sha512_hash(s):
    return hashlib.sha512(s.encode('utf-8')).hexdigest()

def calculate_md5_hash(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

def calculate_sha384_hash(s):
    sha384 = hashlib.sha384(s.encode('utf-8'))
    return sha384.hexdigest()

def calculate_chain(s):
    return ''.join([calculate_sha_hash(s), calculate_base64_hash(s), calculate_ripemd160_hash(s), calculate_uppercase_hex(s),
                    calculate_sha1_hash(s), calculate_sha512_hash(s), calculate_sha384_hash(s)])

def main():
    s = input().strip()
    print(calculate_chain(s))

if __name__ == '__main__':
    main()