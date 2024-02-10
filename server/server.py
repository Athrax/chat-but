import socket
import threading

def gerer_client(client_socket, client_address):
    print(f"Connexion établie avec {client_address}")

    # Recevoir des données du client
    donnees = client_socket.recv(1024)
    print(f"Message reçu du client {client_address}: {donnees.decode()}")

    # Fermer le socket client
    client_socket.close()
    print(f"Connexion avec {client_address} fermée")

# Créer un objet socket
serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associer le socket à une adresse et un port
host = '127.0.0.1'
port = 12345
serveur_socket.bind((host, port))

# Attendre les connexions entrantes (maximum 5)
serveur_socket.listen(5)
print(f"Le serveur écoute sur {host}:{port}")

while True:
    # Accepter la connexion du client
    client_socket, client_address = serveur_socket.accept()

    # Créer un thread pour gérer le client
    client_thread = threading.Thread(target=gerer_client, args=(client_socket, client_address))
    client_thread.start()