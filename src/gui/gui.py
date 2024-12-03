
from datetime import datetime

from customtkinter import *

from src.ciphers.rot13_cipher import *
from src.ciphers.rot47_cipher import *

app = CTk()
app.geometry("800x800")
set_appearance_mode("dark")

historia = {}

def ciphering_to_history(text, algorytm):
    czas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    liczba = len(historia)
    if historia == {}:
        liczba += 1
        historia[liczba] = {"text":text, "algorythm":algorytm, "timestamp":czas}
    else:
        historia[liczba] = {"text":text, "algorythm":algorytm, "timestamp":czas}

def show_menu(menu):
    for m in menus:
        m.place_forget()
    menu.place(relx=0.5, rely=0.5, anchor="center")

def ciphering_text_rot13():
    input_text = entry1.get()
    ciphering = szyfrowanie_rot13(input_text)
    label.configure(text=f"{ciphering}")
    ciphering_to_history(input_text, "ROT13")

def ciphering_text_rot47():
    input_text = entry1.get()
    ciphering = szyfrowanie_rot47(input_text)
    label1.configure(text=f"{ciphering}")
    ciphering_to_history(input_text, "ROT47")



menu_glowne = CTkFrame(app, width=1000, height=1000)
btn1 = CTkButton(menu_glowne, width=500, height=100, text="Zakoduj tekst", command=lambda: show_menu(menu_z_wyborem_szyfru_kodujacego))
btn2 = CTkButton(menu_glowne, width=500, height=100, text="Zdekoduj tekst")
btn3 = CTkButton(menu_glowne, width=500, height=100, text="Pokaz historie")
btn4 = CTkButton(menu_glowne, width=500, height=100, text="Zapisz historie do pliku")
btn5 = CTkButton(menu_glowne, width=500, height=100, text="Odkoduj tekst z pliku")

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()

menu_z_wyborem_szyfru_kodujacego = CTkFrame(app, width=200, height=200)
btn1 = CTkButton(menu_z_wyborem_szyfru_kodujacego, width=500, height=100, text="ROT13", command=lambda: show_menu(okno_z_wprowadzniem_textu_i_wyswitlaniem_rot13))
btn2 = CTkButton(menu_z_wyborem_szyfru_kodujacego, width=500, height=100, text="ROT47", command=lambda: show_menu(okno_z_wprowadzniem_textu_i_wyswitlaniem_rot47))
btn3 = CTkButton(menu_z_wyborem_szyfru_kodujacego, width=500, height=100, text="powrot", command=lambda: show_menu(menu_glowne))

btn1.pack()
btn2.pack()
btn3.pack()

okno_z_wprowadzniem_textu_i_wyswitlaniem_rot13 = CTkFrame(app, width=600, height=600)
entry1 = CTkEntry(okno_z_wprowadzniem_textu_i_wyswitlaniem_rot13, width=500, height=200, placeholder_text="wprowadz tekst do zakodowania")
entry1.pack()
btn1 = CTkButton(okno_z_wprowadzniem_textu_i_wyswitlaniem_rot13,width=500, height=100, text="KONWERTUJ", command=lambda :ciphering_text_rot13())
btn1.pack()
label = CTkLabel(okno_z_wprowadzniem_textu_i_wyswitlaniem_rot13,width=500,height=200,text="tu pojawi sie kod")
label.pack()
btn2 = CTkButton(okno_z_wprowadzniem_textu_i_wyswitlaniem_rot13, width=500, height=100, text="Powrot", command=lambda: show_menu(menu_z_wyborem_szyfru_kodujacego))
btn2.pack()

okno_z_wprowadzniem_textu_i_wyswitlaniem_rot47 = CTkFrame(app, width=600, height=600)
entry1 = CTkEntry(okno_z_wprowadzniem_textu_i_wyswitlaniem_rot47, width=500, height=200, placeholder_text="wprowadz tekst do zakodowania")
entry1.pack()
btn1 = CTkButton(okno_z_wprowadzniem_textu_i_wyswitlaniem_rot47,width=500, height=100, text="KONWERTUJ", command=lambda: ciphering_text_rot47())
btn1.pack()
label1 = CTkLabel(okno_z_wprowadzniem_textu_i_wyswitlaniem_rot47,width=500,height=200,text="tu pojawi sie kod")
label1.pack()
btn2 = CTkButton(okno_z_wprowadzniem_textu_i_wyswitlaniem_rot47, width=500, height=100, text="Powrot", command=lambda: show_menu(menu_z_wyborem_szyfru_kodujacego))
btn2.pack()


menus = [menu_glowne,menu_z_wyborem_szyfru_kodujacego,okno_z_wprowadzniem_textu_i_wyswitlaniem_rot13, okno_z_wprowadzniem_textu_i_wyswitlaniem_rot47]
show_menu(menu_glowne)





app.mainloop()


