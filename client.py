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
    
    client_socket = clientSocketHanlder()                       # Init handler 
    if client_socket.socket_handler_init():                     # Init connection
        
        start_time = time.time()                
        
        fileHandler().generate_strings_file()                   # Generate file
        
        logging.info(f"Generate process completed in [{time.time() - start_time}] seconds")
        
        start_time = time.time()
        
        fileHandler.clear_file('response.txt')                  # Clear file , this method: 'fileHandler.write_strings_into_file' open file in mode append , need first time be empty
        
        line_count = 0                                          # This counter is used in the method: 'fileHandler.read_strings_from_file' to maintain the order of reading lines from the file
        while(True):
            strings , line_count = fileHandler.read_strings_from_file(line_count)
            if not strings:                                     # Indicates that the file in 'fileHandler.read_strings_from_file' has reached its end  
                break
            
            
            response = client_socket.send_strings_data(strings) # Send strings to server 
           
            # Write response into file ( separator is null in this case , the protocol dictates that the server already returns the strings with "\n" between items )
            fileHandler.write_strings_into_file(response,separator="")
            
        client_socket.close_socket()
        logging.info(f"Process completed in   [{time.time() - start_time}] seconds")
    