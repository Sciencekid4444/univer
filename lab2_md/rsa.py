import random
from Crypto.Util.number import isPrime


def get_prime() -> int:
    primes = [i for i in range(0, 100) if isPrime(i)]
    return random.choice(primes)



def main() -> any:
    p = get_prime()
    q = get_prime()
    eq = (p - 1) * (q - 1) + 1
    x = 1
    y = 1
    xy = x * y

    while xy != eq:
        x += 1
        y = eq / x
        xy = x * y

    print("public key, x: " + str(x))
    print("private key, y: " + str(y))
    print("modulo (pq): " + str(p * q))

    m = int(input())
    pq = p * q
    exp = m ** x
    encrypted_message = exp % pq
    print('Your de/encrypted message is: ' + str(encrypted_message))



if __name__ == "__main__":
    main()
