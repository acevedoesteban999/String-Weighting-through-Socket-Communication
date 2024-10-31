from .socket.socket_handler import socketHandler,socket
import logging
from .environ_handler import ENVIROMENT

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
            try:
                sock.bind((self._host, self._port)) 
                sock.listen(1)
            except Exception as e:
                logging.error(f"Server could not start on {self._host}:{self._port}\n\t*{e}")
                exit()
                
            logging.info(f"Server has started on {self._host}:{self._port}")
            
            """ 
                The constant 'MAX_RECV' is the max number of bytes to recive. Approximately 
                the max number of lines to send is determined by the maximum line 
                length (95 + 5 + 1; 5 to reach 100 and one for the separator 
                character '\n') plus 10 bytes for other protocol characters, 
                such as end-of-line characters
                    - Why 95? Because the maximum is 100 characters. If I have a maximum of 5 
                    spaces, the maximum case of 95 + 5 would make 100.
            """
            MAX_RECV = ENVIROMENT['MAX_LINES_TO_SEND'] * 110
            
            while True:
                conn, _ = sock.accept()                                 # Accept a client
                with conn:
                    while True:                                         # Loop until the connection is close
                        data = conn.recv(MAX_RECV).decode() 
                        
                        if not data:                                    # Close connection
                            break   
                        
                        lines = [ i for i in data.split("\n") if i]    # Take a list of strings separated by the '\n' character and ignore empty items
                        
                        weighting:str = self.process_data(lines)        # Process data
                        
                        if weighting: 
                            conn.sendall(weighting.encode())            # Send response to client      
                              
                    
        

    def process_data(self,lines:str) -> str:
        """
            Process the received data and provide a response regarding the weighting of the strings
                - This method receives the data separated by '\\n' and calculates the weighting, 
                returning it in a string separated by the same character ('\\n')
        """
        weighting = ""
        for line in lines:
            if "aa" in line.lower():                                        # This way, the cases: [aa,aA,Aa,AA] are covered  
                logging.warning(f"Double 'a' rule detected >> '{line}'") 
                weighting += "1000\n"
            else:
                try:                                                                        # Try For invalid strings where there are no spaces ( division by zero )
                    count_letters = sum(caracter.isalpha() for caracter in line )           # Get letters counter
                    count_numbers = sum(caracter.isnumeric() for caracter in line )         # Get numbers counter
                    count_spaces = sum(caracter.isspace() for caracter in line )            # Get spaces counter
                    metric:float = (count_letters *1.5 + count_numbers*2)/count_spaces      # Apply weighting formula
                    metric = round(metric,3)                                                # Only take 3 decimal places
                    weighting += f"{metric}\n"                                              # Save as string
                except:
                    weighting += "0\n"                                                      # Return 0 for this data if there is any error 
        return weighting
    