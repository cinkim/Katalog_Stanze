import csv

import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W
from tkinter import LEFT, NO, DISABLED, NORMAL
import tkinter.messagebox

import os

import win32com.client as win32

import pandas as pd 
import numpy as np

from novy_zaznam import vytvor_top_novy_zaznam
from katalog import vytvor_top_katalog_nozu
from prepress import vytvor_top_souradnic_prepress
from brusici import vytvot_top_brusici
from zmeny import smazat_zaznam, vytvor_top_zmeny, zmeny_v_datech, ulozit_zmeny

class stanzmesserliste:

    def __init__(self):
        self.odemceno = stanzmesserliste.odemknout(self)
        self.cesta_souboru = "D:/Python/Projekty_Python/Katalog_nozu/seznam_nozu_test.csv"
        self.pravda = None
        self.nalezeno = []
        self.pro_zobrazeni = []
        self.cesta_pro_PDF = "D:/Python/Projekty_Python/Katalog_nozu/PDFStanzen/"
        self.stanzmesserliste_prepress = []
        self.cesta_sestavy_Brusici = "D:/Python/Projekty_Python/Katalog_nozu/brusici.csv"
        self.seznamBrusici = []


    def prober_nalezeno(self, nalezeno):
        self.pro_zobrazeni = []
        seznam = []
        for nuz in self.nalezeno:
            seznam = nuz[0:12]
            dalsi1 = str(nuz[34:35])
            dalsi1 = dalsi1.replace("'", "").replace("[", "").replace("]", "")
            seznam.append(dalsi1)
            dalsi2 = str(nuz[12:13])
            if dalsi2 == "[nan]":
                dalsi2 = ""
            else:
                pass
            dalsi2 = dalsi2.replace("'", "").replace("[", "").replace("]", "")
            seznam.append(dalsi2)
            self.pro_zobrazeni.append(seznam)



    def odemknout(self):
        self.uzivatel = os.getenv('username')
        if (self.uzivatel == "fiser") or (self.uzivatel == "bekucad") or (self.uzivatel == "hana.dufkova"):
            self.odemceno = NORMAL
            return self.odemceno
        else:
            self.odemceno = DISABLED
            return self.odemceno


    def pridej_zaznam(self, cesta_souboru, stanze, konecna_vyska, konecna_sirka, otevrena_vyska,
                    otevrena_sirka, zaverna_klapka, prodlouzena_zaverna, spodni_klapka, prodlouzena_spodni,
                    bocni_leva, bocni_prava, prekryti, poznamky, lepidlo_bocni_klapka_venku_1, lepidlo_bocni_klapka_venku_2,
                    lepidlo_bocni_venku_X, lepidlo_bocni_venku_Y, lepidlo_spodni_klapka_venku_1, lepidlo_spodni_klapka_venku_2,
                    lepidlo_spodni_klapka_venku_X, lepidlo_spodni_klapka_venku_Y, lepidlo_bocni_klapka_uvnitr_1, lepidlo_bocni_klapka_uvnitr_2,
                    lepidlo_bocni_klapka_uvnitr_X, lepidlo_bocni_klapka_uvnitr_Y, lepidlo_zaverna_klapka_uvnitr_1, lepidlo_zaverna_klapka_uvnitr_2,
                    lepidlo_zaverna_klapka_uvnitr_X, lepidlo_zaverna_klapka_uvnitr_Y, bocni_vysekovka_1, bocni_vysekovka_2,
                    spodni_vysekovka_1, spodni_vysekovka_2, simulace, pouzity):
        try:
            with open(self.cesta_souboru, mode="r", encoding="utf-8") as test_souboru:
                test_souboru = test_souboru.read()
        except FileNotFoundError:
            tk.messagebox.showwarning("ERROR", "Soubor s daty nenalezen")
            return False
        else:
            with open(self.cesta_souboru, mode="a", encoding="utf-8") as pridat:
                print(stanze + ";" + konecna_vyska + ";" + konecna_sirka + ";" + otevrena_vyska + ";" + 
                        otevrena_sirka + ";" + zaverna_klapka + ";" + prodlouzena_zaverna + ";" + spodni_klapka + ";" + prodlouzena_spodni + ";" + 
                        bocni_leva + ";" + bocni_prava + ";" + prekryti + ";" + poznamky + ";" + lepidlo_bocni_klapka_venku_1 + ";" + lepidlo_bocni_klapka_venku_2 + ";" + 
                        lepidlo_bocni_venku_X + ";" + lepidlo_bocni_venku_Y + ";" + lepidlo_spodni_klapka_venku_1 + ";" + lepidlo_spodni_klapka_venku_2 + ";" + 
                        lepidlo_spodni_klapka_venku_X + ";" + lepidlo_spodni_klapka_venku_Y + ";" + lepidlo_bocni_klapka_uvnitr_1 + ";" + lepidlo_bocni_klapka_uvnitr_2 + ";" + 
                        lepidlo_bocni_klapka_uvnitr_X + ";" + lepidlo_bocni_klapka_uvnitr_Y + ";" + lepidlo_zaverna_klapka_uvnitr_1 + ";" + lepidlo_zaverna_klapka_uvnitr_2 + ";" + 
                        lepidlo_zaverna_klapka_uvnitr_X + ";" + lepidlo_zaverna_klapka_uvnitr_Y + ";" + bocni_vysekovka_1 + ";" + bocni_vysekovka_2 + ";" + 
                        spodni_vysekovka_1 + ";" + spodni_vysekovka_2 + ";" + simulace + ";" + pouzity, file=pridat)

    def zobraz_PDF(self, cesta_pro_PDF, pro_zobrazeni, pozice):
        projite_pozice = 0
        for cislo_zaznamu in pro_zobrazeni:
            if projite_pozice != pozice:
                projite_pozice +=1
            else:
                pdf = cislo_zaznamu[0] + ".pdf"
                pdf = self.cesta_pro_PDF + pdf
                os.startfile(pdf)
                return

    def odesli_PDF(self, cesta_pro_PDF, pro_zobrazeni, pozice):
        projite_pozice = 0
        for cislo_zaznamu in pro_zobrazeni:
            if projite_pozice != pozice:
                projite_pozice +=1
            else:
                pdf = cislo_zaznamu[0] + ".pdf"
                pdf = self.cesta_pro_PDF + pdf
                return pdf




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
        self.brusici = tk.Button(root, text="pro brusírnu\n für Messerschärfer ", state=self.stanzmesserliste.odemceno, font="Arial 14", command=self.vytvot_top_brusici, width=self.entry_width)
        self.brusici.grid(row=6, column=0)
        self.mezera4 = tk.Label()
        self.mezera4.grid(row=7, column=0)
        self.zmena = tk.Button(root, text="změny v datech\n Änderung", state=self.stanzmesserliste.odemceno, font="Arial 14", command=self.zmenavdatech, width=self.entry_width)
        self.zmena.grid(row=8, column=0)
        self.mezera5 = tk.Label()
        self.mezera5.grid(row=9, column=0)
        self.button_Konec = tk.Button(root, text="Konec\n Ende", command=self.on_close, fg="red", font="Arial 14", width=self.entry_width)
        self.button_Konec.grid(row=10, column=0)
        

    def otevri_PDF(self):
       if self.tree_zaznamy.focus():
            pozice = self.tree_zaznamy.focus()
            pozice = self.tree_zaznamy.item(pozice)
            pozice = pozice["text"]
            self.pozice = int(pozice)
            stanzmesserliste.zobraz_PDF(self.stanzmesserliste.cesta_pro_PDF, self.stanzmesserliste.pro_zobrazeni, self.pozice)

    def per_email(self):
        if self.tree_zaznamy.focus():
            pozice = self.tree_zaznamy.focus()
            pozice = self.tree_zaznamy.item(pozice)
            pozice = pozice["text"]
            self.pozice = int(pozice)
            outlook = win32.Dispatch("outlook.application")
            mail = outlook.CreateItem(0)
            mail.subject = "Stanzmesser"
            priloha = stanzmesserliste.odesli_PDF(self.stanzmesserliste.cesta_pro_PDF, self.stanzmesserliste.pro_zobrazeni, self.pozice)
            mail.Attachments.Add(priloha)
            mail.Display(False)

    def najdi_nuz(self):
        try:
            self.nuz = self.c_noze_Entry.get()
            self.nuz = str(self.nuz)
            if self.nuz == "":
                tk.messagebox.showwarning("ERROR", "falsche Eingabe\nfehlende Messernummer")
                return
            elif "/" in self.nuz:
                self.nuz = self.nuz.replace("/", "_")
            elif "_" not in self.nuz:
                tk.messagebox.showwarning("ERROR", "falsche Eingabe\nfehlender Begrenzer '_'")
                return
        except ValueError:
            tk.messagebox.showwarning("ERROR", "falsche Eingabe")
            return
        else:
            sloupce = ["Stanze", "End_vyska", "End_sirka", "O_vyska",
                        "O_sirka", "Sch_k", "PSK", "B_K", "PBK", "L", "P", "Prek", "Bem", "LBKV_1", "LBKV_2", "LBV_X", "LBV_Y", "LSKV_1", "LSKV_2",
                        "LSKV_X", "LSKV_Y", "LBKU_1", "LBKU_2", "LBKU_X", "LBKU_Y", "LZKU_1", "LZKU_2", "LZKU_X", "LZKU_Y", "BV_1", "BV_2",
                        "SV_1", "SV_2", "SIM", "POU"]

            typy = {"Stanze": np.object, "End_vyska": np.int64, "End_sirka": np.int64, "O_vyska": np.float64,
                    "O_sirka": np.float64, "Sch_k": np.float64, "PSK": np.float64, "B_K": np.float64, "PBK": np.float64, "L": np.float64, "P": np.float64,
                    "Prek": np.float64, "Bem": np.object, "LBKV_1": np.float64, "LBKV_2": np.float64, "LBV_X": np.float64, "LBV_Y": np.float64, "LSKV_1": np.float64, "LSKV_2": np.float64,
                    "LSKV_X": np.float64, "LSKV_Y": np.float64, "LBKU_1": np.float64, "LBKU_2": np.float64, "LBKU_X": np.float64, "LBKU_Y": np.float64,
                    "LZKU_1": np.float64, "LZKU_2": np.float64, "LZKU_X": np.float64, "LZKU_Y": np.float64, "BV_1": np.float64, "BV_2": np.float64,
                    "SV_1": np.float64, "SV_2": np.float64, "SIM": np.float64, "POU": np.object}

            data = pd.read_csv(self.stanzmesserliste.cesta_souboru, names=sloupce, dtype=typy, delimiter=";")


            self.nuz = data[(data["Stanze"] == self.nuz)]
            self.nuz.head()

            self.stanzmesserliste.nalezeno = self.nuz.values.tolist()
            if self.stanzmesserliste.nalezeno == []:
                tk.messagebox.showwarning("ERROR", "keine Daten")
                return
            self.zobraz()
            return
    def nuz_prepress(self):
        try:
            self.stanze_prepress = self.c_noze_Entry10.get()
            if self.stanze_prepress == "":
                return
            elif "/" in self.stanze_prepress:
                self.stanze_prepress = self.stanze_prepress.replace("/", "_")
            elif "_" not in self.stanze_prepress:
                tk.messagebox.showwarning("ERROR", "Chybí oddělovač\n '_'")
                return
        except:
            tk.messagebox.showwarning("ERROR", "Nějaká chyba na vstupu.")
            return
        else:
            sloupce = ["Stanze", "End_vyska", "End_sirka", "O_vyska",
                        "O_sirka", "Sch_k", "PSK", "B_K", "PBK", "L", "P", "Prek", "Bem", "LBKV_1", "LBKV_2", "LBV_X", "LBV_Y", "LSKV_1", "LSKV_2",
                        "LSKV_X", "LSKV_Y", "LBKU_1", "LBKU_2", "LBKU_X", "LBKU_Y", "LZKU_1", "LZKU_2", "LZKU_X", "LZKU_Y", "BV_1", "BV_2",
                        "SV_1", "SV_2", "SIM", "POU"]

            typy = {"Stanze": np.object, "End_vyska": np.int64, "End_sirka": np.int64, "O_vyska": np.float64,
                    "O_sirka": np.float64, "Sch_k": np.float64, "PSK": np.float64, "B_K": np.float64, "PBK": np.float64, "L": np.float64, "P": np.float64,
                    "Prek": np.float64, "Bem": np.object, "LBKV_1": np.float64, "LBKV_2": np.float64, "LBV_X": np.float64, "LBV_Y": np.float64, "LSKV_1": np.float64, "LSKV_2": np.float64,
                    "LSKV_X": np.float64, "LSKV_Y": np.float64, "LBKU_1": np.float64, "LBKU_2": np.float64, "LBKU_X": np.float64, "LBKU_Y": np.float64,
                    "LZKU_1": np.float64, "LZKU_2": np.float64, "LZKU_X": np.float64, "LZKU_Y": np.float64, "BV_1": np.float64, "BV_2": np.float64,
                    "SV_1": np.float64, "SV_2": np.float64, "SIM": np.float64, "POU": np.object}

            data = pd.read_csv(self.stanzmesserliste.cesta_souboru, names=sloupce, dtype=typy, delimiter=";")


            self.nalezeno = data[(data["Stanze"] == self.stanze_prepress)]
            self.nalezeno.head()

            self.stanzmesserliste_prepress = self.nalezeno.values.tolist()
            self.zobraz_prepress()
            return

    def zobraz_prepress(self):
        self.koty1_zobraz = []
        self.koty2_zobraz = []
        for qq in self.stanzmesserliste_prepress:
            koty1 = qq[13:21] 
            koty1 = koty1 + (qq[29:33])
            self.koty1_zobraz.append(koty1)
            koty2 = (qq[21:29])
            koty2 = koty2 + (qq[11:12])
            koty2 = koty2 + (qq[33:34])
            self.koty2_zobraz.append(koty2)
            break

        for pot in self.tree_koty1.get_children():
            self.tree_koty1.delete(pot)

        for pot in self.tree_koty2.get_children():
            self.tree_koty2.delete(pot)

        pozice1 = 0   
        for LBKV_1, LBKV_2, LBV_X, LBV_Y, LSKV_1, LSKV_2, LSKV_X, LSKV_Y, BV_1, BV_2, SV_1, SV_2 in self.koty1_zobraz:
            self.tree_koty1.insert("", "end", text=pozice1, values=(LBKV_1, LBKV_2, LBV_X, LBV_Y, LSKV_1, LSKV_2, LSKV_X, 
                LSKV_Y, BV_1, BV_2, SV_1, SV_2))
            pozice1 += 1

        pozice2 = 0   
        for LBKU_1, LBKU_2, LBKU_X, LBKU_Y, LZKU_1, LZKU_2, LZKU_X, LZKU_Y, Prek, Sim in self.koty2_zobraz:
            self.tree_koty2.insert("", "end", text=pozice2, values=(LBKU_1, LBKU_2, LBKU_X, LBKU_Y, LZKU_1, LZKU_2, LZKU_X, LZKU_Y, Prek, Sim))
            pozice2 += 1

    def zmenavdatech(self):
        vytvor_top_zmeny(self)

    def vytvor_top_novy_zaznam(self):
        vytvor_top_novy_zaznam(self)
  
    def vytvor_top_katalog_nozu(self):
        vytvor_top_katalog_nozu(self)

    def vytvor_top_souradnic_prepress(self):
        vytvor_top_souradnic_prepress(self)

    def vytvot_top_brusici(self):
        vytvot_top_brusici(self)
    
    def vyhledej_noze(self):
        try:
            self.vyska1 = self.min_vyska_Entry.get()
            self.vyska2 = self.max_vyska_Entry.get()
            self.sirka1 = self.min_sirka_Entry.get()
            self.sirka2 = self.max_sirka_Entry.get()
            self.SK1 = self.min_sk_Entry.get()
            self.SK2 = self.max_sk_Entry.get()
            self.vyska1 = int(self.vyska1)
            self.sirka1 = int(self.sirka1)
        except ValueError:
            tk.messagebox.showwarning("ERROR", "falsche Eingabe")
            return
        else:
            sloupce = ["Stanze", "End_vyska", "End_sirka", "O_vyska",
                        "O_sirka", "Sch_k", "PSK", "B_K", "PBK", "L", "P", "Prek", "Bem", "LBKV_1", "LBKV_2", "LBV_X", "LBV_Y", "LSKV_1", "LSKV_2",
                        "LSKV_X", "LSKV_Y", "LBKU_1", "LBKU_2", "LBKU_X", "LBKU_Y", "LZKU_1", "LZKU_2", "LZKU_X", "LZKU_Y", "BV_1", "BV_2",
                        "SV_1", "SV_2", "SIM", "POU"]

            typy = {"Stanze": np.object, "End_vyska": np.int64, "End_sirka": np.int64, "O_vyska": np.float64,
                    "O_sirka": np.float64, "Sch_k": np.float64, "PSK": np.float64, "B_K": np.float64, "PBK": np.float64, "L": np.float64, "P": np.float64,
                    "Prek": np.float64, "Bem": np.object, "LBKV_1": np.float64, "LBKV_2": np.float64, "LBV_X": np.float64, "LBV_Y": np.float64, "LSKV_1": np.float64, "LSKV_2": np.float64,
                    "LSKV_X": np.float64, "LSKV_Y": np.float64, "LBKU_1": np.float64, "LBKU_2": np.float64, "LBKU_X": np.float64, "LBKU_Y": np.float64,
                    "LZKU_1": np.float64, "LZKU_2": np.float64, "LZKU_X": np.float64, "LZKU_Y": np.float64, "BV_1": np.float64, "BV_2": np.float64,
                    "SV_1": np.float64, "SV_2": np.float64, "SIM": np.float64, "POU": np.object}

            data = pd.read_csv(self.stanzmesserliste.cesta_souboru, names=sloupce, dtype=typy, delimiter=";")

            if self.vyska2 == "":
                self.vyska2 = int(self.vyska1)
            else:
                self.vyska2 = int(self.vyska2)
                if self.vyska2 < self.vyska1:
                    tk.messagebox.showwarning("ERROR", "falsche Eingabe\nchyba zadání")                   
                    return

            if self.sirka2 == "":
                self.sirka2 = int(self.sirka1)
            else:
                self.sirka2 = int(self.sirka2)
                if self.sirka2 < self.sirka1:
                    tk.messagebox.showwarning("ERROR", "falsche Eingabe\nchyba zadání")
                    return

            self.vyska1 = data[(data["End_vyska"] >= self.vyska1) & (data["End_vyska"] <= self.vyska2)]
            self.vyska1.head()

            self.sirka = self.vyska1[(self.vyska1["End_sirka"] >= self.sirka1) & (self.vyska1["End_sirka"] <= self.sirka2)]
            self.sirka.head()

            if (self.SK1 == "") and (self.SK2 == ""):
                self.stanzmesserliste.nalezeno = self.sirka.values.tolist()
                self.zobraz()
            elif (self.SK1 != "") and (self.SK2 == ""):
                self.SK1 = int(self.SK1)
                self.SK2 = self.SK1
                self.SK = self.sirka[(self.sirka["Sch_k"] >= self.SK1) & (self.sirka["Sch_k"] <= self.SK2)]
                self.SK.head()
                self.stanzmesserliste.nalezeno = self.SK.values.tolist()
                self.zobraz()
                return
            else:
                self.SK1 = int(self.SK1)
                self.SK2 = int(self.SK2)
                if self.SK2 < self.SK1:
                    tk.messagebox.showwarning("ERROR", "falsche Eingabe\nchyba zadání")
                    return
                else:
                    self.SK = self.sirka[(self.sirka["Sch_k"] >= self.SK1) & (self.sirka["Sch_k"] <= self.SK2)]
                    self.SK.head()
                    self.stanzmesserliste.nalezeno = self.SK.values.tolist()
                    self.zobraz()
                    return



    def zobraz(self):
        stanzmesserliste.prober_nalezeno(self)

        for pot in self.tree_zaznamy.get_children():
            self.tree_zaznamy.delete(pot)

        pozice = 0   
        for Stanze, End_vyska, End_sirka, O_vyska, sirka, Sch_k, PSK, B_K, PBK, L, P, Prek, Bem, POU in self.stanzmesserliste.pro_zobrazeni:
            self.tree_zaznamy.insert("", "end", text=pozice, values=(Stanze, End_vyska, End_sirka, O_vyska,
                sirka, Sch_k, PSK, B_K, PBK, L, P, Prek, Bem, POU))
            pozice += 1

    def pridat_nuz(self):
        self.stanze = self.entry_stanze.get()
        if self.stanze == "":
            tk.messagebox.showwarning("ERROR", "falsche Eingabe\nchyba zadání")
            return
        self.konecna_vyska = self.entry_konecna_vyska.get()
        self.konecna_sirka = self.entry_konecna_sirka.get()
        self.otevrena_vyska = self.entry_otevrena_vyska.get()
        self.otevrena_sirka = self.entry_otevrena_sirka.get()
        self.zaverna_klapka = self.entry_zaverna_klapka.get()
        self.prodlouzena_zaverna = self.entry_prodlouzena_zaverna.get()
        self.spodni_klapka = self.entry_spodni_klapka.get()
        self.prodlouzena_spodni = self.entry_prodlouzena_spodni.get()
        self.bocni_leva = self.entry_bocni_leva.get()
        self.bocni_prava = self.entry_bocni_prava.get()
        try:
            self.prekryti = float(self.spodni_klapka) + float(self.zaverna_klapka) - float(self.konecna_vyska)
            self.poznamky = self.entry_poznamky.get()
            self.pouzity = self.var.get()
            if self.pouzity == 0:
                self.pouzity = "NE"
            else:
                self.pouzity = "ANO"
            self.lepidlo_bocni_klapka_venku_1 = float(self.bocni_leva) - 6 + 2
            self.lepidlo_bocni_klapka_venku_2 = float(self.spodni_klapka) - 5
            self.lepidlo_bocni_venku_X = (((float(self.konecna_sirka) / 2)+(float(self.bocni_leva) / 2 + 6)) * -1)
            self.lepidlo_bocni_venku_Y = float(self.konecna_vyska) - float(self.konecna_vyska)
            self.lepidlo_spodni_klapka_venku_1 = float(self.konecna_sirka) - float(self.bocni_leva) - float(self.bocni_prava)
            self.lepidlo_spodni_klapka_venku_2 = float(self.prekryti) - 5 + 3.5 
            self.lepidlo_spodni_klapka_venku_X = float(self.konecna_vyska) - float(self.konecna_vyska)
            self.lepidlo_spodni_klapka_venku_Y = float(self.spodni_klapka) + 2
            self.lepidlo_bocni_klapka_uvnitr_1 = float(self.bocni_leva)
            self.lepidlo_bocni_klapka_uvnitr_2 = float(self.lepidlo_bocni_klapka_venku_2) - 5
            self.lepidlo_bocni_klapka_uvnitr_X = (float(self.konecna_sirka) / 2 + 2)-(float(self.lepidlo_bocni_klapka_uvnitr_1) / 2)
            self.lepidlo_bocni_klapka_uvnitr_Y = float(self.lepidlo_bocni_klapka_uvnitr_2) + 5
            self.lepidlo_zaverna_klapka_uvnitr_1 = float(self.prekryti) + 2
            self.lepidlo_zaverna_klapka_uvnitr_2 = float(self.konecna_sirka) - float(self.bocni_leva) - float(self.bocni_prava)
            self.lepidlo_zaverna_klapka_uvnitr_X = float(self.konecna_sirka) - float(self.konecna_sirka)
            self.lepidlo_zaverna_klapka_uvnitr_Y = (float(self.konecna_vyska) + float(self.zaverna_klapka) - float(self.lepidlo_zaverna_klapka_uvnitr_1) + 2) * -1
            self.bocni_vysekovka_1 = float(self.konecna_sirka) / 2 + float(self.bocni_leva)
            self.bocni_vysekovka_2 = (float(self.spodni_klapka) - 15) * -1
            self.spodni_vysekovka_1 = float(self.konecna_sirka) / 2 - 27
            self.spodni_vysekovka_2 = float(self.spodni_klapka)
            self.simulace = 2 - float(self.otevrena_vyska) + float(self.prekryti)
        except ValueError:
            tk.messagebox.showwarning("ERROR", "falsche Eingabe\nchyba zadání")
            return
        else:
            if self.stanzmesserliste.pridej_zaznam(self, self.stanze, str(self.konecna_vyska), str(self.konecna_sirka), str(self.otevrena_vyska),
                                                str(self.otevrena_sirka), str(self.zaverna_klapka), str(self.prodlouzena_zaverna), str(self.spodni_klapka), str(self.prodlouzena_spodni),
                                                str(self.bocni_leva), str(self.bocni_prava), str(self.prekryti), str(self.poznamky), str(self.lepidlo_bocni_klapka_venku_1), str(self.lepidlo_bocni_klapka_venku_2),
                                                str(self.lepidlo_bocni_venku_X), str(self.lepidlo_bocni_venku_Y), str(self.lepidlo_spodni_klapka_venku_1), str(self.lepidlo_spodni_klapka_venku_2),
                                                str(self.lepidlo_spodni_klapka_venku_X), str(self.lepidlo_spodni_klapka_venku_Y), str(self.lepidlo_bocni_klapka_uvnitr_1), str(self.lepidlo_bocni_klapka_uvnitr_2),
                                                str(self.lepidlo_bocni_klapka_uvnitr_X), str(self.lepidlo_bocni_klapka_uvnitr_Y), str(self.lepidlo_zaverna_klapka_uvnitr_1), str(self.lepidlo_zaverna_klapka_uvnitr_2),
                                                str(self.lepidlo_zaverna_klapka_uvnitr_X), str(self.lepidlo_zaverna_klapka_uvnitr_Y), str(self.bocni_vysekovka_1), str(self.bocni_vysekovka_2),
                                                str(self.spodni_vysekovka_1), str(self.spodni_vysekovka_2), str(self.simulace), self.pouzity) == False:
                return
            else:
                self.nuz.set("")
                self.kv.set("")
                self.ks.set("")
                self.ov.set("")
                self.os.set("")
                self.zk.set("")
                self.pzk.set("")
                self.sk.set("")
                self.psk.set("")
                self.bl.set("")
                self.bp.set("")
                self.poz.set("")
                self.var.set(0)

                tk.messagebox.showwarning("Hotovo", "Nový nůž uložen.")

    def sestava(self):
        try:
            with open(self.stanzmesserliste.cesta_souboru, "r", encoding="utf-8") as soubor:
                soubor = csv.reader(soubor, delimiter=";")
                for radka in soubor:
                    cast = radka[0:11] + radka[12:13]
                    self.stanzmesserliste.seznamBrusici.append(cast)
        except FileNotFoundError:
            tk.messagebox.showwarning("Error", "Soubor, nebo cesta k souboru nenalezena.\n Nebo se jedná o prvotní použití programu.")
            return
        else:
            with open(self.stanzmesserliste.cesta_sestavy_Brusici, mode="w", encoding="ANSI") as brus:
                for rad in self.stanzmesserliste.seznamBrusici:
                    rad = str(rad)
                    rad = rad.replace("[", "").replace("]", "")
                    rad = rad.replace(",", ";").replace("'", "")
                    print(rad, file=brus)
                tk.messagebox.showwarning("ERROR", "Sestava vytvořena")
                return

    def nuz_zmeny(self):
        zmeny_v_datech(self, self.stanzmesserliste.cesta_souboru)

    def uloz_zmeny(self):
        ulozit_zmeny(self, self.stanzmesserliste.cesta_souboru)
     
    def on_close(self):
       self.parent.destroy()

    def smazat(self):
        smazat_zaznam(self, self.stanzmesserliste.cesta_souboru)


    
if __name__ == '__main__':
    root = tk.Tk()
    stanzmesserliste = stanzmesserliste()
    app = stanzmesserlisteGUI(root, stanzmesserliste)
    app.mainloop()

