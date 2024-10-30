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
        
        start_time = time.time()
        
        fileHandler().generate_strings_file()
        
        
        logging.info(f"Generate process completed in [{time.time() - start_time}] seconds")
        
        eof = False 
        start_time = time.time()
        line_count = 0
        while(True):
            
            strings , line_count, eof = fileHandler.read_strings_from_file(line_count)
            if eof:
                break
            print(strings,line_count)
            
            # Send strings to server 
            response = client_socket.send_strings_data(strings)
            print("A")
            # Write response into file ( separator is null , the protocol dictates that the server already returns the strings with "\n" between items )
            fileHandler.write_strings_into_file(response,separator="")
        logging.info(f"Process completed in   [{time.time() - start_time}] seconds")
    