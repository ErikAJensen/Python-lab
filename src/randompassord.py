import random
import string

# Passordgenerator: store/små bokstaver, tall, spesialtegn, nordiske bokstaver og brukerinput.
def generer_passord(lengde, ekstra_tegn=""):
    tegn = string.ascii_letters + string.digits + string.punctuation + "øæå" + ekstra_tegn
    passord = "".join(random.choice(tegn) for _ in range(lengde))
    return passord


# Spør brukeren
lengde = int(input("Hvor langt passord vil du ha? "))
ekstra = input("Skriv inn tegn du vil blande inn i passordet (eller trykk Enter for ingen): ")

# Lag og vis passord
print("Ditt tilfeldige passord:", generer_passord(lengde, ekstra))
