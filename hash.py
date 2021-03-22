#!/usr/bin/python3.9
import hashlib
z = []
def sha256():
    Sha256 = hashlib.sha256(b'javad').hexdigest()
    print(f'Sha256:{Sha256}')
sha256()
def md5():
    Md5 = hashlib.md5(b'javad').hexdigest()
    print(f'Md5:{Md5}')
md5()
