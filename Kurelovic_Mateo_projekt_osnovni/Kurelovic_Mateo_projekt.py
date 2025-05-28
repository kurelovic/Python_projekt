def prikazi_izbornik():
    print("\n1. Dodaj novu bilješku")
    print("2. Pregledaj sve bilješke")
    print("3. Izlaz")
    return input("Odaberi opciju upisivanjem broja: ")

def dodaj_biljesku():
    nova_biljeska=input("\nUnesite novu bilješku: \n")
    with open("biljeske.txt", "a") as datoteka:
        datoteka.write(nova_biljeska + "\n")
    print("Bilješka je uspješno spremljena.")

def pregledaj_biljeske():
    with open("biljeske.txt", "r") as datoteka:
        biljeske=datoteka.readlines()
        if biljeske==[]:
            print("\nNema spremljenih bilješki.")
        else:
            print("\nSve Bilješke: ")
            for i, biljeska in enumerate(biljeske, start=1):
                print(f"{i}. {biljeska.strip()}")
    
radi=True
while radi:
    izbor=prikazi_izbornik()
    if izbor=="1":
        dodaj_biljesku()
    elif izbor=="2":
        pregledaj_biljeske()
    elif izbor=="3":
        print("\nDoviđenja!")
        radi=False
    else:
        print("\nNeispravan odabir. Molim unesi broj 1-3.")
