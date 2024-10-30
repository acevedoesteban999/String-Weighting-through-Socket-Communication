import logging
from src.client_socket_handler import clientSocketHanlder
from src.file_hanlde import fileHandler
import time

# For Visual Studio Code debug
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

# Loggin configuration
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
        strings = fileHandler().generate_strings_file(get_strings = True)
        
        start_time = time.time()
        # Send strings to server 
        response = client_socket.send_strings_data(strings)
        end_time = time.time()
        logging.info(f"Process completed in {end_time - start_time} seconds")
        print(f"Process completed in {end_time - start_time} seconds")
        # Write response into file ( newline is null , the protocol dictates that the server already returns the strings with "\n" between items )
        fileHandler.write_strings_into_file(response,newline="")
    