
import math
PI = math.pi

inp=input("KOD BŁĘDU:√2 (Brak danych). Proszę podać wzór:")

if inp == "?":
    print("""
Dostępne komendy:
-Osz:Objętość Sześcianu
-PPSz:Pole Powierzchni Sześcianu
-OPr:Objętość Prostopadłościanu
-PPPr:Obwód Prostokąta
-OOs:Objętość Ostrosłupa
-PPOs:Pole Powirzchni Ostrosłupa
-OWa:Objętość Walca
-PPWa:Pole Powierzchni Walca
-OSt:Objętość Stożka
-PPSt:Pole Powierzchni Stożka
-Oku:Pole Koła
-PPku:Obwód Koła
""")
else:
    print("KOD BŁĘDU √1 (Brak odpowiedzi). Proszę wpisać odpowiedź:")

if inp == "OSz":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    print(a**3)

elif inp == "PPSz":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    print(6*a**2)

elif inp == "OPr":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    b=float(input("KOD BŁĘDU:√6 (Brak wartości dla b). Proszę podać dane dla b:"))
    c=float(input("KOD BŁĘDU:√7 (Brak wartości dla c). Proszę podać dane dla c:"))
    print(a*b*c)

elif inp == "PPPr":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    b=float(input("KOD BŁĘDU:√6 (Brak wartości dla b). Proszę podać dane dla b:"))
    c=float(input("KOD BŁĘDU:√6 (Brak wartości dla c). Proszę podać dane dla c:"))
    print(2*(a*b)+2*(a*c)+2*(c*b))

elif inp == "OOs":
    Pp=float(input("KOD BŁĘDU:√20.17 (Brak wartości dla Pp). Proszę podać dane dla Pp:"))
    h=float(input("KOD BŁĘDU:√13 (Brak wartości dla h). Proszę podać dane dla h:"))
    print(1/3*(Pp*h))

elif input == "PPOs":
    Pp=float(input("KOD BŁĘDU:√20.17 (Brak wartości dla Pp). Proszę podać dane dla Pp:"))
    Pb=float(input("KOD BŁĘDU:√20.02 (Brak wartości dla Pb). Proszę podać dane dla Pb:"))
    print(Pp+Pb)

elif inp == "Owa":
    h=float(input("KOD BŁĘDU:√13 (Brak wartości dla h). Proszę podać dane dla h:"))
    r=float(input("KOD BŁĘDU:√22 (Brak wartości dla r). Proszę podać dane dla r:"))
    print(PI*r**2*h)

elif inp == "PPWa":
    h=float(input("KOD BŁĘDU:√13 (Brak wartości dla h). Proszę podać dane dla h:"))
    r=float(input("KOD BŁĘDU:√22 (Brak wartości dla r). Proszę podać dane dla r:"))
    print(2*PI*r**2+2*PI*r*h)


elif inp == "OSt":
    h=float(input("KOD BŁĘDU:√13 (Brak wartości dla h). Proszę podać dane dla h:"))
    r=float(input("KOD BŁĘDU:√22 (Brak wartości dla r). Proszę podać dane dla r:"))
    print(1/3*PI*r**2*h)

elif inp == "PPSt":
    l=float(input("KOD BŁĘDU:√15 (Brak wartości dla l). Proszę podać dane dla l:"))
    r=float(input("KOD BŁĘDU:√22 (Brak wartości dla r). Proszę podać dane dla r:"))
    print(PI*r**2+PI*r*l)

elif inp == "OKu":
    r=float(input("KOD BŁĘDU:√22 (Brak wartości dla r). Proszę podać dane dla r:"))
    print(4/3*PI*r**3)

elif inp == "PPKu":
    r=float(input("KOD BŁĘDU:√22 (Brak wartości dla r). Proszę podać dane dla r:"))
    print(4*PI*r**2)
