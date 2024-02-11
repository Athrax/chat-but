import customtkinter as ctk


class Application(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tahc")
        self.geometry("800x500")
        self.minsize(width=400, height=200)

        self.cadre_menu_gauche = CadreMenuGauche(self)
        self.cadre_menu_gauche.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="nswe")

        self.cadre_chat = CadreChat(self)
        self.cadre_chat.grid(row=0, column=1, padx=(10, 10), pady=10, sticky="nswe")

        self.rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=10)

        self.connection()
        self.main()

    def main(self):
        pass

    def connection(self):
        import socket

        # Créer un objet socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Se connecter au serveur
        host = '127.0.0.1'
        port = 12345
        self.client_socket.connect((host, port))


class CadreChat(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=10)
        self.grid_rowconfigure(0, weight=10)
        self.grid_rowconfigure(1, weight=1)

        self.cadre_entree_texte = BoxView(self)
        self.cadre_entree_texte.grid(row=0, column=0, padx=(10, 10), pady=(10, 0), sticky="nswe")

        self.cadre_messages = BoxInput(self)
        self.cadre_messages.grid(row=1, column=0, padx=(10, 10), pady=10, sticky="nswe")

        self.main()

    def main(self):
        pass


class BoxView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)


class BoxInput(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.entreeMessage = ctk.CTkTextbox(self, height=5)
        self.entreeMessage.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.boutonEnvoyer = ctk.CTkButton(self, text="✉️", width=50, command=self.envoyerMessage)
        self.boutonEnvoyer.grid(row=0, column=1, padx=5, pady=5)

    def envoyerMessage(self):
        # Envoyer des données au serveur
        message = self.entreeMessage.get(1.0, ctk.END)
        self.master.master.client_socket.send(message.encode())

        # Supprimer l'entrée
        self.entreeMessage.delete(1.0, ctk.END)


class CadreMenuGauche(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)


application = Application()
application.mainloop()
