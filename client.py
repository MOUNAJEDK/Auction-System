import socket
import threading

HOST = 'localhost'
PORT = 12345

def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if message:
            print(message)
        else:
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    
    client_name = input("Introduceti numele dvs.: ")
    client_socket.sendall(client_name.encode())
    
    response = client_socket.recv(1024).decode()
    if response == "Numele este deja folosit.":
        print(response)
        client_socket.close()
        return
    
    print(response)
    
    print("\nBine ati venit la serverul de licitatii!")
    print("Comenzi disponibile:")
    print("1. ADAUGA_PRODUS <nume_produs> <pret_initial> - Adauga un produs la licitatie")
    print("2. PUNE_LICITATIE <nume_produs> <suma_licitata> - Plaseaza o licitatie pentru un produs")
    print("3. EXIT - Iesire din aplicatie\n")
    
    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    
    while True:
        command = input()
        if command.upper() == "EXIT":
            print("Deconectare de la server...")
            client_socket.close()
            break
        client_socket.sendall(command.encode())

if __name__ == "__main__":
    main()
