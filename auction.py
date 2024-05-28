import threading
import time

class Auction:
    def __init__(self, duration):
        self.products = []
        self.clients = {}
        self.duration = duration

    def add_product(self, product):
        for p in self.products:
            if p.name.lower() == product.name.lower():
                return False
        self.products.append(product)
        self.notify_clients(f"Produs nou adaugat: {product}")
        return True

    def add_client(self, client_name, client_conn):
        if client_name.lower() in [name.lower() for name in self.clients.keys()]:
            return False
        self.clients[client_name] = client_conn
        return True

    def notify_clients(self, message):
        for client in self.clients.values():
            client.sendall(message.encode())

    def start_auction(self, product):
        def auction_timer():
            time.sleep(self.duration)
            self.notify_clients(f"Licitatie incheiata pentru {product.name}. Pretul maxim: {product.highest_bid} "
                                f"(Proprietar: {product.owner}, Pret Initial: {product.starting_price}, Pret Maxim: {product.highest_bid})")
            print(f"Licitatie incheiata pentru {product.name}. Pretul final: {product.highest_bid}")
            self.products.remove(product)
        
        auction_thread = threading.Thread(target=auction_timer)
        auction_thread.start()
    
    def notify_new_bid(self, product, bidder, bid_amount):
        self.notify_clients(f"Licitatie noua pentru {product.name}: {bid_amount} de catre {bidder} "
                            f"(Proprietar: {product.owner}, Pret Initial: {product.starting_price}, Pret Maxim: {product.highest_bid})")
