import os


class envaironHandler():
    """
        This class allows handling environment variables stored in the .env file at the root of the project 
    """
    def __init__(self,filename:str = '.env'):
        self.__variables = {}                                                               # main variable
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))       # lead the absolute path of .env file
        env_path = os.path.join(project_root, filename)                                     # join absolute path with filename 
        
        # Line by line ignore the spaces, get a key,value of variables and save into main dict
        with open(env_path, 'r') as f:                  
            for line in f:                              
                line = line.strip().replace(" ", "")                                        # filter line      
                if not line or line.startswith('#'):                                        # pass comment and empty lines
                    continue
                key, value = line.split('=', 1)                                             # get key, value 
                try:
                    value = int(value)                                                      # try convert into int ( only int and string are used in the code)
                except:
                    pass                                                                    # if can not convert , is string 
                
                self.__variables[key] = value   
    
    def __getitem__(self, key: str):
        """
            Get items like dict
        """
        return self.__variables.get(key)
    
ENVIROMENT = envaironHandler()