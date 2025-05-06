class Berles:  # class kulcsszóval deklarálok egy Berles nevű osztályt
    def __init__(self, felhasznalo_nev, auto, datum):  # init kulcsszóval definiálok egy konstruktort. Felruházom atribútumokkal (felhasznalo_nev, auto, datum) ezeket a paramétereket fogja várni példányosításkor az osztályunk
        # self kulcsszóval eltárolom a paramétereket egy osztálypéldányba
        self._felhasznalo_nev = felhasznalo_nev  # A bérlő neve (pl. "Kocsis Ferenc") non-public attribútum
        self.auto = auto  # Az autó, amit kibérel
        self.datum = datum  # A bérlés dátuma (pl. "2025-05-04")

    def get_felhasznalo_nev(self):  # definiálok egy getter metódust
        return self._felhasznalo_nev  # visszatér a self._felhasznalo_nev non-public attribútummal

    def set_felhasznalo_nev(self, new_felhasznalo_nev):  # definiálok egy setter metódust
        self._felhasznalo_nev = new_felhasznalo_nev  # a self._felhasznalo_nev osztály attribútumot beállítom a new_felhasznalo_new értékre

    felhasznalo_nev = property(get_felhasznalo_nev, set_felhasznalo_nev)  # létrehozok egy felhasznalo_nev attribútumot és a property függvénnyel megadom, hogy a get_felhasznalo_nev és set_felhasznalo_nev tartozik hozzá

    def __str__(self):  # definiálok egy string metódust (dunder metódus), ami akkor fog meghívódni, amikor az osztálypéldányra ráhívok egy print-et
        return f"{self.felhasznalo_nev} béreli: {self.auto.rendszam} ({self.auto.tipus}) - {self.datum} napon"  # megjeleníti a bérlés részleteit
