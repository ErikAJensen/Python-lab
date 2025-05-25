import random  # Importerer random-funksjonen for å velge tilfeldige tegn.
import string  # Gir tilgang til bokstaver, tall og spesialtegn.

# Passordgenerator: bruker store/små bokstaver, tall, spesialtegn og nordiske bokstaver.
def generer_passord(lengde):
    tegn = string.ascii_letters + string.digits + string.punctuation + "øæå"
    passord = "".join(random.choice(tegn) for _ in range(lengde))
    return passord

# Spør brukeren om ønsket passordlengde.
lengde = int(input("Hvor lang passord vil du ha? "))

# Skriv ut det tilfeldige passordet.
print("Ditt tilfeldige passord:", generer_passord(lengde))
