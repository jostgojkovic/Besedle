import random

class Barve:
    ZELENA = '\033[92m'
    RUMENA = '\033[93m'
    NORMALNA = '\033[0m'


class Stanje_crk:

    def __init__(self, znak):
        self.znak = znak
        self.v_besedi = False
        self.v_poziciji = False

    def __repr__(self):
        return f'[{self.znak} v besedi: {self.v_besedi}, v poziciji: {self.v_poziciji}]'


class Besedle:

    MAX_STEVILO_POSKUSOV = 6
    DOLZINA_BESEDE = 5

    
    def __init__(self, geslo):
        self.geslo = geslo.upper()
        self.poskusi = []
    
    def dodaj_poskus(self, beseda):
        beseda = beseda.upper()
        self.poskusi.append(beseda) # [petka, tarok, meter]

    def ugibaj(self, beseda):
        beseda = beseda.upper()
        rezultat = [Stanje_crk(znak) for znak in beseda]

        pomozna_skrivnost = list(self.geslo)

        for i in range(self.DOLZINA_BESEDE):
            crka = rezultat[i]
            if crka.znak == pomozna_skrivnost[i]:
                crka.v_poziciji = True
                pomozna_skrivnost[i] = '*'

        for i in range(self.DOLZINA_BESEDE):
            crka = rezultat[i]
            if crka.v_poziciji:
                continue

            for j in range(self.DOLZINA_BESEDE):
                if crka.znak == pomozna_skrivnost[j]:
                    pomozna_skrivnost[j] = '*'
                    crka.v_besedi = True
                    break

        return rezultat

    def zmaga(self):
        return len(self.poskusi) > 0 and  self.poskusi[-1] == self.geslo

    def preostali_poskusi(self):
        return self.MAX_STEVILO_POSKUSOV - len(self.poskusi)

    def lahko_poskusi(self):
        return self.preostali_poskusi() > 0 and not self.zmaga()
        
    def izberi_namig(self):
        seznam_geslo = list(self.geslo)
        for j in range(len(self.poskusi)):
            for i in range(self.DOLZINA_BESEDE):
                if self.poskusi[j][i] in seznam_geslo:
                    seznam_geslo.remove(self.poskusi[j][i])
        if len(seznam_geslo) != 0:
            return random.choice(seznam_geslo)
        elif len(seznam_geslo) == 0:
            print('Imaš že vse črke!')
    
# bug 1: če imam vse črke, namig vrne None
'''
petka, kamen, blišč, račka,
krčma
'''
# bug 2: če pri namigu ne vneseš da/ne je isto kot ne 
            
