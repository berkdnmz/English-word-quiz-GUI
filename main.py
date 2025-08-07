
from tkinter import *
import random

kelimeler = {
    "apple": "elma",
    "car": "araba",
    "sun": "güneş",
    "house": "ev",
    "dog": "köpek",
    "book": "kitap"
}

def yeni_kelime():
    global aktif_kelime
    aktif_kelime = random.choice(list(kelimeler.keys()))
    label_english_word.config(text=aktif_kelime)
    entry_turkish_word.delete(0, END)
    label_sonuç.config(text="")

def kontrol_et(event):
    cevap = entry_turkish_word.get().strip().lower()
    dogru_cevap = kelimeler[aktif_kelime].lower()

    if cevap == dogru_cevap:
        label_sonuç.config(text = "DOĞRU!", fg="green")
    else:
        label_sonuç.config(text="YANLIŞ", fg="red")

    root.after(1000, yeni_kelime)

def center(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    win.geometry(f"{width}x{height}+{x}+{y}")


#ekran
root = Tk()
root.title("English Word Quiz")
root.resizable(width=False, height=False)
center(root,800,500)
root.configure(bg="#222222")

for i in range(10):
    root.grid_rowconfigure(i, weight=1, minsize=40)
for i in range(4):
    root.grid_columnconfigure(i, weight=1, minsize=40)



label_baslik = Label(root, text="English Word Quiz", font=("Helvetica", 20, "bold"), background="#F5F5DC", padx=20, pady=10)
label_baslik.place(relx=0.5, rely=0.08, anchor='center')

label_english = Label(root, text="-- English --", font=("Helvetica", 15, "bold"), background="black", foreground="white",padx=20, pady=10)
label_english.grid(row=3, column=1, padx=10, pady=10)

label_turkish = Label(root, text="-- Türkçe --", font=("Helvetica", 15, "bold"), background="black",foreground="white", padx=20, pady=10)
label_turkish.grid(row=3, column=2, padx=10, pady=10)
label_english_word = Label(root, text="", font=("Helvetica", 13), background="white", foreground="black", padx=56, pady=0)
label_english_word.grid(row=4, column=1, padx=10, pady=10)

entry_turkish_word = Entry(root,font=("Helvetica", 13), width=16)
entry_turkish_word.grid(row=4, column=2, padx=10, pady=0)
entry_turkish_word.focus()
entry_turkish_word.bind("<Return>", kontrol_et)

maker_label = Label(root, text="Created by Berk",background="#F5F5DC", font=("Helvetica", 11, "italic bold",))
maker_label.place(relx=1.0, rely=1.0, anchor="se")

label_sonuç = Label(root , text="", background="#F5F5DC", font=("Helvetica", 15, "bold",), padx= 90)
label_sonuç.place(relx=0.5, rely=0.7, anchor="center")


yeni_kelime()


root.mainloop()