'''
Created on Mar 30, 2023

@author: esa
'''

import eristePallo as ep

"""
Höyrynpaine luokan tehtävä on huolehtia tiedostojen lukemisesta ja alustaa muuttajat tiedostoissa olevien tietojen mukaan
"""
class Hoyrynpaine:
    
    """
    Lukee datan tekstitiedostosta stringiin
    @param tiedostopolku: Polku, josta luettava tekstitiedosto löytyy
    @return rivit: Palauttaa rivit listan, jossa jokainen listan alkio on yksi tekstitiedostonrivi
    """
    @staticmethod
    def lueDataTiedostosta(tiedostopolku):
        mode = 'r' #'r' = read, 'w' = write, 'a' = append
        with open(tiedostopolku, mode, encoding='utf8') as tiedosto:
            rivit = tiedosto.readlines() #read() lukee kokotiedoston stringiin #readline() lukee tiedoston riviriviltä ja palauttaa stringeinä #readlines() lukee kaikki rivit ja palauttaa string taulukkona
            return rivit
    
    """
    Konstruktori alustaa mittauksen tiedostopolusta löytyvien tiedostojen mukaan
    @param tiedostopolku: Pilku, josta luettavat tekstitiedostot löytyy
    """
    def __init__(self, tiedostopolku):
        self.tiedostopolku = tiedostopolku
        
        self.pallo
        self.__alustaEristePallo()
        
        self.vedenMassa = []
        
        self.astianMassa = []
        self.huoneenlämpötila = []
        
        self.vedenJaAstianMassa = []
        
        self.astianMassa = 0;
        self.vedenMassa = []
        self.vedenMassa_err = []
        
        self.wh_alussa = []
        self.wh_lopussa = []
        self.wh_kulutus = []
        self.wh_kulutus_err = []
        self.alustaSuoraMittaus()
        self.suoraMittaus = SuoraMittaus(self.vedenMassa, self.wh_kulutus)
        
        self.epaSuoraMittaus = EpasuoraMittaus()
    
    """
    Alustaa eristePallon, jonka tiedot on tekstitiedostossa suoraMittausEristePallo.txt. Alla tekstitiedoston esimerkki rakenne. Kaksi ekaa saraketta ovat ohjelman toiminnan kannalta oleellisia. Kolmas sarake on vain esimerkin vuoksi kertomassa mitä yksikköä tulisi käyttää.
        pullonTilavuus    4    l
        pullonTilavuus_err    0.1    l
        pullonYmparysMitta    10    cm
        pullonYmparysMitta_err 5    cm
    """    
    def __alustaEristePallo(self):
        data = self.lueDataTiedostosta(self.tiedostopolku + "suoraMittausEristePallo.txt")
        for rivi in data:
            rivi = rivi.split()
            
            match rivi[0]:
                case "pullonTilavuus":
                    pullonTilavuus = float(rivi[1])
                case "pullonTilavuus_err":
                    pullonTilavuus_err = float(rivi[1])
                case "pullonYmparysMitta":
                    pullonYmparysMitta = float(rivi[1])
                case "pullonYmparysMitta_err":
                    pullonYmparysMitta_err = float(rivi[1])
                case _:
                    print("Tiedostosta suoraMittausEristePallo.txt ylimääräinen rivi")
            
        self.pallo = ep.EristePallo(pullonTilavuus, pullonTilavuus_err, pullonYmparysMitta, pullonYmparysMitta_err)
        
    def alustaSuoraMittaus(self):
        data = self.lueDataTiedostosta(self.tiedostopolku + "suoraMittaus.txt")
        for rivi in data:
            rivi = rivi.split()
            
            self.wh_alussa.append(float(rivi[0]))
            self.wh_lopussa.append(float(rivi[1]))
            self.wh_kulutus.append(float(rivi[1])-float(rivi[2]))
            
            self.vedenJaAstian_massa.append(float(rivi[2]))