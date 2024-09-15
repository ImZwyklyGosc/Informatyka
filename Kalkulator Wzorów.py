import math
PI = math.pi

inp=input("KOD BŁĘDU:√2 (Brak danych). Proszę podać wzór:")

if inp == "?":
    print("""
Dostępne komendy:
-WToB:Wysokość Trójkąta Równobocznego
-PKw:Przekątna Kwadratu
-TPit:Twierdzenie Pitagorasa
""")
else:
    print("KOD BŁĘDU √1 (Brak odpowiedzi). Proszę wpisać odpowiedź:")

if inp == "WToB":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    print(1/2*(a*math.sqrt(3)))

elif inp == "PKw":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    print(a*math.sqrt(2))

elif inp == "TPit":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    b=float(input("KOD BŁĘDU:√6 (Brak wartości dla b). Proszę podać dane dla b:"))
    print(math.sqrt(a**2 + b**2))