import random
import trial_division as td


def generate_prime():
    n = random.randint(500, 10000)
    while not td.is_prime(n):
        n = random.randint(500, 10000)
    return n


def main():

    p, q = generate_prime(), generate_prime()

    print(f"p: {p}")
    print(f"q: {q}")

    return 0


if __name__ == "__main__":
    main()
