def sestej(a, b):
    return a + b

def odstej(a, b):
    return a - b

def deli(a, b):
    if b == 0:
        return "Napaka: Deljenje z nič ni dovoljeno!"
    return a / b
    
# DODANO: Funkcija za množenje
def pomnozi(a, b):
    return a * b

while True: # ZAČETEK ZANKE
    print("\n--- Mini Kalkulator ---")
    print("1 = seštevanje")
    print("2 = odštevanje")
    print("3 = množenje")
    print("4 = deljenje")
    print("0 = IZHOD") # Nova možnost
    
    izbira = input("Izberi operacijo (0-4): ")
    
    if izbira == "0":
        print("Nasvidenje!")
        break # To prekine zanko in konča program
        
    if izbira in ["1", "2", "3", "4"]:
        x = float(input("Prvo število: "))
        y = float(input("Drugo število: "))
        
        if izbira == "1":
            print(f"Rezultat: {sestej(x, y)}")
        elif izbira == "2":
            print(f"Rezultat: {odstej(x, y)}")
        elif izbira == "3":
            print(f"Rezultat: {pomnozi(x, y)}")
        elif izbira == "4":
            print(f"Rezultat: {deli(x, y)}")
    else:
        print("Neveljavna izbira, poskusi znova!")