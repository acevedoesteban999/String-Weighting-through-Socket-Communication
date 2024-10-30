from .socket.socket_handler import socketHandler
import logging

MAX_ITEMS_TO_SEND = 10

class clientSocketHanlder(socketHandler):   
    def socket_handler_init(self) -> bool:
        """
            Init Client Handle Socket
        """
        try:
            self._socket.connect((self._host,self._port))
            return True
        except ConnectionRefusedError as e:     # Connection Error
            logging.error(f" Could not connect to {self._host} : {self._port}\n\t *{e}")
        except Exception as e:                  # Another Error                
            logging.error(e)
        return False
    
    
    def send_strings_data(self,data_str:str) -> str:
        """
            Send strings agrupadted to server
                - This method use MAX_ITEMS_TO_SEND global variable
        """
        
        # To group, all values will be stored in a string, and with a counter, the send event will be triggered
        buffer_str = ""
        response = ""
        count_str_grouped = 0
        for line in data_str:
            buffer_str += line                                  # Group strings 
            count_str_grouped += 1                              # Increment counter  
            if count_str_grouped >= MAX_ITEMS_TO_SEND:   
                self._socket.sendall(buffer_str.encode())       # Its necesary convert to binay ( str.encode, by default utf-8)
                response += self._socket.recv(1024).decode()    # Its necesary convert to str ( binary.decode, by default utf-8)
                
                #Reset buffer and counter
                buffer_str = ""
                count_str_grouped = 0
                
        # Before finishing the loop, it's necessary to check if there is any data that has not been sent yet
        if count_str_grouped:
            self._socket.sendall((buffer_str + "\r").encode())   # Send data and the end signal    
            response += self._socket.recv(1024).decode()   
        else:
            self._socket.sendall("\r".encode())                   # Send only the end signal
            
        return response
         
        
        
        