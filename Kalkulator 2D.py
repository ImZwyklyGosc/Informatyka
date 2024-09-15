import math
PI = math.pi

inp=input("KOD BŁĘDU:√2 (Brak danych). Proszę podać wzór:")

if inp == "?":
    print("""
Dostępne komendy:
-PKw:Pole Kwadratu
-OKw:Obwód Kwadratu
-PPR:Pole Prosokąta
-OPr:Obwód Prostokąta
-PTa:Pole Trapezu
-OTa:Obwód Trapezu
-Pto:Pole Trójkąta
-OTo:Obwód Trójkąta
-PToB:Obwód Trójkąta Równobocznego
-OToB:Obwód Trójkąta Równobocznego
-PKo:Pole Koła
-OKo:Obwód Koła
-PEl:Pole Epipsy
-OEl:Obwód Elipsy
-PRo1:Pole Rombu 1
-Pro2:Pole Rombu 2
-Oro:Obwód Rombu
""")
else:
    print("KOD BŁĘDU √1 (Brak odpowiedzi). Proszę wpisać odpowiedź:")

if inp == "PKw":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    print(a**2)

elif inp == "Okw":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    print(4*a)

elif inp == "PPr":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    b=float(input("KOD BŁĘDU:√6 (Brak wartości dla b). Proszę podać dane dla b:"))
    print(a*b)

elif inp == "OPr":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    b=float(input("KOD BŁĘDU:√6 (Brak wartości dla b). Proszę podać dane dla b:"))
    print(2*(a+b))

elif inp == "PRw":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    b=float(input("KOD BŁĘDU:√6 (Brak wartości dla b). Proszę podać dane dla b:"))
    print(a*b)

elif input == "ORw":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    b=float(input("KOD BŁĘDU:√6 (Brak wartości dla b). Proszę podać dane dla b:"))
    print(2*a+2*b)

elif inp == "PTa":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    b=float(input("KOD BŁĘDU:√6 (Brak wartości dla b). Proszę podać dane dla b:"))
    h=float(input("KOD BŁĘDU:√13 (Brak wartości dla h). Proszę podać dane dla h:"))
    print(1/2*(h*(a+b)))

elif inp == "OTa":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    b=float(input("KOD BŁĘDU:√6 (Brak wartości dla b). Proszę podać dane dla b:"))
    c=float(input("KOD BŁĘDU:√7 (Brak wartości dla c). Proszę podać dane dla c:"))
    d=float(input("KOD BŁĘDU:√8 (Brak wartości dla d). Proszę podać dane dla d:"))
    print(a+b+c+d)

elif inp == "PTo":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    h=float(input("KOD BŁĘDU:√13 (Brak wartości dla h). Proszę podać dane dla h:"))
    print(1/2*(a*h))

elif inp == "OTo":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    b=float(input("KOD BŁĘDU:√6 (Brak wartości dla b). Proszę podać dane dla b:"))
    print(a*b)

elif inp == "PToB":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    h=float(input("KOD BŁĘDU:√13 (Brak wartości dla h). Proszę podać dane dla h:"))
    print(1/4*(a**2*math.sqrt(3)))

elif inp == "OToB":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    print(3*a)

elif inp == "PKo":
    r=float(input("KOD BŁĘDU:√21 (Brak wartości dla r). Proszę podać dane dla r:"))
    print(PI*r**2)

elif inp == "OKo":
    r=float(input("KOD BŁĘDU:√21 (Brak wartości dla r). Proszę podać dane dla r:"))
    print(2*PI*r)

elif inp == "PEl":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    b=float(input("KOD BŁĘDU:√6 (Brak wartości dla b). Proszę podać dane dla b:"))
    print(PI*a*b)

elif inp == "OEl":
    print("Nie ma prostego wzoru na obwód elipsy (Wzór:L=4aE(ε)=2πa[1−(12)2ε2−(1⋅32⋅4)2⋅ε43−(1⋅3⋅52⋅4⋅6)2⋅ε65−...])")

elif inp == "PRo1":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    h=float(input("KOD BŁĘDU:√13 (Brak wartości dla h). Proszę podać dane dla h:"))
    print(a*h)

elif inp == "PRo2":
    e=float(input("KOD BŁĘDU:√10 (Brak wartości dla e). Proszę podać dane dla e:"))
    f=float(input("KOD BŁĘDU:√11 (Brak wartości dla f). Proszę podać dane dla f:"))
    print(1/2*(e*f))

elif inp == "ORo":
    a=float(input("KOD BŁĘDU:√5 (Brak wartości dla a). Proszę podać dane dla a:"))
    print(4*a)
