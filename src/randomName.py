import random  # Importerer random-modulen for å velge tilfeldig navn

def random_navn():
    navn_liste = ["Erik", "Nathalie", "Bernt" , "Roger"]  # Lager en liste med navn
    resultat = random.choice(navn_liste)  # Velger et tilfeldig navn fra listen
    print("du fikk navnet", resultat)  # Skriver ut det tilfeldige navnet

input("Trykk enter for å få tildelt et random navn")  # Venter på at bruker trykker enter
random_navn()  # Kaller funksjonen for å vise et tilfeldig navn