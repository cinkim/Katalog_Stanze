import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W
from tkinter import LEFT, NO, DISABLED, NORMAL
import tkinter.messagebox
from tkinter import messagebox
import win32com.client as win32

import os

import pandas as pd
import numpy as np

def vytvor_top_katalog_nozu(self):
        self.top_katalog = tk.Toplevel()
        self.top_katalog.title("Stanzmesserliste")

        self.min_vyska_obalky = tk.Label(self.top_katalog, text="Min. End Format Höhe", width=20, font="Arial 8")
        self.min_vyska_obalky.grid(row=0, column=0, sticky=W)
        self.max_vyska_obalky = tk.Label(self.top_katalog, text="Max. End Format Höhe", width=20, font="Arial 8")
        self.max_vyska_obalky.grid(row=0, column=1, sticky=W)

        self.c_noze_Label = tk.Label(self.top_katalog, text="Stanzmesser Nummer", width=20, font="Arial 8")
        self.c_noze_Label.grid(row=0, column=3, sticky=W)
        self.c_noze_Entry = tk.Entry(self.top_katalog, width=20, justify="center")
        self.c_noze_Entry.grid(row=1, column=3, sticky=W)
        self.c_noze_button = tk.Button(self.top_katalog, text="Suchen Stanze", width=17, command=self.najdi_nuz)
        self.c_noze_button.grid(row=2, column=3, sticky=W)

        self.otevri_pdf = tk.Button(self.top_katalog, text="Open PDF", width=17, command=self.otevri_PDF)
        self.otevri_pdf.grid(row=1, column=14, sticky=E)
        self.email = tk.Button(self.top_katalog, text="per E-mail", width=17, command=self.per_email)
        self.email.grid(row=2, column=14, sticky=E)

        self.min_vyska_Entry = tk.Entry(self.top_katalog, width=20, justify="center")
        self.min_vyska_Entry.grid(row=1, column=0, sticky=W)
        self.max_vyska_Entry = tk.Entry(self.top_katalog, width=20, justify="center")
        self.max_vyska_Entry.grid(row=1, column=1, sticky=W)

        self.min_sirka_obalky = tk.Label(self.top_katalog, text="Min. End Format Breite", width=20, font="Arial 8")
        self.min_sirka_obalky.grid(row=2, column=0, sticky=W)
        self.max_sirka_obalky = tk.Label(self.top_katalog, text="Max. End Format Breite", width=20, font="Arial 8")
        self.max_sirka_obalky.grid(row=2, column=1, sticky=W)
        self.min_sirka_Entry = tk.Entry(self.top_katalog, width=20, justify="center")
        self.min_sirka_Entry.grid(row=3, column=0, sticky=W)
        self.max_sirka_Entry = tk.Entry(self.top_katalog, width=20, justify="center")
        self.max_sirka_Entry.grid(row=3, column=1, sticky=W)

        self.min_sk = tk.Label(self.top_katalog, text="Min. Schlusklappe", width=20, font="Arial 8")
        self.min_sk.grid(row=4, column=0, sticky=W)
        self.min_sk_Entry = tk.Entry(self.top_katalog, width=20, justify="center")
        self.min_sk_Entry.grid(row=5, column=0, sticky=W)

        self.max_sk = tk.Label(self.top_katalog, text="Max. Schlusklappe", width=20, font="Arial 8")
        self.max_sk.grid(row=4, column=1, sticky=W)
        self.max_sk_Entry = tk.Entry(self.top_katalog, width=20, justify="center")
        self.max_sk_Entry.grid(row=5, column=1, sticky=W)

        self.vyhledej_noze_Button = tk.Button(self.top_katalog, text="Suchen Format", width=17, command=self.vyhledej_noze)
        self.vyhledej_noze_Button.grid(row=6, column=0, sticky=W)

        self.mezera1 = tk.Label(self.top_katalog, text="    ")
        self.mezera1.grid(row=7, column=0)


        # Seznam zaznamu
        style = ttk.Style(self.top_katalog)
        style.configure("Treeview", rowheight=20)
        self.tree_zaznamy = ttk.Treeview(self.top_katalog, columns=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"), height=20)
        self.tree_zaznamy.grid(row=8, column=0, columnspan=15)

        self.tree_zaznamy.heading("#0", text="ID\n\n")
        self.tree_zaznamy.column("#0", minwidth=0, width=35, stretch=NO, anchor='w')

        self.tree_zaznamy.heading("1", text="Stanze\n\n")
        self.tree_zaznamy.column("1", minwidth=0, width=70, stretch=NO, anchor='center')
  
        self.tree_zaznamy.heading("2", text="EF Höhe\n\n")
        self.tree_zaznamy.column("2", minwidth=0, width=70, stretch=NO, anchor='center')

        self.tree_zaznamy.heading("3", text="EF Breite\n\n")
        self.tree_zaznamy.column("3", minwidth=0, width=70, anchor='center')

        self.tree_zaznamy.heading("4", text="OF Höhe\n\n")
        self.tree_zaznamy.column("4", minwidth=0, width=70, anchor='center')

        self.tree_zaznamy.heading("5", text="OF Breite\n\n")
        self.tree_zaznamy.column("5", minwidth=0, width=70, anchor='center')

        self.tree_zaznamy.heading("6", text="Schlussklappe\n\n")
        self.tree_zaznamy.column("6", minwidth=0, width=90, anchor='center')

        self.tree_zaznamy.heading("7", text="verlängerung\nSchlussklappe\n")
        self.tree_zaznamy.column("7", minwidth=0, width=90, anchor='center')

        self.tree_zaznamy.heading("8", text="Bodenklappe\n\n")        
        self.tree_zaznamy.column("8", minwidth=0, width=90, anchor='center')

        self.tree_zaznamy.heading("9", text="verlängerung\nBodenklappe\n")
        self.tree_zaznamy.column("9", minwidth=0, width=90, anchor='center')

        self.tree_zaznamy.heading("10", text="Sk L\n\n")
        self.tree_zaznamy.column("10", minwidth=0, width=50, anchor='center')

        self.tree_zaznamy.heading("11", text="Sk R\n\n")
        self.tree_zaznamy.column("11", minwidth=0, width=50, anchor='center')

        self.tree_zaznamy.heading("12", text="Überdeckung\n\n")
        self.tree_zaznamy.column("12", minwidth=0, width=80, anchor='center')

        self.tree_zaznamy.heading("13", text="Aktiv\n\n")
        self.tree_zaznamy.column("13", minwidth=0, width=50, anchor='center')

        self.tree_zaznamy.heading("14", text="Bemerkungen\n\n")
        self.tree_zaznamy.column("14", minwidth=0, width=300, anchor='center')
        
        self.button_Konec = tk.Button(self.top_katalog, text="Konec", width=20, command=self.top_katalog.destroy, fg="red")
        self.button_Konec.grid(row=10, column=0, sticky=W)


def PDF_nahled(self, cesta_pro_PDF, nalezeno):
        """
        Otevře pdf v prohlížeči
        data načítá z proměnné NALEZENO
        """
        if self.tree_zaznamy.focus():
            pozice = self.tree_zaznamy.focus()
            pozice = self.tree_zaznamy.item(pozice)
            pozice = pozice["text"]
            pozice = int(pozice)
        projite_pozice = 0
        for cislo_zaznamu in nalezeno:
            if projite_pozice != pozice:
                projite_pozice +=1
            else:
                pdf = cislo_zaznamu[0] + ".pdf"
                pdf = cesta_pro_PDF + pdf
                os.startfile(pdf)
                return

def odeslat(self, cesta_pro_PDF, nalezeno, pozice_k_odeslani):
        """
        Odešle PDF emailem
        data načítá z proměnné NALEZENO
        """
        if self.tree_zaznamy.focus():
                pozice = self.tree_zaznamy.focus()
                pozice = self.tree_zaznamy.item(pozice)
                pozice = pozice["text"]
                pozice = int(pozice)
                prosle = 0
                for qq in nalezeno:
                        if prosle == pozice:
                                self.stanzmesserliste.pozice_k_odeslani.append(qq[0])
                                break
                        else:
                                prosle +=1

                while True:
                        if messagebox.askyesno("???", "Vybrat další:") == True:
                                return
                        else:
                                outlook = win32.Dispatch("outlook.application")
                                mail = outlook.CreateItem(0)
                                mail.subject = "Stanzmesser"
                                for zaznam in pozice_k_odeslani:
                                        pdf = zaznam + ".pdf"
                                        pdf = cesta_pro_PDF + pdf
                                        mail.Attachments.Add(pdf)
                                        mail.Display(False)
                                return



def najdi(self, cesta_souboru):
        """
        Najde nůž podle čísla
        výstup uloží do proměnné NALEZENO
        """
        self.stanzmesserliste.nalezeno = []
        self.stanzmesserliste.pro_zobrazeni = []
        try:
            nuz = self.c_noze_Entry.get()
            if nuz == "":
                tk.messagebox.showwarning("ERROR", "falsche Eingabe\nfehlende Messernummer")
                return
            elif "/" in nuz:
                nuz = nuz.replace("/", "_")
            elif "_" not in nuz:
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

            data = pd.read_csv(cesta_souboru, names=sloupce, dtype=typy, delimiter=";")


            nuz = data[(data["Stanze"] == nuz)]
            nuz.head()

            nalezeno = nuz.values.tolist()
            if nalezeno == []:
                tk.messagebox.showwarning("ERROR", "keine Daten")
                return

        self.stanzmesserliste.pro_zobrazeni = []
        seznam = []
        for nuz in nalezeno:
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
            self.stanzmesserliste.pro_zobrazeni.append(seznam)
        self.stanzmesserliste.nalezeno = self.stanzmesserliste.pro_zobrazeni


        for pot in self.tree_zaznamy.get_children():
            self.tree_zaznamy.delete(pot)

        pozice = 0   
        for Stanze, End_vyska, End_sirka, O_vyska, sirka, Sch_k, PSK, B_K, PBK, L, P, Prek, Bem, POU in self.stanzmesserliste.pro_zobrazeni:
            self.tree_zaznamy.insert("", "end", text=pozice, values=(Stanze, End_vyska, End_sirka, O_vyska,
                sirka, Sch_k, PSK, B_K, PBK, L, P, Prek, Bem, POU))
            pozice += 1
            return

def najdi_noze(self, cesta_souboru):
        """
        najde nože podle rozměrů
        výstup uloží do proměnné NALEZENO
        """
        self.stanzmesserliste.nalezeno = []
        self.stanzmesserliste.pro_zobrazeni = []
        try:
                vyska1 = self.min_vyska_Entry.get()
                vyska2 = self.max_vyska_Entry.get()
                sirka1 = self.min_sirka_Entry.get()
                sirka2 = self.max_sirka_Entry.get()
                SK1 = self.min_sk_Entry.get()
                SK2 = self.max_sk_Entry.get()
                vyska1 = int(vyska1)
                sirka1 = int(sirka1)
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

                data = pd.read_csv(cesta_souboru, names=sloupce, dtype=typy, delimiter=";")

                if vyska2 == "":
                        vyska2 = int(vyska1)
                else:
                        vyska2 = int(vyska2)
                        if vyska2 < vyska1:
                                tk.messagebox.showwarning("ERROR", "falsche Eingabe\nchyba zadání")                   
                                return

                if sirka2 == "":
                        sirka2 = int(sirka1)
                else:
                        sirka2 = int(sirka2)
                        if sirka2 < sirka1:
                                tk.messagebox.showwarning("ERROR", "falsche Eingabe\nchyba zadání")
                                return

                vyska1 = data[(data["End_vyska"] >= vyska1) & (data["End_vyska"] <= vyska2)]
                vyska1.head()

                sirka = vyska1[(vyska1["End_sirka"] >= sirka1) & (vyska1["End_sirka"] <= sirka2)]
                sirka.head()

                if (SK1 == "") and (SK2 == ""):
                        self.stanzmesserliste.nalezeno = sirka.values.tolist()

                        zobrazit = []
                        seznam = []
                        for nuz in self.stanzmesserliste.nalezeno:
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
                                zobrazit.append(seznam)

                        for pot in self.tree_zaznamy.get_children():
                                self.tree_zaznamy.delete(pot)

                        pozice = 0   
                        for Stanze, End_vyska, End_sirka, O_vyska, sirka, Sch_k, PSK, B_K, PBK, L, P, Prek, Bem, POU in zobrazit:
                                self.tree_zaznamy.insert("", "end", text=pozice, values=(Stanze, End_vyska, End_sirka, O_vyska,
                                        sirka, Sch_k, PSK, B_K, PBK, L, P, Prek, Bem, POU))
                                pozice += 1
                        return

                elif (SK1 != "") and (SK2 == ""):
                        SK1 = int(SK1)
                        SK2 = SK1
                        SK = sirka[(sirka["Sch_k"] >= SK1) & (sirka["Sch_k"] <= SK2)]
                        SK.head()
                        self.stanzmesserliste.nalezeno = SK.values.tolist()

                        zobrazit = []
                        seznam = []
                        for nuz in self.stanzmesserliste.nalezeno:
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
                                zobrazit.append(seznam)

                        for pot in self.tree_zaznamy.get_children():
                                self.tree_zaznamy.delete(pot)

                        pozice = 0   
                        for Stanze, End_vyska, End_sirka, O_vyska, sirka, Sch_k, PSK, B_K, PBK, L, P, Prek, Bem, POU in zobrazit:
                                self.tree_zaznamy.insert("", "end", text=pozice, values=(Stanze, End_vyska, End_sirka, O_vyska,
                                        sirka, Sch_k, PSK, B_K, PBK, L, P, Prek, Bem, POU))
                                pozice += 1
                        return

                        for pot in self.tree_zaznamy.get_children():
                                self.tree_zaznamy.delete(pot)

                        pozice = 0   
                        for Stanze, End_vyska, End_sirka, O_vyska, sirka, Sch_k, PSK, B_K, PBK, L, P, Prek, Bem, POU in zobrazit:
                                self.tree_zaznamy.insert("", "end", text=pozice, values=(Stanze, End_vyska, End_sirka, O_vyska,
                                        sirka, Sch_k, PSK, B_K, PBK, L, P, Prek, Bem, POU))
                                pozice += 1
                                return
                
                else:
                        SK1 = int(SK1)
                        SK2 = int(SK2)
                        if SK2 < SK1:
                                tk.messagebox.showwarning("ERROR", "falsche Eingabe\nchyba zadání")
                                return
                        else:
                                SK = sirka[(sirka["Sch_k"] >= SK1) & (sirka["Sch_k"] <= SK2)]
                                SK.head()
                                self.stanzmesserliste.nalezeno = SK.values.tolist()
                                
                                zobrazit = []
                                seznam = []
                                for nuz in self.stanzmesserliste.nalezeno:
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
                                        zobrazit.append(seznam)

                                for pot in self.tree_zaznamy.get_children():
                                        self.tree_zaznamy.delete(pot)

                                pozice = 0   
                                for Stanze, End_vyska, End_sirka, O_vyska, sirka, Sch_k, PSK, B_K, PBK, L, P, Prek, Bem, POU in zobrazit:
                                        self.tree_zaznamy.insert("", "end", text=pozice, values=(Stanze, End_vyska, End_sirka, O_vyska,
                                                sirka, Sch_k, PSK, B_K, PBK, L, P, Prek, Bem, POU))
                                        pozice += 1
                                return


