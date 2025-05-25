import random

def random_navn():
    navn_liste = ["Erik", "Nathalie"]
    resultat = random.choice(navn_liste)
    print("du fikk navnet", resultat)

input("Trykk enter for å få tildelt et random navn")
random_navn()