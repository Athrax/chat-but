import customtkinter as ctk


class CadreMenuGauche:
    def __init__(self, master):
        super.__init__(master)
        self.main()
    def main(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)


class BoxMess:
    def __init__(self,CadreChat):


class CadreChat:
    def __init__(self, master):
        super.__init__(master)
        self.main()

    def main(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.cadre_messages = BoxMess(self)
        self.cadre_messages.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nswe", columnspan=0)

        self.cadre_entree_texte = BoxTexte(self)
        self.cadre_entree_texte.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nsw")


class Application(ctk.CTk):
    def __init__(self):
        super.__init__()
        self.title("Tahc")
        self.geometry("800x500")
        self.minsize(width=800, height=500)
        self.main()
    def main(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.cadre_menu_gauche = CadreMenuGauche(self)
        self.cadre_menu_gauche.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nswe", columnspan=0)

        self.cadre_chat = CadreChat(self)
        self.cadre_chat.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nsw")


