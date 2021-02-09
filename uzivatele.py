print("Správa uživatelů")
print()
import os
cesta = "D:/Python/Projekty_Python/Katalog_nozu/uzivatele.taj"

def nacti_soubor(cesta):
    try:
        uzivatele = []
        with open(cesta, mode="r", encoding="utf-8") as soubor:
            uzivatele = soubor.read()
            return uzivatele
    except FileNotFoundError:
        with open(cesta, mode="w", encoding="utf-8") as novy_soubor:
            print("Vytvořen nový soubor uživatelů")
    except PermissionError:
        print("Přístup odepřen")
        return
    except:
        print("Neočekávaná chyba")
        return


def volba():
    while True:
        print("Zadej volbu výběru:")
        print()
        print("1 - Zobrazí oktuální uživatele s Admin přístupem:")
        print("2 - Přidá uživatele:")
        print("3 - Smaže uživatele:")
        print("0 - pro ukončení programu:")
        print()

        try:
            volba = int(input("Čekám na tvojí volbu: "))
            if (volba < 0) or (volba > 3):
                print("\nPro tuto volbu není k dispozici žádná funkce: ")
            else:
                return volba
        except ValueError:
            print("\nŠpatné zadání. Prosím zadejte číslo volby: ")


def novy(uzi, cesta):
    nov = input("Zadej nového uživatele podle uživatelského jména v systému Windows: ")
    with open(cesta, mode="a", encoding="utf-8") as soubor2:
        print(nov, file=soubor2)


def smazat(uzi, cesta):
    uzi = uzi.split()
    znovu = "Ano"
    while True:
        pro_vymaz = input("Zadej uživatele pro smazání: ")
        if pro_vymaz not in uzi:
            print("Uživatel nenalezen")
            print("Pro nové zadání stiskněte: a")
            zn = input("Čekám na volbu: ")
            if zn == "a":
                znovu = "Ano"
            else:
                return
        else:
            break
    novy_seznam = []
    for jm in uzi:
        if jm == pro_vymaz:
            pass
        else:
            novy_seznam.append(jm)
    with open(cesta, mode="w", encoding="utf-8") as nov:
        for jmena in novy_seznam:
            print(jmena, file=nov)




def prog():
    while True:
        c_volby = volba()
        if c_volby == 1:
            uzivatel = nacti_soubor(cesta)
            print(uzivatel)
        elif c_volby == 2:
            uzi = nacti_soubor(cesta)
            novy(uzi, cesta)
        elif c_volby == 3:
            uzi = nacti_soubor(cesta)
            smazat(uzi, cesta)
        else:
            input("Ukončuji program: ")
            os._exit(0)
    

prog()