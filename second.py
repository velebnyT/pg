def cislo_text(cislo):
    cislo = int(cislo)
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desítky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    zvlastni = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]

    if cislo < 0 or cislo > 100:
        return "Číslo není v rozsahu (0-100)"
    
    if cislo == 100:
        return "sto"
    elif cislo < 10:
        return jednotky[cislo]
    elif cislo < 20:
        return zvlastni[cislo - 10]
    else:
        des = cislo // 10
        jed = cislo % 10
        if jed == 0:
            return desítky[des]
        else:
            return desítky[des] + jednotky[jed]
            
if __name__ == "__main__":
# Získání vstupu od uživatele
vstup = input("Zadejte číslo (0-100): ")

# Převod vstupu na celé číslo
try:
    cislo = int(vstup)
    # Výpis textové reprezentace čísla
    print(cislo_text(cislo))
except ValueError:
    print("Zadejte prosím platné číslo.")

