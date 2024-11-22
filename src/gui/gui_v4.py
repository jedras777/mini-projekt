from customtkinter import *

class Window:
    def __init__(self):
        self.root = CTk()
        self.root.geometry("800x800")
        set_appearance_mode("dark")
        self.menu_glowne()

    def mainloop(self):
        self.root.mainloop()

    def przycisk(self, frame, width, height, text, command=None):
        przycisk = CTkButton(master=frame, width=width, height=height, text=text, command=command)
        przycisk.pack()
        return przycisk

    def komenda(self, wiadomosc):
        print(f"{wiadomosc}")

    def change_frame(self, new_frame, old_frame):
        old_frame.pack_forget()
        new_frame.pack()

    def menu_glowne(self):
        frame_glowne = CTkFrame(self.root, width=1000, height=1000)
        frame_glowne.pack()
        btn1 = self.przycisk(frame_glowne, 500, 100, "Zakoduj tekst", command=lambda: self.change_frame(self.menu_szyfru(), frame_glowne))
        btn2 = self.przycisk(frame_glowne, 500, 100, "Odkoduj tekst", command=lambda: self.change_frame(self.menu_szyfru(), frame_glowne))
        btn3 = self.przycisk(frame_glowne, 500, 100, "Pokaż historię")
        btn4 = self.przycisk(frame_glowne, 500, 100, "Zapisz historię")
        btn5 = self.przycisk(frame_glowne, 500, 100, "Odkoduj tekst z pliku")
        btn6 = self.przycisk(frame_glowne, 500, 100, "Zakończ")
        return frame_glowne

    def menu_szyfru(self):
        frame_szyfru = CTkFrame(self.root, width=800, height=800)
        frame_szyfru.pack()
        btn1 = self.przycisk(frame_szyfru, 500, 100, "ROT13", command=lambda: self.komenda("elo"))
        btn2 = self.przycisk(frame_szyfru, 500, 100, "ROT47")
        btn3 = self.przycisk(frame_szyfru, 250, 100, "POWRÓT",command=lambda: self.change_frame(self.menu_glowne(), frame_szyfru))
        return frame_szyfru






apka = Window()
apka.mainloop()
