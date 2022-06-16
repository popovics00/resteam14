class lokalniUredjaj:
    def __init__(self, imeUredjaja, vreme, trenutnaVrednost):
        self.imeUredjaja = imeUredjaja
        self.vreme = vreme
        self.trenutnaVrednost = trenutnaVrednost

class vremeSlanja:
    def __init__(self, vremeSlanja):
        self.vremeSlanja = vremeSlanja

class Kontroler:
    def __init__(self, imeKontrolera, portKontrolera):
        self.imeKontrolera = imeKontrolera
        self.portKontrolera = portKontrolera
