from Auto import Auto # Az Auto fájlból importálom az Auto osztályt
class Szemelyauto(Auto): # Szemelyauto gyereosztály létrehozása, az Auto ősosztályból származtatva
    def __init__(self, rendszam, tipus, berleti_dij, ajtok_szama): # gyerekosztálynak van egy plusz értéke (ajtok_szama)
        super().__init__(rendszam, tipus, berleti_dij) # meghívom az ősosztály konstruktorát, hogy a gyerekosztály is megkapja az ősosztály értékeit (rendszam, tipus, berleti_dij)
        # self kulcsszóval eltárolom a paramétert egy osztálypéldányba
        self.ajtok_szama = ajtok_szama # A személyautók egyedi jellemzője az ajtók száma

    def leiras(self): # felülírom az absztrakt osztályban létrehozott leiras metódust, a Szemelyauto osztály adatait használom és kiíratom az autó adatait
        return f"Személyautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Ajtók: {self.ajtok_szama}, Díj: {self.berleti_dij} Ft/nap" # visszatér az autó adatait