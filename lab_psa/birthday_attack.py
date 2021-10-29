import hashlib
import os
from random import randint
from base64 import b64encode

def convert(string):
    hash_obj = hashlib.md5(str(string).encode('utf-8')).hexdigest()
    return hash_obj[:7]

def main():
    BD = []
    for i in range(0, 15000):
        day = randint(1,31)
        month = randint(1,12)
        year = randint(1,2021)
        bd = str(day) + str(month) + str(year)
        bd_hash = convert(bd)
        if bd_hash not in BD:
            BD.append(bd_hash)

    while(True):
        kappa = os.urandom(8)
        hash_obj = convert(kappa)
        if hash_obj in BD:
            print('\n',kappa,hash_obj)
            break

    token = b64encode(kappa).decode('utf-8')
    print(token,hash_obj)
if __name__ == '__main__':
    main()