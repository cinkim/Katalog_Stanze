import tkinter as tk
from tkinter import ttk, StringVar, NORMAL, CENTER, N, S, E, W
from tkinter import LEFT, NO, DISABLED, NORMAL
import tkinter.messagebox

def vytvot_top_brusici(self):
        self.top_brusici = tk.Toplevel()
        self.top_brusici.title("Sestava brusiči")
        self.mez1 = tk.Label(self.top_brusici, text="", width=60,)
        self.mez1.grid(row=0, column=0)

        self.button_Brusici = tk.Button(self.top_brusici, text="Sestava pro brusírnu", width=60, command=self.sestava)
        self.button_Brusici.grid(row=1, column=0)

        self.mez2 = tk.Label(self.top_brusici, text="", width=60,)
        self.mez2.grid(row=2, column=0)
        
        self.button_Konec = tk.Button(self.top_brusici, text="Konec", width=60, command=self.top_brusici.destroy, fg="red")
        self.button_Konec.grid(row=3, column=0)