import random
import string

def generer_passord(lengde):
    tegn = string.ascii_letters + string.digits + string.punctuation + "øæå"
    passord = "".join(random.choice(tegn) for _ in range(lengde))
    return passord

lengde = int(input("hvor lang passord vil du ha ?"))
print("ditt tilfeldige passord:", generer_passord(lengde))