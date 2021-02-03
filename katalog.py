import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W
from tkinter import LEFT, NO, DISABLED, NORMAL
import tkinter.messagebox
import win32com.client as win32

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

        self.tree_zaznamy.heading("13", text="Akviv\n\n")
        self.tree_zaznamy.column("13", minwidth=0, width=50, anchor='center')

        self.tree_zaznamy.heading("14", text="Bemerkungen\n\n")
        self.tree_zaznamy.column("14", minwidth=0, width=300, anchor='center')
        
        self.button_Konec = tk.Button(self.top_katalog, text="Konec", width=20, command=self.top_katalog.destroy, fg="red")
        self.button_Konec.grid(row=10, column=0, sticky=W)

