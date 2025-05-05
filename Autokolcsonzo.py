from Berles import Berles # A Berles fájlból importálom a Berles osztályt

class Autokolcsonzo: # class kulcsszóval deklarálok egy Autokolcsonzo nevű osztályt
    def __init__(self, nev): # init kulcsszóval definiálok egy konstruktort.
        self.nev = nev # A kölcsönző neve (pl. "Best Autókölcsönző")
        self.autok = [] # Elérhető autók listája (Auto objektumokat tárol)
        self.berlesek = [] # Aktuális bérlések listája (Berles objektumokat tárol)

    def auto_hozzaad(self, auto):
        self.autok.append(auto) # Új autó hozzáadása a kölcsönzőhöz

    def berel_auto(self, felhasznalo_nev, rendszam, datum):
        auto = next((a for a in self.autok if a.rendszam == rendszam), None) # Megkeresem az autót a rendszám alapján
        if auto is None:
            print(f"Nincs ilyen rendszámú autó: {rendszam}") # Ha nincs ilyen rendszámú autó, akkor azt kiírja
            return

        if any(b.auto.rendszam == rendszam and b.datum == datum for b in self.berlesek): # Ellenőrzöm, hogy elérhető-e a megadott dátumon
            print(f"Ez az autó már foglalt ezen a napon: {datum}") # Ha foglalt a megadott dátumon, akkor azt kiírja
            return

        uj_berles = Berles(felhasznalo_nev, auto, datum) # Ha minden rendben, létrehozom a bérlést
        self.berlesek.append(uj_berles)
        print(f"Sikeres bérlés! Ár: {auto.berleti_dij} Ft") # Kiírja a sikeres bérlést

    def lemond_berlest(self, felhasznalo_nev, rendszam, datum): # A bérlés lemondás definiálása
        for b in self.berlesek: # Megkeresem a bérlést
            if b.felhasznalo_nev == felhasznalo_nev and b.auto.rendszam == rendszam and b.datum == datum: # Bérlő neve, autó rendszáma és bérlés dátuma alapján
                self.berlesek.remove(b) # Ha van ilyen bérlés, akkor törlöm
                print("Bérlés lemondva.") # Kiíratom, hogy a bérlés lemondva
                return
        print("Nincs ilyen bérlés.") # Ha nincs ilyen bérlés, akkor azt kiíratom

    def listaz_berlesek(self): # Bérlések listázása
        if not self.berlesek: # Ha nincsenek bérlések, akkor kiírja, hogy nincsenek
            print("Nincs aktív bérlés.")
            return
        print("Aktív bérlések:") # Kiíratom az összes bérlés adatait
        for b in self.berlesek:
            print(f" - {b}")