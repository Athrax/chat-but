import socket

# Créer un objet socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Se connecter au serveur
host = '127.0.0.1'
port = 12345
client_socket.connect((host, port))

# Envoyer des données au serveur
message = "Bonjour, serveur!"
client_socket.send(message.encode())

# Fermer le socket client
client_socket.close()
