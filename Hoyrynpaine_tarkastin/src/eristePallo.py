'''
Created on Mar 30, 2023

@author: esa
'''

import numpy as np

"""
    Mittauksessa käytetyn eristepallon ominaisuudet
    @param pullonTilavuus: Pullon tilavuus litroina
    @param pullonTilavuus_err: Pullon tilavuuden virhe litroina
    @param pullonYmparysMitta: Pullon ympärysmitta senttimetreinä
    @param pullonYmparysMitta_err: Pullon ympärysmitan virhe senttimetreinä
"""
class EristePallo:
    def __init__(self, pullonTilavuus, pullonTilavuus_err, pullonYmparysMitta, pullonYmparysMitta_err):
        self.pullonTilavuus = pullonTilavuus
        self.pullonTilavuus_err = pullonTilavuus_err
        self.pullonYmparysMitta = pullonYmparysMitta
        self.pullonYmparysMitta_err = pullonYmparysMitta_err
        
        litratKuutioSenttimetreiksiKerroin = 1000
        
        pullonTilavuus = pullonTilavuus*litratKuutioSenttimetreiksiKerroin #cm**3
        
        self.pullonSisaSade = (3*pullonTilavuus*0.001 / (4*np.pi()))**(1/3) #cm
        self.pullonSisaSade_err = None
        self.pullonUlkoSade = pullonYmparysMitta / (2*np.pi) #cm
        self.pullonUlkoSade_err = None
        self.eristeenPaksuus = self.pullonUlkoSade - self.pullonSisaSade #cm
        self.eristeenPaksuus_err = None
        
        self.lammanJohtavuus = None
        self.lammonJohtuvuus_err = None
     
    """
        Laskee lämmönjohtavuuden, kun veden kiehuessa hukkaan mennyt teho on tiedossa ja eristeen ulkopuolella oleva huoneenlämpötila on tiedossa.
    """    
    def laskeLammonJohtavuus(self, hukkateho, huoneenLampotila):
        kiehuvanVedenLampoTila = 100
        lampotilaEro = kiehuvanVedenLampoTila - huoneenLampotila
        self.lammanJohtavuus=hukkateho*self.eristeenPaksuus/(lampotilaEro*4*np.pi*self.pullonUlkoSade**2)
        