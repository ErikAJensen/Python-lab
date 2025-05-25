import random  # Importerer random-modulen

hemmelig_tall = random.randint(2, 10)  # Lager et tilfeldig tall mellom 2 og 10

gjett = int(input("gjett et tall mellom 1 og 10"))  # Spør brukeren om å gjette et tall

if gjett == hemmelig_tall:  # Sjekker om brukeren gjettet riktig
    print("Gratulerer du gjettet riktig")  # Skriver ut gratulasjon hvis riktig
else:
    print("Feil tall din tulling, riktige tallet er", hemmelig_tall)  # Skriver ut riktig tall hvis feil