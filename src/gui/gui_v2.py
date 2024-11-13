import tkinter as tk


class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Moja Aplikacja Tkinter")
        self.root.geometry("800x800")

    def create_button(self,text, command):
        button = tk.Button(self.root, text=text, command=command)
        button.pack()

    def create_entry(self, text):
        self.entry = tk.Entry(self.root, width=100)
        self.entry.pack()


    def deszyfruj_rot(self):


    def menu_glowne(self):
        self.create_button("elo", )




if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    app.create_entry("elo")
    root.mainloop()

