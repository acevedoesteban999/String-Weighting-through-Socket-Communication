import logging
from src.server_socket_handler import serverSocketHanlder

# For Visual Studio Code debug
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

# Loggin configuration
logging.basicConfig(
    format='[%(asctime)s][%(levelname)s]: %(message)s',  
    datefmt='%Y-%m-%d %H:%M:%S'                         
)
if __name__ == "__main__":
    
    server_socket = serverSocketHanlder()   # Init hanlder
    
    server_socket.socket_handler_init()     # Main lopp for server
        
    