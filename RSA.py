import random
import trial_division as td


def generate_prime():
    n = random.randint(500, 10000)
    while not td.is_prime(n):
        n = random.randint(500, 10000)
    return n


def gcd(a, b):
    if a == 0:
        return b

    if b == 0:
        return a

    # Swap the values so `a` is always bigger
    if a < b:
        a, b = b, a

    remainder = a % b
    return gcd(b, remainder)


def main():

    p, q = generate_prime(), generate_prime()

    print(f"p: {p}")
    print(f"q: {q}")

    modulus = p * q

    euler_totient = (p - 1) * (q - 1)

    print(euler_totient)

    pub_exp = 65537

    print(gcd(270, 192))

    return 0


if __name__ == "__main__":
    main()
