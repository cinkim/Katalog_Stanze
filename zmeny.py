import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W
from tkinter import LEFT, NO, DISABLED, NORMAL
import tkinter.messagebox
import csv

def vytvor_top_zmeny(self):
        self.top_zmeny = tk.Toplevel()
        self.top_zmeny.title("Změny v datech")


        self.c_noze_zmenaL = tk.Label(self.top_zmeny, text="Stanzmesser Nummer", width=20, font="Arial 8")
        self.c_noze_zmenaL.grid(row=0, column=0, sticky=W)
        self.c_noze_zmenaE = tk.Entry(self.top_zmeny, width=20, justify="center")
        self.c_noze_zmenaE.grid(row=1, column=0, sticky=W)
        self.c_noze_zmenaB = tk.Button(self.top_zmeny, text="Suchen Stanze", width=17, command=self.nuz_zmeny)
        self.c_noze_zmenaB.grid(row=2, column=0, sticky=W)
        self.mez1 = tk.Label(self.top_zmeny, text="", width=20, font="Arial 8")
        self.mez1.grid(row=3, column=0, sticky=W)

        
        self.konecna_vyska_zmenaL = tk.Label(self.top_zmeny, text="Konečná výška/End Format Höhe", width=40, font="Arial 14", anchor=E)
        self.konecna_vyska_zmenaL.grid(row=4, column=0, sticky=W)
        self.kv_zmena = StringVar()
        self.entry_konecna_vyska_zmenaE = ttk.Entry(self.top_zmeny, width=40, textvariable=self.kv_zmena)
        self.entry_konecna_vyska_zmenaE.config(state=NORMAL)
        self.entry_konecna_vyska_zmenaE.grid(row=4, column=1)

        self.konecna_sirka_zmenaL = tk.Label(self.top_zmeny, text="Konečná šířka/End Format Breite", width=40, font="Arial 14", anchor=E)
        self.konecna_sirka_zmenaL.grid(row=5, column=0, sticky=W)
        self.ks_zmena = StringVar()
        self.entry_konecna_sirka_zmenaE = ttk.Entry(self.top_zmeny, width=40, textvariable=self.ks_zmena)
        self.entry_konecna_sirka_zmenaE.config(state=NORMAL)
        self.entry_konecna_sirka_zmenaE.grid(row=5, column=1)

        self.otevrena_vyska_zmenaL = tk.Label(self.top_zmeny, text="Otevřená výška/Öfnen Höhe", width=40, font="Arial 14", anchor=E)
        self.otevrena_vyska_zmenaL.grid(row=6, column=0, sticky=W)
        self.ov_zmena = StringVar()
        self.entry_otevrena_vyska_zmenaE = ttk.Entry(self.top_zmeny, width=40, textvariable=self.ov_zmena)
        self.entry_otevrena_vyska_zmenaE.config(state=NORMAL)
        self.entry_otevrena_vyska_zmenaE.grid(row=6, column=1)

        self.otevrena_sirka_zmenaL = tk.Label(self.top_zmeny, text="Otevřená šířka/Öfnen Breite", width=40, font="Arial 14", anchor=E)
        self.otevrena_sirka_zmenaL.grid(row=7, column=0, sticky=W)
        self.os_zmena = StringVar()
        self.entry_otevrena_sirka_zmenaE = ttk.Entry(self.top_zmeny, width=40, textvariable=self.os_zmena)
        self.entry_otevrena_sirka_zmenaE.config(state=NORMAL)
        self.entry_otevrena_sirka_zmenaE.grid(row=7, column=1)

        self.zaverna_klapka_zmenaL = tk.Label(self.top_zmeny, text="Závěrná klapka/Schlusklappe", width=40, font="Arial 14", anchor=E)
        self.zaverna_klapka_zmenaL.grid(row=8, column=0, sticky=W)
        self.zk_zmena = StringVar()
        self.entry_zaverna_klapka_zmenaE = ttk.Entry(self.top_zmeny, width=40, textvariable=self.zk_zmena)
        self.entry_zaverna_klapka_zmenaE.config(state=NORMAL)
        self.entry_zaverna_klapka_zmenaE.grid(row=8, column=1)

        self.prodlouzena_zaverna_zmenaL = tk.Label(self.top_zmeny, text="Prodloužená závěrná/Verlëngerte Schlusklappe", width=40, font="Arial 14", anchor=E)
        self.prodlouzena_zaverna_zmenaL.grid(row=9, column=0, sticky=W)
        self.pzk_zmena = StringVar()
        self.entry_prodlouzena_zaverna_zmenaE = ttk.Entry(self.top_zmeny, width=40, textvariable=self.pzk_zmena)
        self.entry_prodlouzena_zaverna_zmenaE.config(state=NORMAL)
        self.entry_prodlouzena_zaverna_zmenaE.grid(row=9, column=1)

        self.spodni_klapka_zmenaL = tk.Label(self.top_zmeny, text="Spodní klapka/Bodenklappe", width=40, font="Arial 14", anchor=E)
        self.spodni_klapka_zmenaL.grid(row=10, column=0, sticky=W)
        self.sk_zmena = StringVar()
        self.entry_spodni_klapka_zmenaE = ttk.Entry(self.top_zmeny, width=40, textvariable=self.sk_zmena)
        self.entry_spodni_klapka_zmenaE.config(state=NORMAL)
        self.entry_spodni_klapka_zmenaE.grid(row=10, column=1)

        self.prodlouzena_spodni_zmenaL = tk.Label(self.top_zmeny, text="Prodloužená spodní/Verlëngerte Bodenklappe", width=40, font="Arial 14", anchor=E)
        self.prodlouzena_spodni_zmenaL.grid(row=11, column=0, sticky=W)
        self.psk_zmena = StringVar()
        self.entry_prodlouzena_spodni_zmenaE = ttk.Entry(self.top_zmeny, width=40, textvariable=self.psk_zmena)
        self.entry_prodlouzena_spodni_zmenaE.config(state=NORMAL)
        self.entry_prodlouzena_spodni_zmenaE.grid(row=11, column=1)

        self.bocni_leva_zmenaL = tk.Label(self.top_zmeny, text="Boční levá/Seitenklappe L", width=40, font="Arial 14", anchor=E)
        self.bocni_leva_zmenaL.grid(row=12, column=0, sticky=W)
        self.bl_zmena = StringVar()
        self.entry_bocni_leva_zmenaE = ttk.Entry(self.top_zmeny, width=40, textvariable=self.bl_zmena)
        self.entry_bocni_leva_zmenaE.config(state=NORMAL)
        self.entry_bocni_leva_zmenaE.grid(row=12, column=1)

        self.bocni_prava_zmenaL = tk.Label(self.top_zmeny, text="Boční pravá/Seitenklappe R", width=40, font="Arial 14", anchor=E)
        self.bocni_prava_zmenaL.grid(row=13, column=0, sticky=W)
        self.bp_zmena = StringVar()
        self.entry_bocni_prava_zmenaE = ttk.Entry(self.top_zmeny, width=40, textvariable=self.bp_zmena)
        self.entry_bocni_prava_zmenaE.config(state=NORMAL)
        self.entry_bocni_prava_zmenaE.grid(row=13, column=1)

        self.poznamky_zmenaL = tk.Label(self.top_zmeny, text="Poznámky/Bemerkung", width=40, font="Arial 14", anchor=E)
        self.poznamky_zmenaL.grid(row=14, column=0, sticky=W)
        self.poz_zmena = StringVar()
        self.entry_poznamky_zmenaE = ttk.Entry(self.top_zmeny, width=70, textvariable=self.poz_zmena)
        self.entry_poznamky_zmenaE.config(state=NORMAL)
        self.entry_poznamky_zmenaE.grid(row=14, column=1)


        self.button_Konec = tk.Button(self.top_zmeny, text="Konec", width=17, command=self.top_zmeny.destroy, fg="red")
        self.button_Konec.grid(row=15, column=0, sticky=W)

def zmeny_v_datech(self):
        nuz = self.c_noze_zmenaE.get()
        if "_" in nuz:
                pass
        elif "/" in nuz:
                nuz = nuz.replace("/", "_")
        else:
                return

        seznam_nozu = []
        with open("D:/Python/Projekty_Python/Katalog_nozu/seznam_nozu_test.csv", mode="r", encoding="utf-8") as noze:
                noze = csv.reader(noze, delimiter=";")
                for radka in noze:
                        if radka[0] != nuz:
                                seznam_nozu.append(radka)
                        else:
                                self.kv_zmena.set(radka[1])
                                self.ks_zmena.set(radka[2])
                                self.ov_zmena.set(radka[3])
                                self.os_zmena.set(radka[4])
                                self.zk_zmena.set(radka[5])
                                self.pzk_zmena.set(radka[6])
                                self.sk_zmena.set(radka[7])
                                self.psk_zmena.set(radka[8])
                                self.bl_zmena.set(radka[9])
                                self.bp_zmena.set(radka[10])
                                self.poz_zmena.set(radka[12])
                                nuz = nuz
                                kv = self.entry_konecna_vyska_zmenaE.get()
                                ks = self.entry_konecna_sirka_zmenaE.get()
                                ov = self.entry_otevrena_vyska_zmenaE.get()
                                os = self.entry_otevrena_sirka_zmenaE.get()
                                zk = self.entry_zaverna_klapka_zmenaE.get()
                                pzk = self.entry_prodlouzena_zaverna_zmenaE.get()
                                sp = self.entry_spodni_klapka_zmenaE.get()
                                psk = self.entry_prodlouzena_spodni_zmenaE.get()
                                bl = self.entry_bocni_leva_zmenaE.get()
                                bp = self.entry_bocni_prava_zmenaE.get()
                                poz = self.entry_poznamky_zmenaE.get()


                                try:
                                        prekryti = float(sk) + float(zk) - float(kv)
                                        lepidlo_bocni_klapka_venku_1 = float(bl) - 6 + 2
                                        lepidlo_bocni_klapka_venku_2 = float(sk) - 5
                                        lepidlo_bocni_venku_X = (((float(ks) / 2)+(float(bl) / 2 + 6)) * -1)
                                        lepidlo_bocni_venku_Y = float(kv) - float(kv)
                                        lepidlo_spodni_klapka_venku_1 = float(ks) - float(bl) - float(bp)
                                        lepidlo_spodni_klapka_venku_2 = float(prekryti) - 5 + 3.5 
                                        lepidlo_spodni_klapka_venku_X = float(kv) - float(kv)
                                        lepidlo_spodni_klapka_venku_Y = float(sk) + 2
                                        lepidlo_bocni_klapka_uvnitr_1 = float(bl)
                                        lepidlo_bocni_klapka_uvnitr_2 = float(lepidlo_bocni_klapka_venku_2) - 5
                                        lepidlo_bocni_klapka_uvnitr_X = (float(ks) / 2 + 2)-(float(lepidlo_bocni_klapka_uvnitr_1) / 2)
                                        lepidlo_bocni_klapka_uvnitr_Y = float(lepidlo_bocni_klapka_uvnitr_2) + 5
                                        lepidlo_zaverna_klapka_uvnitr_1 = float(prekryti) + 2
                                        lepidlo_zaverna_klapka_uvnitr_2 = float(ks) - float(bl) - float(bp)
                                        lepidlo_zaverna_klapka_uvnitr_X = float(ks) - float(ks)
                                        lepidlo_zaverna_klapka_uvnitr_Y = (float(kv) + float(zk) - float(lepidlo_zaverna_klapka_uvnitr_1) + 2) * -1
                                        bocni_vysekovka_1 = float(ks) / 2 + float(bl)
                                        bocni_vysekovka_2 = (float(sk) - 15) * -1
                                        podni_vysekovka_1 = float(ks) / 2 - 27
                                        spodni_vysekovka_2 = float(sk)
                                        simulace = 2 - float(ov) + float(prekryti)
                                except ValueError:
                                        tk.messagebox.showwarning("ERROR", "falsche Eingabe\nchyba zadání")
                                        return
                                else:
                                        pozmene = nuz+";"+kv+";"+ks+";"+ov+";"+os+";"+zk+";"+pzk+";"+sk+";"
                                        +psk+";"+bl+";"+bp+";"+poz+";"+str(prekryti)+";"+str(lepidlo_bocni_klapka_venku_1)+";"
                                        +str(lepidlo_bocni_klapka_venku_2)+";"+str(lepidlo_bocni_venku_X)+";"+str(lepidlo_bocni_venku_Y)+";"
                                        +str(lepidlo_spodni_klapka_venku_1)+";"+str(lepidlo_spodni_klapka_venku_2)+";"+str(lepidlo_spodni_klapka_venku_X)+";"
                                        +str(lepidlo_spodni_klapka_venku_Y)+";"+str(lepidlo_bocni_klapka_uvnitr_1)+";"+str(lepidlo_bocni_klapka_uvnitr_2)+";"
                                        +str(lepidlo_bocni_klapka_uvnitr_X)+";"+str(lepidlo_bocni_klapka_uvnitr_Y)+";"+str(lepidlo_zaverna_klapka_uvnitr_1)+";"
                                        +str(lepidlo_zaverna_klapka_uvnitr_2)+";"+str(lepidlo_zaverna_klapka_uvnitr_X)+";"+str(lepidlo_zaverna_klapka_uvnitr_Y)+";"
                                        +str(bocni_vysekovka_1)+";"+str(bocni_vysekovka_2)+";"+str(podni_vysekovka_1)+";"+str(spodni_vysekovka_2)+str(simulace)+";"
                                        +"ANO"
                                        print(pozmene)
                                                
                                """
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

                                tk.messagebox.showwarning("Hotovo", "Změna uložena.")
                                """




                                
