import logging
from src.server_socket_handler import serverSocketHanlder

# For Visual Studio Code debug
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

if __name__ == "__main__":
    
    server_socket = serverSocketHanlder()
    server_socket.socket_handler_init()
        
    