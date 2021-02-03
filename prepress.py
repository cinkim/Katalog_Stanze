import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W
from tkinter import LEFT, NO, DISABLED, NORMAL
import tkinter.messagebox

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