def sestej(a, b):
    return a + b

def odstej(a, b):
    return a - b

def pomnozi(a, b):
    return a * b

def deli(a, b):
    if b == 0:
        return "Napaka: Deljenje z nič ni dovoljeno!"
    return a / b

def prikazi_meni():
    print("\n--- Mini Kalkulator ---")
    print("1 = Seštevanje")
    print("2 = Odštevanje")
    print("3 = Množenje")
    print("4 = Deljenje")
    print("0 = Izhod")

while True:
    prikazi_meni()
    izbira = input("Izberi operacijo (0-4): ")

    if izbira == "0":
        print("Nasvidenje!")
        break
    
    if izbira in ["1", "2", "3", "4"]:
        try:
            x = float(input("Vnesi prvo število: "))
            y = float(input("Vnesi drugo število: "))
            
            if izbira == "1":
                print(f"Rezultat: {x} + {y} = {sestej(x, y)}")
            elif izbira == "2":
                print(f"Rezultat: {x} - {y} = {odstej(x, y)}")
            elif izbira == "3":
                print(f"Rezultat: {x} * {y} = {pomnozi(x, y)}")
            elif izbira == "4":
                print(f"Rezultat: {x} / {y} = {deli(x, y)}")
        except ValueError:
            print("Napaka: Prosim vnesi številke!")
    else:
        print("Neveljavna izbira, poskusi znova.")