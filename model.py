import json
import random


# bug 1: če imam vse črke, namig vrne None
'''
petka, kamen, blišč, račka,
krčma

'''

DATOTEKA_Z_BESEDAMI = 'besede.txt'
DATOTEKA_S_STANJEM = 'stanje.json'


class Barve:
    ZELENA = '\033[92m'
    RUMENA = '\033[93m'
    NORMALNA = '\033[0m'


class Stanje_crk:

    def __init__(self, znak):
        self.znak = znak
        self.v_besedi = False
        self.v_poziciji = False


class Besedle:

    MAX_STEVILO_POSKUSOV = 6
    DOLZINA_BESEDE = 5

    
    def __init__(self, geslo):
        self.geslo = geslo.upper()
        self.poskusi = []

    def dodaj_poskus(self, beseda):
        beseda = beseda.upper()
        self.poskusi.append(beseda) 

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
    


    # kle probem nardit sharnjevanje stanja ampak nevem kaj se dogaja

    def v_slovar(self):
        return {
            'id_igre': 'id_igre', # dodaj nekam id_igre
            'geslo': self.geslo,
        }
    

    @staticmethod
    def iz_slovarja(slovar):
        pass

'''
{
    {
        'id_igre' = 1
        'geslo' = 'PETKA'
    },

    {
        'id_igre' = 2
        'geslo' = 'MESTO'
    }
}

'''


with open(DATOTEKA_Z_BESEDAMI) as f:
    seznam_besed = [vrstica.strip().upper() for vrstica in f if len(vrstica) == 6]

def nova_igra():
    return Besedle(random.choice(seznam_besed))



class Stanje:
    
    pass



#     def __init__(self):
#         self.igre = {}
#         self.datoteka_s_stanjem = DATOTEKA_S_STANJEM

#     def prost_id_igre(self):
#         if self.igre == {}:
#             return 0
#         else:
#             return max(self.igre.keys()) + 1

#     def nova_igra(self):
#         self.nalozi_igre_iz_datoteke()
#         id_igre = self.prost_id_igre()
#         igra = nova_igra()
#         self.igre[id_igre] = (igra, ZACETEK)
#         self.zapisi_igre_v_datoteko()
#         return id_igre
        
#     def ugibaj(self, id_igre, crka):
#         self.nalozi_igre_iz_datoteke()
#         igra, _ = self.igre[id_igre]
#         stanje = igra.ugibaj(crka)
#         self.igre[id_igre] = (igra, stanje)
#         self.zapisi_igre_v_datoteko()


#     def zapisi_igre_v_datoteko(self):
#         with open(self.datoteka_s_stanjem, "w", encoding="utf-8") as f:
#             igre = {id_igre: (Besedle.geslo, stanje)
#                 for id_igre, (igra, stanje) in self.igre.items()}
#             json.dump(igre, f)

#     def nalozi_igre_iz_datoteke(self):
#         with open(self.datoteka_s_stanjem, "r", encoding="utf-8") as f:
#             igre = json.load(f)
#             self.igre = {int(id_igre): (Besedle(geslo), stanje)
#                 for id_igre, (geslo, stanje) in igre.items()}