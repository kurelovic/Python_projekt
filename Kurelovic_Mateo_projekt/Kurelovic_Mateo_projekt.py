import tkinter as tk
from tkinter import simpledialog, messagebox

def dodaj_biljesku():
    nova_biljeska = simpledialog.askstring("Bilješka", "Unesite novu bilješku:")
    if nova_biljeska:
        with open("biljeske.txt", "a") as datoteka:
            datoteka.write(nova_biljeska + "\n")
        messagebox.showinfo("Obavijest", "Bilješka je uspješno spremljena.")

def pregledaj_biljeske():
    with open("biljeske.txt", "r") as datoteka:
        biljeske = datoteka.readlines()
        if biljeske==[]:
            messagebox.showinfo("Bilješke", "Nema spremljenih bilješki.")
        else:
            prikaz = "\n".join(f"{i + 1}. {b.strip()}" for i, b in enumerate(biljeske))
            messagebox.showinfo("Sve bilješke", prikaz)
        
prozor = tk.Tk()
prozor.title("Bilješke")
prozor.geometry("300x200")

btn_dodaj = tk.Button(prozor, text="Dodaj novu bilješku", command=dodaj_biljesku)
btn_dodaj.pack(pady=10)

btn_pregledaj = tk.Button(prozor, text="Pregledaj sve bilješke", command=pregledaj_biljeske)
btn_pregledaj.pack(pady=10)

btn_izlaz = tk.Button(prozor, text="Izlaz", command=prozor.destroy)
btn_izlaz.pack(pady=10)

