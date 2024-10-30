import logging
import random
import string

WORD_MIN_LEN = 50
WORD_MAX_LEN = 100
GENERATE_MAX_LINES = 1000
READ_MAX_LINES = 2

class fileHandler():
    """
        Static class for management files
    """    
    @staticmethod
    def add_spaces_to_word(word:str) ->str:
        """
            Add 3-5 blank spaces to a word
                - Do not add at the beginning or end, nor consecutive blank spaces
        """
        spaces = random.randint(3, 5)                                           #generate numbers of spaces to insert
        """
            To avoid spaces at the beginning and end, the range is from [1, max-1], and to prevent 
            having 2 consecutive spaces, I take the odd (or even, there’s no difference) values that remain, 
            so the possible blank spaces will always be separated by at least an even number
        """
        available_positions = [i for i in range(1,len(word)-1) if i%2 != 0]       
        pos = random.sample(available_positions, spaces)                        # choise a random positions
        for _pos in sorted(pos):        
            word = word[:_pos] + ' ' + word[_pos:]                              # insert sections into word
        
        return word
    
    @staticmethod
    def generate_word()->str:
        """
            Generate a random word only with ['a-z', 'A-Z', '0-9'] 
                - The range defined by the constants WORD_MIN_LEN and WORD_MAX_LEN
        """
        valid_caracters = string.ascii_letters + string.digits 
        return ''.join(random.choice(valid_caracters) for _ in range(WORD_MIN_LEN,WORD_MAX_LEN))
   
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
    def generate_strings_file(filename:str = "chains.txt",separator = '\n') ->None:
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
        with open(filename, 'w') as _:   
            pass
        
        
    
        # Number of cycles to reach the highest value of GENERATE_MAX_LINES without exceeding
        for _ in range(int(count_str/GENERATE_MAX_LINES)):
            fileHandler.__generate_and_write(filename,separator,GENERATE_MAX_LINES)
        
        # Remaining words that need to be generated; this number is less than GENERATE_MAX_LINES
        fileHandler.__generate_and_write(filename,separator,count_str%GENERATE_MAX_LINES)
        
    
    @staticmethod
    def read_strings_from_file(line_count:int,filename:str = "chains.txt",separator = '\n') -> str:
        """
            Read strings from file  
                - Filename is a name of file to read
                - The separator is a character for splitting the reads 
        """
        lines = []
        current_line_number = 0
        with open(filename, 'r') as file:
            while True:
                for _ in range(line_count):
                    if not file.readline():
                        return lines,line_count,True  
                for _ in range(READ_MAX_LINES):
                    _line = file.readline(106)
                    print(_line)
                    if not _line:
                        return lines,line_count,True
                    lines.append(_line)
                    line_count+=1
                return lines,line_count,False
                
    @staticmethod
    def write_strings_into_file(data:list,filename:str = "response.txt",separator = '\n') -> None:
        """
            Write strings into file 
             
        """
        _data = [i + separator for i in data]
        with open(filename, 'w') as file:
            file.writelines( _data )
    
    