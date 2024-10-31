from .socket.socket_handler import socketHandler
import logging
from .environ_handler import ENVIROMENT


class clientSocketHanlder(socketHandler):
    """
        Handler Client Socket 
            - This client sends the data separated by '\\n' and expects to receive the same format from the server
    """   
    def socket_handler_init(self) -> bool:
        """
            Init Client Handle Socket
        """
        try:
            self._socket.connect((self._host,self._port))
            return True
        except ConnectionRefusedError as e:                                                 # Connection Error
            logging.error(f" Could not connect to {self._host} : {self._port}\n\t *{e}")
        except Exception as e:                                                              # Another Error                
            logging.error(e)
        return False
    
    def send_strings_data(self,data_str:str) -> str:
        """
            Send strings agrupadted to server
        """
        
        # To group, all values will be stored in a string, and with a counter, the send event will be triggered
        buffer_str = ""
        response = ""
        count_str_grouped = 0
        for line in data_str:
            buffer_str += line                                  # Group strings 
            count_str_grouped += 1                              # Increment counter  
            if count_str_grouped >= ENVIROMENT['MAX_LINES_TO_SEND']:   
                self._socket.sendall(buffer_str.encode())       # Is necesary convert to binay ( str.encode, by default utf-8)
                
                
                # The number of bytes to receive will be at least equal to the number of bytes sent, plus 10. Ten bytes per line at most, which will include weighting
                response += self._socket.recv(ENVIROMENT["MAX_LINES_TO_SEND"] * 10).decode()    # Is necesary convert to str ( binary.decode, by default utf-8)
                
                #Reset buffer and counter
                buffer_str = ""
                count_str_grouped = 0
                
        # Before finishing the loop, it's necessary to check if there is any data that has not been sent yet
        if count_str_grouped:
            self._socket.sendall((buffer_str).encode())     
            response += self._socket.recv(1024).decode()   
    
            
        return response
    
    
        
        
        