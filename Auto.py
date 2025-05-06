from abc import ABC, abstractmethod # Az absztrakt osztály az összes autó közös ősosztálya lesz.

class Auto(ABC): # class kulcsszóval deklarálok egy Auto nevű ősosztályt
    def __init__(self, rendszam, tipus, berleti_dij): # init kulcsszóval definiálok egy konstruktort. Felruházom atribútumokkal (rendszam, tipus, berleti_dij) ezeket a paramétereket fogja várni példányosításkor az osztályunk
        # self kulcsszóval eltárolom a paramétereket egy osztálypéldányba
        self.rendszam = rendszam # Rendszám: egyedi azonosító, pl. "AA CD-234"
        self.tipus = tipus # Típus: gyártási típus vagy márkanév, pl. "Mercedes CLA"
        self.berleti_dij = berleti_dij  # Bérleti díj: napi díj forintban

    @abstractmethod # dekorátorral jelölöm, hogy ez egy absztrakt metódus
    def leiras(self): # leiras metodus létrehozása
        pass # absztrakt metódus, a pass-szal jelölöm, hogy nincs megvalósítása
