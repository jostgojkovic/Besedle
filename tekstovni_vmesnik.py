from model import Stanje_crk
from model import Barve
from typing import List
from model import nova_igra


PONOVNI_ZAGON = 'p'
IZHOD = 'i'

NAMIG = 'da'
NE_NAMIG = 'ne'


with open('besede.txt', 'r') as f:
    seznam_besed = [vrstica.strip().upper() for vrstica in f if len(vrstica) == 6]


def igra():
    print('\nDobrodošli v igri Besedle!')
    besedle = nova_igra()
  
    while besedle.lahko_poskusi():
        vnos = input('\nUgib: ')
        if len(vnos) != besedle.DOLZINA_BESEDE:
            print(f'Beseda more bit dolžine {besedle.DOLZINA_BESEDE}!')
            continue
        
        elif vnos.upper() not in seznam_besed:
            print('Ta beseda ni veljavna, poskusi ponovno!')
            continue
        
        besedle.dodaj_poskus(vnos)
        izpisi_rezultat(besedle)

        if besedle.preostali_poskusi() <= 2 and besedle.preostali_poskusi() > 0:
            if besedle.zmaga():
                print('Bravo, uspešno ste končali igro!')
                izberi_ponovitev()
            else:
                namig(besedle)

    if besedle.zmaga():
        print('Bravo, uspešno ste končali igro!')
        izberi_ponovitev()
    else:
        print('\nNi ti uspelo!')
        print(f'Beseda je bila: {besedle.geslo}')
        izberi_ponovitev()


def izpisi_rezultat(besedle):
    print(f'Imaš še toliko poskusov: {besedle.preostali_poskusi()}')
    print('\nTvoji Ugibi: \n')
    for beseda in besedle.poskusi:
        rezultat = besedle.ugibaj(beseda)
        pobarvan_rez = dodaj_barve(rezultat)
        print(pobarvan_rez)
    
    for _ in range(besedle.preostali_poskusi()):
        print(' '.join(['_'] * besedle.DOLZINA_BESEDE))

# def izpisi_rezultat(besedle):
#     # print(f'Imaš še toliko poskusov: {besedle.preostali_poskusi()}')
#     # print('\nTvoji Ugibi: \n')
#     for beseda in besedle.poskusi:
#         rezultat = besedle.ugibaj(beseda)
#         pobarvan_rez = dodaj_barve(rezultat)
#         pobarvan_rez
    
#     for _ in range(besedle.preostali_poskusi()):
#         ' '.join(['_'] * besedle.DOLZINA_BESEDE)



def dodaj_barve(rez: List[Stanje_crk]):
    rez_z_barvo = []
    for crka in rez:
        if crka.v_poziciji:
            barva = Barve.ZELENA
        elif crka.v_besedi:
            barva = Barve.RUMENA
        else:
            barva = Barve.NORMALNA
        pobarvana_crka = barva + crka.znak + Barve.NORMALNA
        rez_z_barvo.append(pobarvana_crka)
    return ' '.join(rez_z_barvo)


def zahtevaj_moznost():
    return input('Vnesite možnost: ')

def ponudi_moznosti():
    text = f'''Vpišite črko za izbor naslednjih možnosti:\n
    {PONOVNI_ZAGON} : ponovni zagon igre\n
    {IZHOD} : izhod
    '''
    return text

def izberi_ponovitev():
    print(ponudi_moznosti())
    moznost = zahtevaj_moznost().strip().lower()
    if moznost == PONOVNI_ZAGON:
        igra()
    else:
        IZHOD

def zahtevaj_namig():
    return input('Ali želite namig? ')

def ponudi_namig():
    text = f'''\nVpišite črko za izbor naslednjih možnosti:\n
    {NAMIG} : Hočem namig\n
    {NE_NAMIG} : Brez namiga
    '''
    return text

def namig(besedle):
    print(ponudi_namig())
    izbira = zahtevaj_namig().strip().lower()
    if izbira == NAMIG:
        print(f'v besedi je črka: {besedle.izberi_namig()}')


igra()
