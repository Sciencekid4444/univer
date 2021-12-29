import random
import math
from Crypto.Util.number import isPrime


def get_prime() -> int:
    primes = [i for i in range(0, 1000) if isPrime(i)]
    return random.choice(primes)


if __name__ == "__main__":
    p = get_prime()
    q = get_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while e < phi:
        if math.gcd(e, phi) == 1:
            break
        else:
            e += 1
    msg = int(input())
    dd = pow(e, -1)
    d = math.fmod(dd, phi)
    encryption = pow(msg, e)
    decryption = pow(encryption, d)
    encryption = math.fmod(encryption, n)
    decryption = math.fmod(decryption, n)

    print(f'original msg: {msg}')
    print(f'p = {p}, q = {q}, n = {n}, Euler = {phi}')
    print(f'encryption key = {e}')
    print(f'decryption key = {d}')
    print(f'encrypted message = {encryption}')
    print(f'decrypted message = {decryption}')
