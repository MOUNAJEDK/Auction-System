import socket
import threading
from auction import Auction
from product import Product

HOST = 'localhost'
PORT = 12345
AUCTION_DURATION = 60

auction = Auction(AUCTION_DURATION)

def handle_client(client_socket, client_address):
    client_name = ""
    connected = False
    try:
        client_name = client_socket.recv(1024).decode().strip()
        if not auction.add_client(client_name, client_socket):
            client_socket.sendall("Numele este deja folosit.".encode())
            client_socket.close()
            return
        
        connected = True
        client_socket.sendall("Conectat la serverul de licitatii.\n".encode())
        print(f"Client conectat: {client_name} ({client_address})")

        if auction.products:
            products_list = "\nProduse in curs de licitatie:\n"
            for product in auction.products:
                products_list += f"{product}\n"
            client_socket.sendall(products_list.encode())
        else:
            client_socket.sendall("Nu exista produse in curs de licitatie.\n".encode())
        
        while True:
            data = client_socket.recv(1024).decode().strip()
            if data.upper().startswith("ADAUGA_PRODUS"):
                _, product_name, starting_price = data.split(maxsplit=2)
                product = Product(product_name, client_name, float(starting_price))
                if auction.add_product(product):
                    auction.start_auction(product)
                    print(f"Produs adaugat: {product_name} de {client_name} cu pretul {starting_price}")
                else:
                    client_socket.sendall("Produsul exista deja.\n".encode())
            elif data.upper().startswith("PUNE_LICITATIE"):
                _, product_name, bid_amount = data.split(maxsplit=2)
                product = next((p for p in auction.products if p.name.lower() == product_name.lower()), None)
                if product:
                    if client_name.lower() != product.owner.lower():
                        if product.place_bid(client_name, float(bid_amount)):
                            auction.notify_new_bid(product, client_name, float(bid_amount))
                            print(f"Licitatie noua: {product_name} - {bid_amount} de {client_name}")
                        else:
                            client_socket.sendall("Suma licitata este prea mica.\n".encode())
                    else:
                        client_socket.sendall("Nu puteti licita pentru propriul produs.\n".encode())
                else:
                    client_socket.sendall("Produsul nu a fost gasit.\n".encode())
            else:
                client_socket.sendall("Comanda invalida.\n".encode())
    except Exception as e:
        print(f"Eroare: {e}")
    finally:
        if connected:
            client_socket.close()
            print(f"Client deconectat: {client_name} ({client_address})")
        else:
            client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server pornit pe {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()
