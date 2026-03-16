def sestej(a, b): return a + b
def odstej(a, b): return a - b
def pomnozi(a, b): return a * b
def deli(a, b):
    if b == 0: return "Napaka: Deljenje z nič!"
    return a / b

while True:
    print("\n" + "="*20)
    print("  MOJ KALKULATOR")
    print("="*20)
    print("1 | Seštevanje")
    print("2 | Odštevanje")
    print("3 | Množenje")
    print("4 | Deljenje")
    print("0 | IZHOD")
    print("-" * 20)
    
    izbira = input("Izberi (0-4): ")
    
    if izbira == "0":
        print("Nasvidenje!")
        break
        
    if izbira in ["1", "2", "3", "4"]:
        x = float(input("Vnesi prvo število: "))
        y = float(input("Vnesi drugo število: "))
        print("-" * 20) # Ločilna črta pred rezultatom
        
        if izbira == "1":
            print(f"REZULTAT: {x} + {y} = {sestej(x, y)}")
        elif izbira == "2":
            print(f"REZULTAT: {x} - {y} = {odstej(x, y)}")
        elif izbira == "3":
            print(f"REZULTAT: {x} * {y} = {pomnozi(x, y)}")
        elif izbira == "4":
            rez = deli(x, y)
            print(f"REZULTAT: {x} / {y} = {rez}")
        print("-" * 20)
    else:
        print("Neveljavna izbira!")