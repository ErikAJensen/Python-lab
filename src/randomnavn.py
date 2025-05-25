import random


navnliste = ["Emma", "Oliver", "Nora", "Jakob", "Ella", "Liam", "Selma", "Aksel", "Sofie", "Isak", "Erik"]

etternavn = ["Hansen", "Johansen", "Olsen", "Larsen", "Andersen",
    "Pedersen", "Nilsen", "Kristiansen", "Jensen", "Karlsen",
    "Johnsen", "Pettersen", "Eriksen", "Berg", "Haugen",
    "Dahl", "Moen", "Solberg", "Moe", "Strand",
    "Knutsen", "Andreassen", "Paulsen", "Lie", "Halvorsen"]


def velg_navn():
   return random.choice(navnliste)

def velg_etternavn():
   return random.choice(etternavn)


while True:
   svar = input("Trykk enter for nytt navn, eller skriv q for å avslutte")
   if svar.lower() == "q":
      print("Ferdig")
      break
   print("Ditt nye navn er:", velg_navn(), velg_etternavn())
