import socket
import threading


class Server:
    def __init__(self, port):
        self.port = port
        self.client_id = 0
        self.serv_sock = self.create_serv_sock(self.port)
    
    def run_server(self):
        while True:
            client_sock = self.accept_client_conn(self.serv_sock,  self.client_id)
            t = threading.Thread(target=self.serve_client,
                                 args=(client_sock,  self.client_id))
            t.start()
            self.client_id += 1
    
    def serve_client(self, client_sock, client_id):
        request = self.read_request(client_sock)
        if request is None:
            print(f'Client #{client_id} unexpectedly disconnected')
        else:
            self.write_response(client_sock, request, client_id)
    
    def create_serv_sock(self, serv_port):
        serv_sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM,
                                  proto=0)
        serv_sock.bind(('', serv_port))
        serv_sock.listen()
        return serv_sock
    
    def accept_client_conn(self, serv_sock, client_id):
        client_sock, client_addr = serv_sock.accept()
        print(f'Client #{client_id} connected '
              f'{client_addr[0]}:{client_addr[1]}')
        return client_sock
    
    def read_request(self, client_sock):
        try:
            while True:
                message = client_sock.recv(1024)
                return f'Everything is OK, received your message: {message}'.encode('ascii')
        
        except ConnectionResetError:
            return None
    
    def write_response(self, client_sock, response, client_id):
        client_sock.sendall(response)
        client_sock.close()
        print(f'Client #{client_id} has been served')
        
        
if __name__ == '__main__':
    server = Server(53210)
    server.run_server()
