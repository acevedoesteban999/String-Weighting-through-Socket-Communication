import logging
from src.client_socket_handler import clientSocketHanlder
from src.file_hanlde import fileHandler
import time

# For Visual Studio Code debug
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

# Logging configuration
logging.basicConfig(
    level=logging.INFO,  
    format='[%(asctime)s][%(levelname)s]: %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S'
)

if __name__ == "__main__":
    
    client_socket = clientSocketHanlder()   # Init handler 
    if client_socket.socket_handler_init(): # Init connection
        """
            Since the same file is being generated, the condition of get_strings is set to true 
            to directly obtain the list from the file. In case another file or read again:
                - strings = fileHandler.read_strings_from_file(filename)
        """
        start_time = time.time()
        
        strings = fileHandler().generate_strings_file(get_strings = True)
        
        logging.info(f"Generate process completed in [{time.time() - start_time}] seconds")
        
        
        start_time = time.time()
        
        # Send strings to server 
        response = client_socket.send_strings_data(strings)
        
        logging.info(f"Sending process completed in  [{time.time() - start_time}] seconds")
        
        start_time = time.time()
        # Write response into file ( separator is null , the protocol dictates that the server already returns the strings with "\n" between items )
        fileHandler.write_strings_into_file(response,separator="")
        logging.info(f"Writen process completed in   [{time.time() - start_time}] seconds")
    