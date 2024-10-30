import logging
import random
import string

WORD_MIN_LEN = 50
WORD_MAX_LEN = 100

class fileHandler():
    def __init__(self,filename:str = "chains.txt"):
        self._filename = filename
    
    @staticmethod
    def generate_word():
        """
            Generate a random word only with ['a-z', 'A-Z', '0-9'] 
                * The range defined by the constants WORD_MIN_LEN and WORD_MAX_LEN
        """
        valid_caracters = string.ascii_letters + string.digits 
        return ''.join(random.choice(valid_caracters) for _ in range(WORD_MIN_LEN,WORD_MAX_LEN))
    
    
    def generate_file(self):
        """
            Read the strings and save them in a file.
                - Use the 'input' method to read.
                - The number of readings is defined at execution time.
                - The file name is preconfigured.
        """
        count_str = 0
        while(True):
            try:
                count_str = int(input("How many strings the file will contain?\n\t* Only integers are supported\n\t* Minimum 1 string\n\t* Maximum 1 000 000 strings\n"))
            except:
                logging.error("\nThe answer is not a valid number. Please input a correctly formatted number of strings\n")
                continue
            
            if count_str > 1e6:
                logging.error("\nThe number of strings cannot be greater than 1,000,000\n")
                continue
            
            if count_str < 1 :
                logging.error("\nThe number of strings cannot be less than 1\n")
                continue
            
            break
    
        
        
        