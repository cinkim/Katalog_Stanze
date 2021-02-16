
import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W
from tkinter import LEFT, NO, DISABLED, NORMAL
import tkinter.messagebox
import os
import sys

import novy_zaznam as nz
import katalog as kat
import prepress as pr
import brusici as br
import zmeny as zm


class stanzmesserliste:

    def __init__(self):
        self.cesta_souboru = "seznam_nozu_test.csv"
        self.cesta_prava = "uzivatele.taj"
        self.cestaPDF = "cestaPDFsoubory.txt"
        self.uzivatele_admin = []
        # self.pravda = None
        self.pro_zobrazeni = []
        self.pozice_k_odeslani = []
        self.cesta_pro_PDF = stanzmesserliste.cesta_k_PDF(self, self.cestaPDF)
        self.cesta_sestavy_Brusici = "C:/Brusici/brusici.csv"
        self.nalezeno = []
        self.overeni(self.cesta_prava)
        self.odemceno = stanzmesserliste.odemknout(self)


    def cesta_k_PDF(self, cestaPDF):
        with open(cestaPDF, mode="r", encoding="utf-8") as cesta:
            cesta = cesta.read()
            return cesta

    def overeni(self, cesta_prava):
        with open(cesta_prava, mode="r", encoding="utf-8") as soubor:
            uzivatele_admin = soubor.read()
            self.uzivatele_admin = uzivatele_admin.split()
            return 

    def odemknout(self):
        self.uzivatel = os.getenv('username')
        if self.uzivatel in self.uzivatele_admin:
            self.odemceno = NORMAL
            return self.odemceno
        else:
            self.odemceno = DISABLED
            return self.odemceno



class stanzmesserlisteGUI(tk.Frame):

    def __init__(self, parent, stanzmesserliste):
        super().__init__(parent)
        self.parent = parent
        self.stanzmesserliste = stanzmesserliste
        self.parent.title("Stanzmesserliste")
        self.entry_width = 40
        self.label_width = 40
        self.entry_width_top_novy_zaznam = 60
        self.parent.protocol("WM_DELETE_WINDOW", self.on_close)
        self.create_widgets()


    def create_widgets(self):
        self.pridat = tk.Button(root, text="Přidat záznam\n neu Stanzmesser", font="Arial 14", state=self.stanzmesserliste.odemceno, command=self.vytvor_top_novy_zaznam, width=self.entry_width)
        self.pridat.grid(row=0, column=0)
        self.mezera1 = tk.Label()
        self.mezera1.grid(row=1, column=0)
        self.katalog = tk.Button(root, text="Katalog\n Verzeichnis", font="Arial 14", state=NORMAL, command=self.vytvor_top_katalog_nozu, width=self.entry_width)
        self.katalog.grid(row=2, column=0)
        self.mezera2 = tk.Label()
        self.mezera2.grid(row=3, column=0)
        self.prepress = tk.Button(root, text="souřadnice Prepress\n für Prepress", state=self.stanzmesserliste.odemceno, font="Arial 14", command=self.vytvor_top_souradnic_prepress, width=self.entry_width)
        self.prepress.grid(row=4, column=0)
        self.mezera3 = tk.Label()
        self.mezera3.grid(row=5, column=0)
        self.brusici = tk.Button(root, text="pro brusírnu\n für Messerschärfer ", state=NORMAL, font="Arial 14", command=self.vytvot_top_brusici, width=self.entry_width)
        self.brusici.grid(row=6, column=0)
        self.mezera4 = tk.Label()
        self.mezera4.grid(row=7, column=0)
        self.zmena = tk.Button(root, text="změny v datech\n Änderung", state=self.stanzmesserliste.odemceno, font="Arial 14", command=self.zmenavdatech, width=self.entry_width)
        self.zmena.grid(row=8, column=0)
        self.mezera5 = tk.Label()
        self.mezera5.grid(row=9, column=0)
        self.button_Konec = tk.Button(root, text="Konec\n Ende", command=self.on_close, fg="red", font="Arial 14", width=self.entry_width)
        self.button_Konec.grid(row=10, column=0)
        

    # příkazy okna katalog

    def vyhledej_noze(self):
        kat.najdi_noze(self, self.stanzmesserliste.cesta_souboru)

    def najdi_nuz(self):
        kat.najdi(self, self.stanzmesserliste.cesta_souboru)

    def vytvor_top_katalog_nozu(self):
        kat.vytvor_top_katalog_nozu(self)

    def per_email(self):
        kat.odeslat(self, self.stanzmesserliste.cesta_pro_PDF, self.stanzmesserliste.nalezeno, self.stanzmesserliste.pozice_k_odeslani)

    def otevri_PDF(self):
       kat.PDF_nahled(self, self.stanzmesserliste.cesta_pro_PDF, self.stanzmesserliste.nalezeno)


  
    # příkazy okna prepress
    def nuz_prepress(self):
        pr.nuzproprepress(self, self.stanzmesserliste.cesta_souboru)

    def vytvor_top_souradnic_prepress(self):
        pr.vytvor_top_souradnic_prepress(self)

    

    # příkazy okna nový záznam
    def pridat_nuz(self):
        nz.ulozit_novy_nuz(self, self.stanzmesserliste.cesta_souboru)

    def vytvor_top_novy_zaznam(self):
        nz.vytvor_top_novy_zaznam(self)



    # příkazy okna brusiči
    def vytvot_top_brusici(self):
        br.vytvot_top_brusici(self)

    def sestava(self):
        br.vytvor_sestavu(self, self.stanzmesserliste.cesta_souboru, self.stanzmesserliste.cesta_sestavy_Brusici)



    # příkazy okna změny
    def zmenavdatech(self):
        zm.vytvor_top_zmeny(self)

    def nuz_zmeny(self):
        zm.zmeny_v_datech(self, self.stanzmesserliste.cesta_souboru)

    def uloz_zmeny(self):
        zm.ulozit_zmeny(self, self.stanzmesserliste.cesta_souboru)
     
    def smazat(self):
        zm.smazat_zaznam(self, self.stanzmesserliste.cesta_souboru)


    # zavřít
    def on_close(self):
       self.parent.destroy()


    
if __name__ == '__main__':
    root = tk.Tk()
    stanzmesserliste = stanzmesserliste()
    app = stanzmesserlisteGUI(root, stanzmesserliste)
    app.mainloop()

