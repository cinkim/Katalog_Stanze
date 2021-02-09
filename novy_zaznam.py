import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W
from tkinter import LEFT, NO, DISABLED, NORMAL
import tkinter.messagebox
import os

def vytvor_top_novy_zaznam(self):
        self.top_novy_zaznam = tk.Toplevel()
        self.top_novy_zaznam.title("Nový záznam")

        self.mezera1 = tk.Label(self.top_novy_zaznam)
        self.mezera1.grid(row=0, column=0)

        # popisky
        self.stanze = tk.Label(self.top_novy_zaznam, text="Nůž/Stanze", width=self.label_width, font="Arial 14", anchor=E)
        self.stanze.grid(row=1, column=0, sticky=E)
        self.nuz = StringVar()
        self.entry_stanze = ttk.Entry(self.top_novy_zaznam, width=self.entry_width_top_novy_zaznam, textvariable=self.nuz)
        self.entry_stanze.config(state=NORMAL)
        self.entry_stanze.grid(row=1, column=1)

        self.konecna_vyska = tk.Label(self.top_novy_zaznam, text="Konečná výška/End Format Höhe", width=self.label_width, font="Arial 14", anchor=E)
        self.konecna_vyska.grid(row=2, column=0, sticky=W)
        self.kv = StringVar()
        self.entry_konecna_vyska = ttk.Entry(self.top_novy_zaznam, width=self.entry_width_top_novy_zaznam, textvariable=self.kv)
        self.entry_konecna_vyska.config(state=NORMAL)
        self.entry_konecna_vyska.grid(row=2, column=1)

        self.konecna_sirka = tk.Label(self.top_novy_zaznam, text="Konečná šířka/End Format Breite", width=self.label_width, font="Arial 14", anchor=E)
        self.konecna_sirka.grid(row=3, column=0, sticky=W)
        self.ks = StringVar()
        self.entry_konecna_sirka = ttk.Entry(self.top_novy_zaznam, width=self.entry_width_top_novy_zaznam, textvariable=self.ks)
        self.entry_konecna_sirka.config(state=NORMAL)
        self.entry_konecna_sirka.grid(row=3, column=1)

        self.otevrena_vyska = tk.Label(self.top_novy_zaznam, text="Otevřená výška/Öfnen Höhe", width=self.label_width, font="Arial 14", anchor=E)
        self.otevrena_vyska.grid(row=4, column=0, sticky=W)
        self.ov = StringVar()
        self.entry_otevrena_vyska = ttk.Entry(self.top_novy_zaznam, width=self.entry_width_top_novy_zaznam, textvariable=self.ov)
        self.entry_otevrena_vyska.config(state=NORMAL)
        self.entry_otevrena_vyska.grid(row=4, column=1)

        self.otevrena_sirka = tk.Label(self.top_novy_zaznam, text="Otevřená šířka/Öfnen Breite", width=self.label_width, font="Arial 14", anchor=E)
        self.otevrena_sirka.grid(row=5, column=0, sticky=W)
        self.os = StringVar()
        self.entry_otevrena_sirka = ttk.Entry(self.top_novy_zaznam, width=self.entry_width_top_novy_zaznam, textvariable=self.os)
        self.entry_otevrena_sirka.config(state=NORMAL)
        self.entry_otevrena_sirka.grid(row=5, column=1)

        self.zaverna_klapka = tk.Label(self.top_novy_zaznam, text="Závěrná klapka/Schlusklappe", width=self.label_width, font="Arial 14", anchor=E)
        self.zaverna_klapka.grid(row=6, column=0, sticky=W)
        self.zk = StringVar()
        self.entry_zaverna_klapka = ttk.Entry(self.top_novy_zaznam, width=self.entry_width_top_novy_zaznam, textvariable=self.zk)
        self.entry_zaverna_klapka.config(state=NORMAL)
        self.entry_zaverna_klapka.grid(row=6, column=1)

        self.prodlouzena_zaverna = tk.Label(self.top_novy_zaznam, text="Prodloužená závěrná/Verlëngerte Schlusklappe", width=self.label_width, font="Arial 14", anchor=E)
        self.prodlouzena_zaverna.grid(row=7, column=0, sticky=W)
        self.pzk = StringVar()
        self.entry_prodlouzena_zaverna = ttk.Entry(self.top_novy_zaznam, width=self.entry_width_top_novy_zaznam, textvariable=self.pzk)
        self.entry_prodlouzena_zaverna.config(state=NORMAL)
        self.entry_prodlouzena_zaverna.grid(row=7, column=1)

        self.spodni_klapka = tk.Label(self.top_novy_zaznam, text="Spodní klapka/Bodenklappe", width=self.label_width, font="Arial 14", anchor=E)
        self.spodni_klapka.grid(row=8, column=0, sticky=W)
        self.sk = StringVar()
        self.entry_spodni_klapka = ttk.Entry(self.top_novy_zaznam, width=self.entry_width_top_novy_zaznam, textvariable=self.sk)
        self.entry_spodni_klapka.config(state=NORMAL)
        self.entry_spodni_klapka.grid(row=8, column=1)

        self.prodlouzena_spodni = tk.Label(self.top_novy_zaznam, text="Prodloužená spodní/Verlëngerte Bodenklappe", width=self.label_width, font="Arial 14", anchor=E)
        self.prodlouzena_spodni.grid(row=9, column=0, sticky=W)
        self.psk = StringVar()
        self.entry_prodlouzena_spodni = ttk.Entry(self.top_novy_zaznam, width=self.entry_width_top_novy_zaznam, textvariable=self.psk)
        self.entry_prodlouzena_spodni.config(state=NORMAL)
        self.entry_prodlouzena_spodni.grid(row=9, column=1)

        self.bocni_leva = tk.Label(self.top_novy_zaznam, text="Boční levá/Seitenklappe L", width=self.label_width, font="Arial 14", anchor=E)
        self.bocni_leva.grid(row=10, column=0, sticky=W)
        self.bl = StringVar()
        self.entry_bocni_leva = ttk.Entry(self.top_novy_zaznam, width=self.entry_width_top_novy_zaznam, textvariable=self.bl)
        self.entry_bocni_leva.config(state=NORMAL)
        self.entry_bocni_leva.grid(row=10, column=1)

        self.bocni_prava = tk.Label(self.top_novy_zaznam, text="Boční pravá/Seitenklappe R", width=self.label_width, font="Arial 14", anchor=E)
        self.bocni_prava.grid(row=11, column=0, sticky=W)
        self.bp = StringVar()
        self.entry_bocni_prava = ttk.Entry(self.top_novy_zaznam, width=self.entry_width_top_novy_zaznam, textvariable=self.bp)
        self.entry_bocni_prava.config(state=NORMAL)
        self.entry_bocni_prava.grid(row=11, column=1)

        self.poznamky = tk.Label(self.top_novy_zaznam, text="Poznámky/Bemerkung", width=self.label_width, font="Arial 14", anchor=E)
        self.poznamky.grid(row=12, column=0, sticky=W)
        self.poz = StringVar()
        self.entry_poznamky = ttk.Entry(self.top_novy_zaznam, width=self.entry_width_top_novy_zaznam, textvariable=self.poz)
        self.entry_poznamky.config(state=NORMAL)
        self.entry_poznamky.grid(row=12, column=1)

        self.var = tk.IntVar()
        self.radio_button = tk.Checkbutton(self.top_novy_zaznam, text="Použitý", variable=self.var)
        self.radio_button.config(state=NORMAL)
        self.radio_button.grid(row=13, column=1, sticky=W)

        self.mezera2 = tk.Label(self.top_novy_zaznam)
        self.mezera2.grid(row=13, column=0)

        self.button_pridej = tk.Button(self.top_novy_zaznam, width=self.label_width, text="Přidej nůž.", command=self.pridat_nuz, font="Arial 14")
        self.button_pridej.grid(row=14, column=0)

        self.button_Konec = tk.Button(self.top_novy_zaznam, text="Konec", width=33, command=self.top_novy_zaznam.destroy, fg="red", font="Arial 14")
        self.button_Konec.grid(row=14, column=1)

def ulozit_novy_nuz(self, cesta_souboru):
    stanze = self.entry_stanze.get()
    if stanze == "":
        tk.messagebox.showwarning("ERROR", "falsche Eingabe\nchyba zadání")
        return
    elif "_" in stanze:
        pass
    elif "/" in stanze:
        stanze = stanze.replace("/", "_")
    else:
        tk.messagebox.showwarning("ERROR", "falsche Eingabe\nchyba zadání")
        return
    konecna_vyska = self.entry_konecna_vyska.get()
    konecna_sirka = self.entry_konecna_sirka.get()
    otevrena_vyska = self.entry_otevrena_vyska.get()
    otevrena_sirka = self.entry_otevrena_sirka.get()
    zaverna_klapka = self.entry_zaverna_klapka.get()
    prodlouzena_zaverna = self.entry_prodlouzena_zaverna.get()
    spodni_klapka = self.entry_spodni_klapka.get()
    prodlouzena_spodni = self.entry_prodlouzena_spodni.get()
    bocni_leva = self.entry_bocni_leva.get()
    bocni_prava = self.entry_bocni_prava.get()
    try:
        prekryti = str(float(spodni_klapka) + float(zaverna_klapka) - float(konecna_vyska))
        poznamky = self.entry_poznamky.get()
        pouzity = self.var.get()
        if pouzity == 0:
            pouzity = "NE"
        else:
            pouzity = "ANO"
        lepidlo_bocni_klapka_venku_1 = str(float(bocni_leva) - 6 + 2)
        lepidlo_bocni_klapka_venku_2 = str(float(spodni_klapka) - 5)
        lepidlo_bocni_venku_X = str(((float(konecna_sirka) / 2)+(float(bocni_leva) / 2 + 6)) * -1)
        lepidlo_bocni_venku_Y = str(float(konecna_vyska) - float(konecna_vyska))
        lepidlo_spodni_klapka_venku_1 = str(float(konecna_sirka) - float(bocni_leva) - float(bocni_prava))
        lepidlo_spodni_klapka_venku_2 = str(float(prekryti) - 5 + 3.5)
        lepidlo_spodni_klapka_venku_X = str(float(konecna_vyska) - float(konecna_vyska))
        lepidlo_spodni_klapka_venku_Y = str(float(spodni_klapka) + 2)
        lepidlo_bocni_klapka_uvnitr_1 = str(float(bocni_leva))
        lepidlo_bocni_klapka_uvnitr_2 = str(float(lepidlo_bocni_klapka_venku_2) - 5)
        lepidlo_bocni_klapka_uvnitr_X = str((float(konecna_sirka) / 2 + 2)-(float(lepidlo_bocni_klapka_uvnitr_1) / 2))
        lepidlo_bocni_klapka_uvnitr_Y = str(float(lepidlo_bocni_klapka_uvnitr_2) + 5)
        lepidlo_zaverna_klapka_uvnitr_1 = str(float(prekryti) + 2)
        lepidlo_zaverna_klapka_uvnitr_2 = str(float(konecna_sirka) - float(bocni_leva) - float(bocni_prava))
        lepidlo_zaverna_klapka_uvnitr_X = str(float(konecna_sirka) - float(konecna_sirka))
        lepidlo_zaverna_klapka_uvnitr_Y = str(float(konecna_vyska) + float(zaverna_klapka) - float(lepidlo_zaverna_klapka_uvnitr_1) + 2) * -1
        bocni_vysekovka_1 = str(float(konecna_sirka) / 2 + float(bocni_leva))
        bocni_vysekovka_2 = str((float(spodni_klapka) - 15) * -1)
        spodni_vysekovka_1 = str(float(konecna_sirka) / 2 - 27)
        spodni_vysekovka_2 = str(float(spodni_klapka))
        simulace = str(2 - float(otevrena_vyska) + float(prekryti))
    except ValueError:
        tk.messagebox.showwarning("ERROR", "falsche Eingabe\nchyba zadání")
        return
    else:
        try:
            with open(cesta_souboru, mode="r", encoding="utf-8") as test_souboru:
                test_souboru = test_souboru.read()
        except FileNotFoundError:
            tk.messagebox.showwarning("ERROR", "Soubor s daty nenalezen")

        else:
            with open(cesta_souboru, mode="a", encoding="utf-8") as pridat:
                print(stanze + ";" + konecna_vyska + ";" + konecna_sirka + ";" + otevrena_vyska + ";" + 
                        otevrena_sirka + ";" + zaverna_klapka + ";" + prodlouzena_zaverna + ";" + spodni_klapka + ";" + prodlouzena_spodni + ";" + 
                        bocni_leva + ";" + bocni_prava + ";" + prekryti + ";" + poznamky + ";" + lepidlo_bocni_klapka_venku_1 + ";" + lepidlo_bocni_klapka_venku_2 + ";" + 
                        lepidlo_bocni_venku_X + ";" + lepidlo_bocni_venku_Y + ";" + lepidlo_spodni_klapka_venku_1 + ";" + lepidlo_spodni_klapka_venku_2 + ";" + 
                        lepidlo_spodni_klapka_venku_X + ";" + lepidlo_spodni_klapka_venku_Y + ";" + lepidlo_bocni_klapka_uvnitr_1 + ";" + lepidlo_bocni_klapka_uvnitr_2 + ";" + 
                        lepidlo_bocni_klapka_uvnitr_X + ";" + lepidlo_bocni_klapka_uvnitr_Y + ";" + lepidlo_zaverna_klapka_uvnitr_1 + ";" + lepidlo_zaverna_klapka_uvnitr_2 + ";" + 
                        lepidlo_zaverna_klapka_uvnitr_X + ";" + lepidlo_zaverna_klapka_uvnitr_Y + ";" + bocni_vysekovka_1 + ";" + bocni_vysekovka_2 + ";" + 
                        spodni_vysekovka_1 + ";" + spodni_vysekovka_2 + ";" + simulace + ";" + pouzity, file=pridat)

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