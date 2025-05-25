import random  # Importerer random-modulen

def kast_terning():
    resultat = random.randint(1, 6)  # Trekker et tilfeldig tall mellom 1 og 6
    print("du kastet", resultat)  # Skriver ut resultatet


input("Trykk enter for å kaste terningen")  # Venter på at bruker trykker enter
kast_terning()  # Kaller funksjonen for å kaste terningen