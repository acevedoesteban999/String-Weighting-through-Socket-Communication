import logging
import random
import string
from typing import Union
from .environ_handler import ENVIROMENT


class fileHandler():
    """
        Static class for management files
    """    
    @staticmethod
    def add_spaces_to_word(word:str) ->str:
        """
            Add 3-5 blank spaces to a word randomly
                - This method not add at the beginning or end, nor consecutive blank spaces
                - To avoid spaces at the beginning and end, the range is from [1, max-1], and to prevent 
            having 2 consecutive spaces, I take the odd (or maybe even) values that remain, 
            so the possible blank spaces will always be separated by at least an even number
        """
        spaces = random.randint(3, 5)                                           # Generate numbers of spaces to insert
        
        # Avoid spaces using odd number and [1,max-1] range
        available_positions = [i for i in range(1,len(word)-1) if i%2 != 0]       
        pos = random.sample(available_positions, spaces)                        # Choise a random positions
        for _pos in sorted(pos):        
            word = word[:_pos] + ' ' + word[_pos:]                              # Insert sections into word
        
        return word
    
    @staticmethod
    def generate_word()->str:
        """
            Generate a random word only with ['a-z', 'A-Z', '0-9'] 
        """
        valid_caracters = string.ascii_letters + string.digits 
        return ''.join(random.choice(valid_caracters) for _ in range(50,95))    #   Max range is 95 because the maximum is 100 characters. If I have a maximum of 5 spaces, the maximum case of 95 + 5 would make 100.
   
    @staticmethod
    def __generate_and_write(filename:str,separator,_range):
            """
                This Internal function only generate the word and write into file 
            """
            # Generate and add spaces with 
            strings = [fileHandler.add_spaces_to_word(fileHandler.generate_word() + separator) for _ in range(_range)]
            # Write data
            with open(filename, 'a') as file:   
                file.writelines(strings)
    
    @staticmethod
    def generate_strings_file(filename:str = ENVIROMENT['FILE_STRINGS'],separator = '\n') ->None:
        """
            Read the strings and save them in a file
                - The number of readings is defined at execution time with the 'input' Python method.
                - The separator is the character used to separate one item from another
                
            Important!
                - Since the maximum is 1 million possible lines, and each line has a maximum of 
            100 characters, this amounts to 100 million bytes, or 100 MB. To avoid this 
            large memory usage, it will be divided into VAR_GLOBAL segments, saved to the 
            file, and continuously generated until the target quantity is reached
                - To apply the division in equal cycles and write each GENERATE_MAX_LINES,
            the division of the number of times GENERATE_MAX_LINES fits into cont_str 
            tells me how many cycles of GENERATE_MAX_LINES I need to perform. For the 
            final cycle, which may have fewer values than GENERATE_MAX_LINES, the remainder 
            of the division tells me how many additional words I need to reach cont_str exactly
            
        """
        # Select the string counter
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
        
        #First clear the file 
        fileHandler.clear_file(filename)
        
        
    
        # Number of cycles to reach the highest value of GENERATE_MAX_LINES without exceeding
        for _ in range(int(count_str / ENVIROMENT['GENERATE_MAX_LINES'])):
            fileHandler.__generate_and_write(filename,separator,ENVIROMENT['GENERATE_MAX_LINES'])
        
        # Remaining words that need to be generated; this number is less than GENERATE_MAX_LINES
        fileHandler.__generate_and_write(filename,separator,count_str % ENVIROMENT['GENERATE_MAX_LINES'])
        
    
    @staticmethod
    def read_strings_from_file(line_count:int,filename:str = ENVIROMENT['FILE_STRINGS']) -> tuple[list,int]:
        """
            Read strings from file  
                - Filename is a name of file to read
              
            Important!
                - Since the maximum is 1 million possible lines, and each line has a maximum of 100
                characters, this amounts to 100 million bytes, or 100 MB. To avoid this large memory
                usage, only each READ_WRITE_MAX_LINES will be read, and a counter of where it left 
                off will be returned so that it can be used at another time
        """
        lines = []
        with open(filename, 'r') as file:               # Open file in read mode 
            for _ in range(line_count):                 # Pass all lines readed
                if not file.readline():                 # return if is end of file
                    return lines,line_count  
            
            for _ in range(ENVIROMENT['READ_WRITE_MAX_LINES']):       # read READ_WRITE_MAX_LINES lines 
                _line = file.readline(106)
                if not _line:                           # return if is end of file
                    return lines,line_count
                
                lines.append(_line)                     # save line readed
                line_count+=1                           # increment count
                
            return lines,line_count
                
    @staticmethod
    def clear_file(filename:str):
        with open(filename, 'w') as _:   
            pass
    
    @staticmethod
    def write_strings_into_file(data:list,filename:str = ENVIROMENT['FILE_RESPONSE'],separator = '\n') -> None:
        """
            Write strings into file 
            
            Important!
                - Since the maximum is 1 million possible lines, and each line has a maximum of 100
                characters, this amounts to 100 million bytes, or 100 MB. To avoid this large memory
                usage, it will only write in append mode READ_WRITE_MAX_LINES lines
        """
        _data = [i + separator for i in data]   # Put separator after write
        with open(filename, 'a') as file:
            file.writelines( _data )
    
    