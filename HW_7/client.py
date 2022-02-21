import socket


class Client:
    def __init__(self, host, port):
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_sock.connect((host, port))
    
    def server_message(self):
        message = input('What is your name?: ').encode('ascii')
        self.client_sock.sendall(message)
        data = self.client_sock.recv(1024)
        print(data)
        self.client_sock.close()
       
        
if __name__ == '__main__':
    clients = ['client_1', 'client_2', 'client_3', 'client_4']
    connections = []
    for client in clients:
        connect = Client('', 53210)
        connections.append(connect)
        
    for connect in connections:
        connect.server_message()
