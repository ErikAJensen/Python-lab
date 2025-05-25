from datetime import datetime

# Finner dagens år
nåværende_år = datetime.now().year

# Spør brukeren om fødselsår
fødselsår = int(input("hvilket år er du født?"))

# Regner ut alder
alder = nåværende_år - fødselsår
 
    # Skriver ut resultatet
print("Du er", alder, "år gammel")