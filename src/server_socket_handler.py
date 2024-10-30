from .socket.socket_handler import socketHandler,socket
import logging

class serverSocketHanlder(socketHandler): 
      
    def socket_handler_init(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self._host, self._port))
                s.listen(1)
                while True:
                    conn, addr = s.accept()
                    with conn:
                        print('Connected by', addr)
                        while True:
                            data = conn.recv(1024)
                            print(data)
                            if not data: 
                                break
                            conn.sendall("1000\n200\n300".encode())
        except Exception as e:
            logging.error(e)