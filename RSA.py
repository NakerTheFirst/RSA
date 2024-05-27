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


def get_mod_inv(a, b):
    gcd, x, y = extended_gcd(a, b)

    if gcd != 1:
        raise ValueError(f"Modular inverse does not exist for {a} modulo {b}")

    if x < 0:
        x += b

    return x


def is_coprime(a, b):
    return gcd(a, b) == 1


def main():

    text_to_encrypt = "Lorem"
    p, q = generate_prime(), generate_prime()

    modulus = p * q
    euler_totient = (p - 1) * (q - 1)
    pub_exp = 17

    if not is_coprime(modulus, pub_exp):
        raise Exception(f"Modulus: {modulus} is not coprime to {pub_exp}")

    priv_exp = get_mod_inv(modulus, pub_exp)

    public_key = (pub_exp, modulus)
    private_key = (priv_exp, modulus)

    print(modulus)

    m = 2137
    c = m**pub_exp % modulus

    og_message = c**priv_exp % modulus

    print(og_message)

    return 0


if __name__ == "__main__":
    main()
