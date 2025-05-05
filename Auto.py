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


class Szemelyauto(Auto): # Szemelyauto gyereosztály létrehozása, az Auto ősosztályból származtatva
    def __init__(self, rendszam, tipus, berleti_dij, ajtok_szama): # gyerekosztálynak van egy plusz értéke (ajtok_szama)
        super().__init__(rendszam, tipus, berleti_dij) # meghívom az ősosztály konstruktorát, hogy a gyerekosztály is megkapja az ősosztály értékeit (rendszam, tipus, berleti_dij)
        # self kulcsszóval eltárolom a paramétert egy osztálypéldányba
        self.ajtok_szama = ajtok_szama # A személyautók egyedi jellemzője az ajtók száma

    def leiras(self): # felülírom az absztrakt osztályban létrehozott leiras metódust, a Szemelyauto osztály adatait használom és kiíratom az autó adatait
        return f"Személyautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Ajtók: {self.ajtok_szama}, Díj: {self.berleti_dij} Ft/nap" # visszatér az autó adatait


class Teherauto(Auto): # Teherauto gyereosztály létrehozása, az Auto ősosztályból származtatva
    def __init__(self, rendszam, tipus, berleti_dij, rakter_kobmeter): # gyerekosztálynak van egy plusz értéke (raktar_kobmeter)
        super().__init__(rendszam, tipus, berleti_dij) # meghívom az ősosztály konstruktorát, hogy a gyerekosztály is megkapja az ősosztály értékeit (rendszam, tipus, berleti_dij)
        # self kulcsszóval eltárolom a paramétert egy osztálypéldányba
        self.rakter_kobmeter = rakter_kobmeter # A teherautók egyedi jellemzője a raktér mérete köbméterben

    def leiras(self): # felülírom az absztrakt osztályban létrehozott leiras metódust, a Teherauto osztály adatait használom és kiíratom az teherautó adatait
        return f"Teherautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Raktér: {self.rakter_kobmeter} m³, Díj: {self.berleti_dij} Ft/nap" # visszatér a teherautó adataival
