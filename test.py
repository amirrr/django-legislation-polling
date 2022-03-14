import os

from random import randint



def generate_verification_code():
    n = 6
    return ''.join(["{}".format(randint(0, 9)) for num in range(0, n)])



if __name__ == "__main__":
    print(generate_verification_code())