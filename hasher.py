#!/usr/bin/python3

import hashlib
from termcolor import colored

hashvalue = input('enter string to hash:')

hashobj1 = hashlib.md5()
hashobj1.update(hashvalue.encode())
print(colored('md5:', 'red') + colored(hashobj1.hexdigest(), 'green'))

hashobj2 = hashlib.sha1()
hashobj2.update(hashvalue.encode())
print(colored('sha1:', 'red') + colored(hashobj2.hexdigest(), 'green'))
