import logging
import random
import string

WORD_MIN_LEN = 50
WORD_MAX_LEN = 100

class fileHandler():
    def __init__(self,filename:str = "chains.txt"):
        self._filename = filename
    
    def get_filename(self):
        return self._filename
    
    
    @staticmethod
    def add_spaces_to_word(word):
        """
            Add 3-5 blank spaces to a word
                *Do not add at the beginning or end, nor consecutive blank spaces
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
            word = word[:_pos] + ' ' + word[_pos:]                              #insert sections into word
        
        return word
    
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
    
        strings = [self.add_spaces_to_word(self.generate_word()) for i in range(count_str)]
        
        with open(self._filename, 'w') as file:
            for line in strings:
                file.write(line+ "\n")
        