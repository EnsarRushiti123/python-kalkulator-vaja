def sestej(a, b):
    return a + b

def deli(a, b):
    if b == 0:
        return "Napaka: Deljenje z nič ni mogoče!"
    return a / b


def odstej(a, b):
    return a - b

def pomnozi(a, b):
    return a * b

def deli(a, b):
    if b == 0:
        return "Napaka: Deljenje z nič ni mogoče!"
    return a / b

if izbira == "1":
    x = float(input("Prvo število: "))
    y = float(input("Drugo število: "))
    print(f"Rezultat: {sestej(x, y)}")
elif izbira == "2":
    x = float(input("Prvo število: "))
    y = float(input("Drugo število: "))
    print(f"Rezultat: {odstej(x, y)}")
elif izbira == "4":
    x = float(input("Prvo število: "))
    y = float(input("Drugo število: "))
    print(f"Rezultat: {deli(x, y)}")
    
else:
    print("Neveljavna izbira!")
