import secrets
import random


# Function to implement modular exponentiation algorithm.
def fast_mod_exp(base: int, power: int, modulus: int):

    result = 1 

    while power > 0: 
        if power % 2 == 1: 

            result *= base 
            result %= modulus 

        power //= 2
        base *= base
        base %= modulus

    return result

# Function to perform the Miller-Rabin primality test.
def miller_rabin_test(number: int, base: int):

    s = 0
    t = number - 1

    while t % 2 == 0:
        t /= 2
        s += 1

    if fast_mod_exp(base, t, number) == 1:
        return True

    for i in range(0, s):

        if fast_mod_exp(base, t * 2 ** i, number) == number-1:
            return True
    return False

 # Function to generate a prime number using the Miller-Rabin test.
def get_prime(size: int):

    passed = False

    prime = 0

    while not passed:

        passed = True

        prime = secrets.randbits(size // 2)

        bases = set()

        while len(bases) < 10:
            x = secrets.randbits(5)
            bases.add(x)

        for base in bases:
            if miller_rabin_test(prime, base) == False:

                passed = False

                break

        if passed == True:

            for base in bases:

                if miller_rabin_test(2 * prime + 1, base) == False:

                    passed = False

                    break

    return 2 * prime + 1

# Function to find a primitive root generator for a prime number.
def get_generator(prime: int):

    q = (prime - 1) / 2

    while True:
        g = random.randint(2, prime-2)

        if fast_mod_exp(g, q, prime) != 1:

            return g

# Main function to execute the key exchange algorithm.
def main():

    P = get_prime(64)
    print("Prime: " + str(P))

    G = get_generator(P)
    print("Generator: " + str(G))

    X = random.randint(2, P-1)
    print("Jane Doe's Secret: " + str(X))

    Y = random.randint(2, P-1)
    print("John Doe's Secret: " + str(Y))

    A = fast_mod_exp(G, X, P)
    print("Jane Doe's Public: " + str(P))

    B = fast_mod_exp(G, Y, P)
    print("John Doe's Public: " + str(P))

    Key1 = fast_mod_exp(A, Y, P)
    print("The key is: " + str(P))
    Key2 = fast_mod_exp(B, X, P)

    print("Keys Match? " + str(Key1 == Key2))


main()
