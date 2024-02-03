import math

def hae_asematiedot(tiedosto:str ):

    file = open(tiedosto, 'r')
    firstline = file.readline()
    fline = firstline.split(';')

    asemat = {}
    for line in file:
        line = line.rstrip()
        rivi = line.split(';')
        sijainti = rivi[3]
        longitude = rivi[0]
        latitude = rivi[1]
        tuple = (longitude, latitude)
        asemat[sijainti] = tuple

    return asemat


def etaisyys(asemat: dict, asema1:str, asema2:str):

    longitude1 = asemat[asema1][0]
    longitude1 = float(longitude1)
    longitude2 = asemat[asema2][0]
    longitude2 = float(longitude2)
    latitude1 = asemat[asema1][1]
    latitude1 = float(latitude1)
    latitude2 = asemat[asema2][1]
    latitude2 = float(latitude2)

    #laskutoimitus

    x_kilometreina = (longitude1 - longitude2) * 55.26
    y_kilometreina = (latitude1 - latitude2) * 111.2
    etaisyys = math.sqrt(x_kilometreina ** 2 + y_kilometreina ** 2)

    return etaisyys

def suurin_etaisyys(asemat:dict):
    suurin = 0
    for asema1 in asemat:
        for asema2 in asemat:
            maks_etaisyys = etaisyys(asemat, asema1, asema2)
            if maks_etaisyys > suurin:
                suurin = maks_etaisyys
                tulos = (asema1, asema2, suurin)
            else:
                continue

    return tulos



if __name__ ==  "__main__":
    asemat = hae_asematiedot('stations1.txt')
    asema1, asema2, suurin = suurin_etaisyys(asemat)
    print(asema1, asema2, suurin)