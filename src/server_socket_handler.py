from .socket.socket_handler import socketHandler,socket
import logging

class serverSocketHanlder(socketHandler): 
    """
        Handler Server Socket 
        
            - The server must receive the data separated by '\\n' and return the same format for the weightings
    """
    
    
    
    def socket_handler_init(self):
        """
            Init Server Handle Socket
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Open the server
            sock.bind((self._host, self._port)) 
            sock.listen(1)
            while True:
                conn, _ = sock.accept()                                 # Accept a client
                with conn:
                    while True:                                         # Loop until the end signal (\n\n) is received
                        data = conn.recv(1024).decode() 
                        if not data:
                            break
                        lines = [i for i in data.split("\n") if i and i!='\r']      # Not take empty strings 
                        
                        weighting:str = self.process_data(lines)        # Process data
                        
                        if weighting: 
                            conn.sendall(weighting.encode())            
                        
                        if ("\r" in data):                            # End of data signal, exit until a new connection
                            break
        

    def process_data(self,lines:str) -> str:
        """
            Process the received data and provide a response regarding the weighting of the strings
                - This method receives the data separated by '\\n' and calculates the weighting, 
                returning it in a string separated by the same character ('\\n')
        """
        weighting = ""
        for line in lines:
            if "aa" in line.lower():
                logging.warning(f"Double 'a' rule detected >> '{line}'") 
                weighting += "1000\n"
            else:
                try: # Try For invalid strings where there are no spaces ( division by zero )
                    count_letters = sum(caracter.isalpha() for caracter in line )           # Get letters counter
                    count_numbers = sum(caracter.isnumeric() for caracter in line )         # Get cumbers counter
                    count_spaces = sum(caracter.isspace() for caracter in line )            # Get spaces counter
                    metric:float = (count_letters *1.5 + count_numbers*2)/count_spaces      # Apply weighting formula
                    weighting += f"{metric}\n"                                              #Save as string
                except:
                    weighting += "0\n"                                                      # Return 0 for this data if there is any error 
        return weighting
    