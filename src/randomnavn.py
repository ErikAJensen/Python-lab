import random
import string

def random_name(lengdenavnm):
    teggn = string.ascii_letters
    navn = "".join(random.choice(teggn) for _ in range(lengdenavnm))
    return navn

lengde = int(input("hvor mange bokstaver skal navnet ditt ha ?"))
print("ditt nye navn er", random_name(lengde))
