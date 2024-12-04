

from customtkinter import *

from src.facade.cipher_facade import *
from src.history.history_memory import HistoryOfCodingDecoding


class Window:
    def __init__(self):
        self.root = CTk()
        self.root.geometry("800x800")
        self.root.resizable(True, True)
        set_appearance_mode("dark")
        self.menu_glowne()
        self.facade = CipherFacade()
        self.historia = HistoryOfCodingDecoding()

    def mainloop(self):
        self.root.mainloop()

    def przycisk(self, frame, width, height, text, command=None):
        przycisk = CTkButton(master=frame, width=width, height=height, text=text, command=command)
        przycisk.pack()
        return przycisk

    def change_frame(self, new_frame, old_frame):
        old_frame.pack_forget()
        new_frame.pack()

    def zakoduj(self, entry, algorytm, label):
        encrypted = self.facade.encrypt(entry, algorytm)
        label.configure(text=encrypted)
        return encrypted

    def change_frame_history(self,new_frame, old_frame):
        old_frame.pack_forget()
        new_frame.pack()
        label_historia = CTkLabel(new_frame, text="historia jest pusta", width=700, height=700)
        label_historia.configure(text=self.facade.historia.pokaz_historie())
        label_historia.pack()







    def menu_glowne(self):
        frame_glowne = CTkFrame(self.root, width=1000, height=1000)
        frame_glowne.pack()
        btn1 = self.przycisk(frame_glowne, 500, 100, "Zakoduj tekst", command=lambda: self.change_frame(self.menu_szyfru(), frame_glowne))
        btn2 = self.przycisk(frame_glowne, 500, 100, "Odkoduj tekst", command=lambda: self.change_frame(self.menu_szyfru(), frame_glowne))
        btn3 = self.przycisk(frame_glowne, 500, 100, "Pokaż historię", command=lambda: self.change_frame_history(self.menu_historia(), frame_glowne))
        btn4 = self.przycisk(frame_glowne, 500, 100, "Zapisz historię")
        btn5 = self.przycisk(frame_glowne, 500, 100, "Odkoduj tekst z pliku")
        btn6 = self.przycisk(frame_glowne, 500, 100, "Zakończ")
        return frame_glowne

    def menu_szyfru(self):
        frame_szyfru = CTkFrame(self.root, width=800, height=800)
        frame_szyfru.pack()
        btn1 = self.przycisk(frame_szyfru, 500, 100, "ROT13", command=lambda: self.change_frame(self.menu_cipher_rot13(), frame_szyfru))
        btn2 = self.przycisk(frame_szyfru, 500, 100, "ROT47", command=lambda: self.change_frame(self.menu_cipher_rot47(), frame_szyfru))
        btn3 = self.przycisk(frame_szyfru, 250, 100, "POWRÓT",command=lambda: self.change_frame(self.menu_glowne(), frame_szyfru))
        return frame_szyfru

    def menu_cipher_rot13(self):
        frame_rot13 = CTkFrame(self.root, width=800, height=800)
        frame_rot13.pack()
        entry = CTkEntry(frame_rot13, placeholder_text="wpisz tekst", width=300, height=100)
        entry.pack()
        label_rot13 = CTkLabel(frame_rot13, text="zakodowany tekst", width=300, height=100)
        label_rot13.pack()
        btn1 = self.przycisk(frame_rot13, 500, 100, "ZAKODUJ", command=lambda :self.zakoduj(entry.get(), "ROT13", label_rot13))
        btn1.pack()
        btn2 = self.przycisk(frame_rot13, 500, 100, "POWROT", command=lambda: self.change_frame(self.menu_szyfru(), frame_rot13))
        btn2.pack()
        return frame_rot13

    def menu_cipher_rot47(self):
        frame_rot47 = CTkFrame(self.root, width=800, height=800)
        frame_rot47.pack()
        entry = CTkEntry(frame_rot47, placeholder_text="wpisz tekst", width=300, height=100)
        entry.pack()
        label_rot13 = CTkLabel(frame_rot47, text="zakodowany tekst", width=300, height=100)
        label_rot13.pack()
        btn1 = self.przycisk(frame_rot47, 500, 100, "ZAKODUJ", command=lambda :self.zakoduj(entry.get(), "ROT47", label_rot13))
        btn1.pack()
        btn2 = self.przycisk(frame_rot47, 500, 100, "POWROT", command=lambda: self.change_frame(self.menu_szyfru(), frame_rot47))
        btn2.pack()
        return frame_rot47

    def menu_historia(self):
        frame_historia = CTkFrame(self.root, width=800, height=800)
        frame_historia.pack()
        btn2 = self.przycisk(frame_historia, 500, 100, "POWROT",
                             command=lambda: self.change_frame(self.menu_glowne(), frame_historia))
        btn2.pack(side="bottom")

        return frame_historia







apka = Window()
apka.mainloop()
