from .socket.socket_handler import socketHandler
import logging

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
    
    
    def send_strings_data(self,data_str:str,max = 1) -> str:
        """
            Send strings agrupadted to server
        """
        
        # To group, all values will be stored in a string, and with a counter, the send event will be triggered
        buffer_str = ""
        response = ""
        count_str_grouped = 0
        for line in data_str:
            buffer_str += line                                  # Group strings 
            count_str_grouped += 1                              # Inc count  
            if count_str_grouped >= max:   
                self._socket.sendall(buffer_str.encode())       # Its necesary convert to binay ( str.encode, by default utf-8)
                response += self._socket.recv(1024).decode()    # Its necesary convert to str ( binary.decode, by default utf-8)
                
                #Reset buffer and count
                buffer_str = ""
                count_str_grouped = 0
                
        # Before finishing the loop, it's necessary to check if there is any data that has not been sent yet
        if count_str_grouped:
            self._socket.sendall((buffer_str + "\n\r").encode())      
            response += self._socket.recv(1024).decode()   
        else:
            self._socket.sendall("\n\r".encode())  
        return response
         
        
        
        