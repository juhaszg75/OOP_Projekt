from Auto import Auto # Az Auto fájlból importálom az Auto osztályt
class Teherauto(Auto): # Teherauto gyereosztály létrehozása, az Auto ősosztályból származtatva
    def __init__(self, rendszam, tipus, berleti_dij, rakter_kobmeter): # gyerekosztálynak van egy plusz értéke (raktar_kobmeter)
        super().__init__(rendszam, tipus, berleti_dij) # meghívom az ősosztály konstruktorát, hogy a gyerekosztály is megkapja az ősosztály értékeit (rendszam, tipus, berleti_dij)
        # self kulcsszóval eltárolom a paramétert egy osztálypéldányba
        self.rakter_kobmeter = rakter_kobmeter # A teherautók egyedi jellemzője a raktér mérete köbméterben

    def leiras(self): # felülírom az absztrakt osztályban létrehozott leiras metódust, a Teherauto osztály adatait használom és kiíratom az teherautó adatait
        return f"Teherautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Raktér: {self.rakter_kobmeter} m³, Díj: {self.berleti_dij} Ft/nap" # visszatér a teherautó adataival
