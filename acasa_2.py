speisekarte={"Pizza": [{"id":101, "title":"Margharita","preis": 5.00},
                       {"id":102, "title":"Funghi","preis": 6.00},
                       {"id":103, "title":"Tuna","preis": 7.00}],

            "Auflauf": [{"id":104, "title":"Nudeln","preis": 5.00},
                        {"id":105, "title":"Kartoffeln","preis": 5.00}],

            "Salat":[{"id": 106, "title": "Tofusalat", "preis": 8.50},
                     {"id": 107, "title": "Hähnchensalat", "preis": 8.50}]

}

# Willkommen

print("willkommen bei Acasa")


#zeige das menü



for gericht in speisekarte:
    print(gericht)


    for dish in speisekarte[gericht]:
        print(f"{dish['id']}, {dish['title']}, {dish['preis']} Euro")


#Bestellwunsch 

Bestellwunsch=[]

print("was möchten Sie bestellen  ?")

while True:
    Eingabe=input()

    if Eingabe=="exit":
        break

    Eingabe=int(Eingabe)

    Bestellwunsch.append(Eingabe)



print("Quittung")
print("*************************")
total=0

for Wunsch in Bestellwunsch:

    for gericht in speisekarte:
        for dish in speisekarte[gericht]:
            if Wunsch==dish["id"]:
                print(f"{dish['id']}, {dish['title']}, {dish['preis']} Euro")
                total+=dish["preis"]

print(f"die Rechnungssume lautet:", total, "Euro")




