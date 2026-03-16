def sestej(a, b): return a + b
def odstej(a, b): return a - b
def pomnozi(a, b): return a * b
def deli(a, b):
    if b == 0: return "Napaka: Deljenje z nič!"
    return a / b

# SEZNAM ZA ZGODOVINO
zgodovina = []

while True:
    print("\n" + "="*20)
    print("  MOJ KALKULATOR v1.0")
    print("="*20)
    print("1 | Seštevanje")
    print("2 | Odštevanje")
    print("3 | Množenje")
    print("4 | Deljenje")
    print("5 | PRIKAŽI ZGODOVINO") # Nova opcija
    print("0 | IZHOD")
    print("-" * 20)
    
    izbira = input("Izberi (0-5): ")
    
    if izbira == "0":
        print("Nasvidenje!")
        break
    
    if izbira == "5":
        print("\n--- ZGODOVINA IZRAČUNOV ---")
        if not zgodovina:
            print("Zgodovina je še prazna.")
        for vnos in zgodovina:
            print(vnos)
        continue
        
    if izbira in ["1", "2", "3", "4"]:
        x = float(input("Vnesi prvo število: "))
        y = float(input("Vnesi drugo število: "))
        
        rez = 0
        op = ""
        if izbira == "1": rez, op = sestej(x, y), "+"
        elif izbira == "2": rez, op = odstej(x, y), "-"
        elif izbira == "3": rez, op = pomnozi(x, y), "*"
        elif izbira == "4": rez, op = deli(x, y), "/"
        
        izpis = f"{x} {op} {y} = {rez}"
        print(f"\nREZULTAT: {izpis}")
        
        # DODAJANJE V SEZNAM
        zgodovina.append(izpis)
    else:
        print("Neveljavna izbira!")
