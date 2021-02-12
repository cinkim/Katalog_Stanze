import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W
from tkinter import LEFT, NO, DISABLED, NORMAL
import tkinter.messagebox

import csv

import pandas as pd 
import numpy as np

def vytvor_top_souradnic_prepress(self):
        self.top_souradnice = tk.Toplevel()
        self.top_souradnice.title("Souřadnice Prepress")


        self.c_noze_Label10 = tk.Label(self.top_souradnice, text="Stanzmesser Nummer", width=20, font="Arial 8")
        self.c_noze_Label10.grid(row=0, column=0, sticky=W)
        self.c_noze_Entry10 = tk.Entry(self.top_souradnice, width=20, justify="center")
        self.c_noze_Entry10.grid(row=1, column=0, sticky=W)
        self.c_noze_button10 = tk.Button(self.top_souradnice, text="Suchen Stanze", width=17, command=self.nuz_prepress)
        self.c_noze_button10.grid(row=2, column=0, sticky=W)
        self.c_noze_Label11 = tk.Label(self.top_souradnice, text="", width=20, font="Arial 8")
        self.c_noze_Label11.grid(row=3, column=0, sticky=W)

        # Seznam zaznamu
        style = ttk.Style(self.top_souradnice)
        style.configure("Treeview", rowheight=20, font="Arial 10")
        self.tree_koty1 = ttk.Treeview(self.top_souradnice, columns=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"), height=1)
        self.tree_koty1.grid(row=4, column=0, columnspan=13)

        self.tree_koty1.heading("#0", text="ID\n\n\n")
        self.tree_koty1.column("#0", minwidth=0, width=35, stretch=NO, anchor='w')

        self.tree_koty1.heading("1", text="Rozměr\n lepidla\n boční\n      X")
        self.tree_koty1.column("1", minwidth=0, width=70, stretch=NO, anchor='center')
  
        self.tree_koty1.heading("2", text="Rozměr\n lepidla\n boční\n     Y")
        self.tree_koty1.column("2", minwidth=0, width=70, stretch=NO, anchor='center')

        self.tree_koty1.heading("3", text="Pozice\n lepidla\n boční\n     X")
        self.tree_koty1.column("3", minwidth=0, width=70, anchor='center')

        self.tree_koty1.heading("4", text="Pozice\n lepidla\n boční\n     Y")
        self.tree_koty1.column("4", minwidth=0, width=70, anchor='center')

        self.tree_koty1.heading("5", text="Rozměr\n lepidla\n spodní\n     X")
        self.tree_koty1.column("5", minwidth=0, width=70, anchor='center')

        self.tree_koty1.heading("6", text="Rozměr\n lepidla\n spodní\n     Y")
        self.tree_koty1.column("6", minwidth=0, width=70, anchor='center')

        self.tree_koty1.heading("7", text="Pozice\nlepidla\nspodní\n     X")
        self.tree_koty1.column("7", minwidth=0, width=70, anchor='center')

        self.tree_koty1.heading("8", text="Pozice\nlepidla\nspodní\n     Y")        
        self.tree_koty1.column("8", minwidth=0, width=70, anchor='center')

        self.tree_koty1.heading("9", text="   Boční\nvýsekovky\n\n       X")
        self.tree_koty1.column("9", minwidth=0, width=70, anchor='center')

        self.tree_koty1.heading("10", text="   Boční\nvýsekovky\n\n       Y")
        self.tree_koty1.column("10", minwidth=0, width=70, anchor='center')

        self.tree_koty1.heading("11", text="  Spodní\nvýsekovky\n\n       X")
        self.tree_koty1.column("11", minwidth=0, width=70, anchor='center')

        self.tree_koty1.heading("12", text="  Spodní\nvýsekovky\n\n       Y")
        self.tree_koty1.column("12", minwidth=0, width=70, anchor='center')

        self.c_noze_Label12 = tk.Label(self.top_souradnice, text="", width=20, font="Arial 8")
        self.c_noze_Label12.grid(row=5, column=0, sticky=W)


        self.tree_koty2 = ttk.Treeview(self.top_souradnice, columns=("21", "22", "23", "24", "25", "26", "27", "28", "29", "30"), height=1)
        self.tree_koty2.grid(row=6, column=0, columnspan=13)

        self.tree_koty2.heading("#0", text="ID\n\n\n")
        self.tree_koty2.column("#0", minwidth=0, width=35, stretch=NO, anchor='w')

        self.tree_koty2.heading("21", text="   Rozměr\n    lepidla\nzadní boční\n       X")
        self.tree_koty2.column("21", minwidth=0, width=70, stretch=NO, anchor='center')
  
        self.tree_koty2.heading("22", text="   Rozměr\n    lepidla\nzadní boční\n        Y")
        self.tree_koty2.column("22", minwidth=0, width=70, stretch=NO, anchor='center')

        self.tree_koty2.heading("23", text="   Pozice\n    lepidla\nzadní boční\n        X")
        self.tree_koty2.column("23", minwidth=0, width=70, anchor='center')

        self.tree_koty2.heading("24", text="   Pozice\n    lepidla\nzadní boční\n        Y")
        self.tree_koty2.column("24", minwidth=0, width=70, anchor='center')

        self.tree_koty2.heading("25", text="   Rozměr\n    lepidla\nzadní spodní\n        X")
        self.tree_koty2.column("25", minwidth=0, width=80, anchor='center')

        self.tree_koty2.heading("26", text="   Rozměr\n    lepidla\nzadní spodní\n        Y")
        self.tree_koty2.column("26", minwidth=0, width=80, anchor='center')

        self.tree_koty2.heading("27", text="   Pozice\n    lepidla\nzadní spodní\n        X")
        self.tree_koty2.column("27", minwidth=0, width=80, anchor='center')

        self.tree_koty2.heading("28", text="   Pozice\n    lepidla\nzadní spodní\n        Y")        
        self.tree_koty2.column("28", minwidth=0, width=80, anchor='center')

        self.tree_koty2.heading("29", text="Překrytí\n\n\n")        
        self.tree_koty2.column("29", minwidth=0, width=80, anchor='center')

        self.tree_koty2.heading("30", text="Simulace\n\n\n")        
        self.tree_koty2.column("30", minwidth=0, width=80, anchor='center')

        self.c_noze_mezera = tk.Label(self.top_souradnice, text="", width=20, font="Arial 8")
        self.c_noze_mezera.grid(row=7, column=0, sticky=W)


        self.button_Konec = tk.Button(self.top_souradnice, text="Konec", width=17, command=self.top_souradnice.destroy, fg="red")
        self.button_Konec.grid(row=8, column=0, sticky=W)

def nuzproprepress(self, cesta_souboru):
        try:
            stanze_prepress = self.c_noze_Entry10.get()
            if stanze_prepress == "":
                return
            elif "/" in stanze_prepress:
                stanze_prepress = stanze_prepress.replace("/", "_")
            elif "_" not in stanze_prepress:
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

            try:
                data = pd.read_csv(cesta_souboru, names=sloupce, dtype=typy, delimiter=";")
            except FileNotFoundError:
                tk.messagebox.showwarning("ERROR", "Soubor s daty nenalezen")
            except PermissionError:
                tk.messagebox.showwarning("ERROR", "Přístup odepřen.")
            else:
                nalezeno = data[(data["Stanze"] == stanze_prepress)]
                nalezeno.head()
                stanzmesserliste_prepress = nalezeno.values.tolist()
                
        koty1_zobraz = []
        koty2_zobraz = []
        for qq in stanzmesserliste_prepress:
            koty1 = qq[13:21] 
            koty1 = koty1 + (qq[29:33])
            koty1_zobraz.append(koty1)
            koty2 = (qq[21:29])
            koty2 = koty2 + (qq[11:12])
            koty2 = koty2 + (qq[33:34])
            koty2_zobraz.append(koty2)
            break

        for pot in self.tree_koty1.get_children():
            self.tree_koty1.delete(pot)

        for pot in self.tree_koty2.get_children():
            self.tree_koty2.delete(pot)

        pozice1 = 0   
        for LBKV_1, LBKV_2, LBV_X, LBV_Y, LSKV_1, LSKV_2, LSKV_X, LSKV_Y, BV_1, BV_2, SV_1, SV_2 in koty1_zobraz:
            self.tree_koty1.insert("", "end", text=pozice1, values=(LBKV_1, LBKV_2, LBV_X, LBV_Y, LSKV_1, LSKV_2, LSKV_X, 
                LSKV_Y, BV_1, BV_2, SV_1, SV_2))
            pozice1 += 1

        pozice2 = 0   
        for LBKU_1, LBKU_2, LBKU_X, LBKU_Y, LZKU_1, LZKU_2, LZKU_X, LZKU_Y, Prek, Sim in koty2_zobraz:
            self.tree_koty2.insert("", "end", text=pozice2, values=(LBKU_1, LBKU_2, LBKU_X, LBKU_Y, LZKU_1, LZKU_2, LZKU_X, LZKU_Y, Prek, Sim))
            pozice2 += 1
            return