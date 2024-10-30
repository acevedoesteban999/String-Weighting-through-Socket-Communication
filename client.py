import logging
from src.client_socket_handler import clientSocketHanlder
from src.file_hanlde import fileHandler


# For Visual Studio Code debug
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

if __name__ == "__main__":
    
    client_socket = clientSocketHanlder()
    if client_socket.socket_handler_init():
        """
            Since the same file is being generated, the condition of get_strings is set to true 
            to directly obtain the list from the file. In case another file or read again:
                - strings = fileHandler.read_strings_from_file(filename)
        """
        strings = fileHandler().generate_strings_file(get_strings = True)
        client_socket.send_strings_data(strings)
        
    