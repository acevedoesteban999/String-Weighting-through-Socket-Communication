import socket
from abc import ABC, abstractmethod

class socketHandler(ABC):
    """
        Abstract Class for handling sockets
    """
    
    def __init__(self, host:str | int ='localhost', port:int=8080 ,proto:int = socket.AF_INET , fileno:int|None = socket.SOCK_STREAM ):
        self._host = host
        self._port = port
        self._socket = socket.socket(proto, fileno)
    
    @abstractmethod
    def socket_handler_init(self):
        """
            Abstract class method
        """
        pass
        
        