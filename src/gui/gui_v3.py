from datetime import datetime
from symtable import Class
from tkinter import *

from src.ciphers.base_cypher import lista
from src.ciphers.rot13_cipher import szyfrowanie_rot13, deszyfrowanie_rot13
from src.ciphers.rot47_cypher import szyfrowanie_rot47, deszyfrowanie_rot47
from datetime import datetime

def dodaj_do_historii(text: str, algorytm: str)-> None:
    czas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    liczba = len(historia)
    if historia == {}:
        liczba += 1
        historia[liczba] = f"'text': {text}, 'algorithm': {algorytm}, 'timestamp: {czas}"
    else:
        liczba += 1
        historia[liczba] = f"'text': {text}, 'algorithm': {algorytm}, 'timestamp: {czas}"

def change_frame(new_frame: Frame, old_frame: Frame):
    old_frame.forget()
    new_frame.pack()

def cipher13():
    input_text = entry_rot13.get()
    if entry_rot13.get() == "":
        label_rot13.configure(text="wpisz tekst!!!!")
    else:
        ciphering = szyfrowanie_rot13(input_text)
        label_rot13.configure(text=f"{ciphering}")
        dodaj_do_historii(ciphering, "ROT13")

def cipher47():
    input_text = entry_rot47.get()
    if entry_rot47.get() == "":
        label_rot47.configure(text="wpisz tekst!!!!")
    else:
        ciphering = szyfrowanie_rot47(input_text)
        label_rot47.configure(text=f"{ciphering}")
        dodaj_do_historii(ciphering, "ROT47")

def pokaz_historie():
    tekst = ""
    if not historia:
        tekst = "TWOJA HISTORIA JEST PUSTA"
        label_historii.configure(text=tekst)
    else:
        for indeks, elem in historia.items():
            tekst += f"{indeks} => {elem}\n"
        label_historii.configure(text=tekst)


def decipher13():
    input_text = entry_derot13.get()
    if entry_derot13.get() == "":
        label_derot13.configure(text="wpisz tekst!!!!")
    else:
        ciphering = deszyfrowanie_rot13(input_text)
        label_derot13.configure(text=f"{ciphering}")
        dodaj_do_historii(ciphering, "ROT13")

def decipher47():
    input_text = entry_derot47.get()
    if entry_derot47.get() == "":
        label_derot47.configure(text="wpisz tekst!!!!")
    else:
        ciphering = deszyfrowanie_rot47(input_text)
        label_derot47.configure(text=f"{ciphering}")
        dodaj_do_historii(ciphering, "ROT47")

# def dodaj_his(historia):
#     tekst = ""
#     for i, x in historia.items():
#         tekst += f"{i} => {x}\n"
#     return tekst
#
# def odswiez_text():
#     text_historii.config(state="normal")  # Ustawienie na edytowalny
#     text_historii.delete("1.0", END)   # Usunięcie poprzedniej zawartości
#     text_historii.insert("1.0", dodaj_his(historia))  # Wstawienie nowego tekstu
#     text_historii.config(state="disabled")  # Ustawienie na tylko do odczytu

historia = {}


window = Tk()
window.geometry("500x500")







 #menu
menu = Frame(window)
menu.pack()
btn1 = Button(menu, width=40, height=5, text="Zakoduj tekst", command=lambda: change_frame(menu_ciphering,menu))
btn2 = Button(menu, width=40, height=5, text="Zdekoduj tekst",command=lambda: change_frame(menu_deciphering,menu))
btn3 = Button(menu, width=40, height=5, text="Pokaz historie", command=lambda: change_frame(okno_historii, menu))
btn4 = Button(menu, width=40, height=5, text="Zapisz historie do pliku")
btn5 = Button(menu, width=40, height=5, text="Odkoduj tekst z pliku")

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()

#menu1
menu_ciphering = Frame(window)
btn1 = Button(menu_ciphering, width=40, height=5, text="ROT13", command=lambda: change_frame(menu_rot13,menu_ciphering))
btn2 = Button(menu_ciphering, width=40, height=5, text="ROT47", command=lambda: change_frame(menu_rot47, menu_ciphering))
btn3 = Button(menu_ciphering, width=40, height=5, text="WSTECZ", command=lambda: change_frame(menu,menu_ciphering))

btn1.pack()
btn2.pack()
btn3.pack()

#menu_rot13
menu_rot13 = Frame(window)
label = Label(menu_rot13, text="WPISZ TEKST")
label.pack()
entry_rot13 = Entry(menu_rot13, width=50)
entry_rot13.pack()
btn1 = Button(menu_rot13, width=40, height=5, text="SZYFRUJ", command=lambda: cipher13())
btn1.pack()
label_rot13 = Label(menu_rot13, width=40, height=5, text="SZYFR")
label_rot13.pack()
btn3 = Button(menu_rot13, width=40, height=5, text="WSTECZ", command=lambda: change_frame(menu_ciphering,menu_rot13))
btn3.pack()

#menu_rot47
menu_rot47 = Frame(window)
label = Label(menu_rot47, text="WPISZ TEKST")
label.pack()
entry_rot47 = Entry(menu_rot47, width=50)
entry_rot47.pack()
btn1 = Button(menu_rot47, width=40, height=5, text="SZYFRUJ", command=lambda: cipher47())
btn1.pack()
label_rot47 = Label(menu_rot47, width=40, height=5, text="SZYFR")
label_rot47.pack()
btn3 = Button(menu_rot47, width=40, height=5, text="WSTECZ", command=lambda: change_frame(menu_ciphering,menu_rot47))
btn3.pack()


#historia
okno_historii = Frame(window)
btn4 = Button(okno_historii, width=40, height=3, text="POKAZ HISTORIE", command=lambda: pokaz_historie())
btn4.pack()
label = Label(okno_historii, text="HISTORIA")
label.pack()
label_historii = Label(okno_historii, width=100, height=30, text="HISTORIA JEST PUSTA", font=20, bg="green", relief="raised", borderwidth=10)
label_historii.pack()
btn3 = Button(okno_historii, width=40, height=3, text="WSTECZ", command=lambda: change_frame(menu,okno_historii))
btn3.pack()

# text_historii = Text(okno_historii, width=100, height=30, wrap="word", font=20, bg="green", relief="raised", borderwidth=10)
# text_historii.insert("1.0",f"{dodaj_his(historia)}")
#
# scrollbar = Scrollbar(okno_historii)
# scrollbar.pack(side=LEFT)
# text_historii.config(yscrollcommand=scrollbar.set)



#menu2
menu_deciphering = Frame(window)
btn1 = Button(menu_deciphering, width=40, height=5, text="ROT13", command=lambda: change_frame(menu_derot13, menu_deciphering))
btn2 = Button(menu_deciphering, width=40, height=5, text="ROT47", command=lambda: change_frame(menu_derot47, menu_deciphering))
btn3 = Button(menu_deciphering, width=40, height=5, text="WSTECZ", command=lambda: change_frame(menu,menu_deciphering))
btn1.pack()
btn2.pack()
btn3.pack()

#menu decipherrot13
menu_derot13 = Frame(window)
label = Label(menu_derot13, text="WPISZ TEKST")
label.pack()
entry_derot13 = Entry(menu_derot13, width=50)
entry_derot13.pack()
btn_de = Button(menu_derot13, width=40, height=5, text="DESZYFRUJ", command=lambda: decipher13())
btn_de.pack()
label_derot13 = Label(menu_derot13, width=40, height=5, text="DESZYFR")
label_derot13.pack()
btn3 = Button(menu_derot13, width=40, height=5, text="WSTECZ", command=lambda: change_frame(menu_deciphering,menu_derot13))
btn3.pack()

#menu decipherrot47
menu_derot47 = Frame(window)
label = Label(menu_derot47, text="WPISZ TEKST")
label.pack()
entry_derot47 = Entry(menu_derot47, width=50)
entry_derot47.pack()
btn1 = Button(menu_derot47, width=40, height=5, text="DESZYFRUJ", command=lambda: decipher47())
btn1.pack()
label_derot47 = Label(menu_derot47, width=40, height=5, text="DESZYFR")
label_derot47.pack()
btn3 = Button(menu_derot47, width=40, height=5, text="WSTECZ", command=lambda: change_frame(menu_deciphering,menu_derot47))
btn3.pack()

window.mainloop()