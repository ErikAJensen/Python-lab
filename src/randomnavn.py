import random


navnliste = ["Emma", "Oliver", "Nora", "Jakob", "Ella", "Liam", "Selma", "Aksel", "Sofie", "Isak", "Erik"]

def velg_navn():
   return random.choice(navnliste)


while True:
   svar = input("Trykk enter for nytt navn, eller skriv q for å avslutte")
   if svar.lower() == "q":
      print("Ferdig")
      break
   print("Ditt nye navn er:", velg_navn())
   