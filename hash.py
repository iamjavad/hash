#!/usr/bin/python3.9

import hashlib
string = input(str('enter your string:'))

def sha256():
    Sha256 = hashlib.sha256(string.encode()).hexdigest()
    print(f'Sha256:{Sha256}')
sha256()
def md5():
    Md5 = hashlib.md5(string.encode()).hexdigest()
    print(f'Md5:{Md5}')
md5()
def sha224():
    Sha224 = hashlib.sha224(string.encode()).hexdigest()
    print(f'Sha224:{Sha224}')
sha224()
def sha1():
    sha1 = hashlib.sha1(string.encode()).hexdigest()
    print(f'sha1:{sha1}')
sha1()
