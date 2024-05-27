import random
import trial_division as td


def generate_prime(min_value=1000000, max_value=2000000):
    n = random.randint(min_value, max_value)
    while not td.is_prime(n):
        n = random.randint(min_value, max_value)
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


def text_to_int(cipher_text):
    m_int = 0
    for char in cipher_text:
        m_int = (m_int << 8) + ord(char)
    return m_int


def int_to_text(m_int):
    message = ""
    while m_int > 0:
        byte = m_int % 256
        message = chr(byte) + message
        m_int = m_int >> 8
    return message


def main():
    text_to_encrypt = "Lorem"

    while True:
        p, q = generate_prime(), generate_prime()
        modulus = p * q
        euler_totient = (p - 1) * (q - 1)
        pub_exp = 17

        if is_coprime(euler_totient, pub_exp):
            break

    priv_exp = get_mod_inv(pub_exp, euler_totient)

    public_key = (pub_exp, modulus)
    private_key = (priv_exp, modulus)

    m = text_to_int(text_to_encrypt)

    # Check if the modulus is large enough for the message
    if m >= modulus:
        raise ValueError(f"Encrypted text too long for modulus {modulus}")

    print(f"Original message: {text_to_encrypt}")

    # Encryption
    c = pow(m, pub_exp, modulus)

    print(f"Encrypted message numerical value: {c}")

    # Decryption
    og_message = pow(c, priv_exp, modulus)

    decrypted_message = int_to_text(og_message)
    print(f"Decrypted message: {decrypted_message}")

    return 0


if __name__ == "__main__":
    main()
