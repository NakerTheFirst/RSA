import random
import trial_division as td


def generate_prime():
    n = random.randint(500, 10000)
    while not td.is_prime(n):
        n = random.randint(500, 10000)
    return n


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y


def is_coprime(a, b):
    return gcd(a, b) == 1


def main():

    p, q = generate_prime(), generate_prime()

    print(f"p: {p}")
    print(f"q: {q}")

    modulus = p * q

    euler_totient = (p - 1) * (q - 1)

    print(euler_totient)

    pub_exp = 65537

    if not is_coprime(modulus, pub_exp):
        raise Exception(f"Modulus: {modulus} is not coprime to {pub_exp}")

    d = extended_gcd(modulus, pub_exp)

    return 0


if __name__ == "__main__":
    main()
