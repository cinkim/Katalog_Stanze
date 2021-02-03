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