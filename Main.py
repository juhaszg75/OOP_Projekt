from Auto import Szemelyauto, Teherauto # Az Auto fájlból importálom a Szemelyauto és Teherauto osztályokat
from Autokolcsonzo import Autokolcsonzo # Az Autokolcsonzo fájlból importálom az Autokolcsonzo osztályt

def main():
    kolcsonzo = Autokolcsonzo("Best Autókölcsönző") # Példányosítom a kölcsönzőt

    auto1 = Szemelyauto("AA AA-123", "Opel Corsa", 10000, 3) # létrehozom az auto1-et, amit a Szemelyauto osztályból fogok példányosítani, paraméter listába megadtam a várt értékeket (rendszam, tipus, berleti_dij, ajtok_szama)
    auto2 = Teherauto("AA AB-234", "Ford Transit", 15000, 12) # létrehozom az auto2-t, amit a Teherauto osztályból fogok példányosítani, paraméter listába megadtam a várt értékeket (rendszam, tipus, berleti_dij, rakter_kobmeter)
    auto3 = Szemelyauto("AA CB-375", "Volkswagen Golf", 12000, 5) # létrehozom az auto3-at, amit a Szemelyauto osztályból fogok példányosítani, paraméter listába megadtam a várt értékeket (rendszam, tipus, berleti_dij, ajtok_szama)
    # A kolcsonzo-höz hozzáadok három autót
    kolcsonzo.auto_hozzaad(auto1)
    kolcsonzo.auto_hozzaad(auto2)
    kolcsonzo.auto_hozzaad(auto3)
    # Előre betöltök négy bérlést
    kolcsonzo.berel_auto("Horváth Emőke", "AA AA-123", "2025-05-10")
    kolcsonzo.berel_auto("Pásztor Ferenc", "AA AB-234", "2025-05-11")
    kolcsonzo.berel_auto("Szabó László", "AA CB-375", "2025-05-12")
    kolcsonzo.berel_auto("Kocsis Boróka", "AA AA-123", "2025-05-13")

    # Végtelen ciklusban megjelenő konzolos menü, amely lehetővé teszi a felhasználó számára,
    # hogy műveleteket hajtson végre: új bérlés, bérlés lemondása, aktuális bérlések listázása, vagy kilépés.
    while True:
        print("\n=== AUTÓKÖLCSÖNZŐ MENÜ ===")
        print("1. Új bérlés")
        print("2. Bérlés lemondása")
        print("3. Aktuális bérlések listázása")
        print("4. Kilépés")

        valasztas = input("Válassz egy opciót (1-4): ").strip()
         # Új bérlés
        if valasztas == "1":
            felhasznalo = input("Add meg a neved: ").strip() # A bérlő nevének megadása
            rendszam = input("Add meg a rendszámot: ").strip() # A bérelni kívánt autó rendszáma
            datum = input("Add meg a dátumot (ÉÉÉÉ-HH-NN): ").strip() # A bérelt nap megadása
            kolcsonzo.berel_auto(felhasznalo, rendszam, datum)
        # Bérlés lemondása
        elif valasztas == "2":
            felhasznalo = input("Név: ").strip() # A bérlő nevének megadása
            rendszam = input("Rendszám: ").strip() # A lemondani kívánt autó rendszámának megadása
            datum = input("Dátum (ÉÉÉÉ-HH-NN): ").strip() # A lemondani kívánt bérlés dátumának megadása
            kolcsonzo.lemond_berlest(felhasznalo, rendszam, datum)
        # Bérlések listázása
        elif valasztas == "3":
            kolcsonzo.listaz_berlesek()
        # Kilépés a programból
        elif valasztas == "4":
            print("Kilépés...")
            break
        else:
            print("Hibás választás!")

if __name__ == "__main__": # Ez a fájl a főprogramként fut, meghívjuk a main() függvényt, ez indítja el az autókölcsönző rendszer működését.
    main()
