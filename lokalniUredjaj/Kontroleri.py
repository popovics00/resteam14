class Kontroleri():
    Spisak={}

    @staticmethod
    def DodajUListu(port,imekontrolera):
        #dodaj u kontrolere ime kontrolera sa kljucem koji je zapravo port
        Kontroleri.Spisak[port]=imekontrolera
        Cuvanje() # sacuvaj to
        pass

    @staticmethod
    def UkloniIzListe(port): 
        Kontroleri.Spisak.pop(port) #izbaci iz liste
        pass

    @staticmethod
    def VratiKontolere():
        Cuvanje() #ocitamo sve kontrolere
        for x in Kontroleri.Spisak.keys():    #prodji kroz sve kljuceve
            print("Kontroler sa imenom - "+Kontroleri.Spisak[x]+"  i portom - "+str(x))   #ispisi kontroler
        pass



def Cuvanje():
    Cuvanje.Spisak=getattr(Cuvanje,'Spisak',{})
    for x in Kontroleri.Spisak.keys():
        Cuvanje.Spisak[x]=Kontroleri.Spisak[x]
    Kontroleri.Spisak=Cuvanje.Spisak
    