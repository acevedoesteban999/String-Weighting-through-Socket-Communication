# String Weighting through Socket Communication

### Overview

  >This project implements a system for calculating the weight of strings through socket communication, efficiently managing data transfer between a client and a server to enable dynamic calculations based on the transmitted strings

### Features

> - **Socket Communication**: Establishes a reliable connection between the client and server for data transfer.
> - **String Weighting Calculation**: Computes the weight of strings based on predefined criteria.
> - **Configurable Parameters**: Allows users to adjust parameters for string weighting calculations.
> - **Memory Optimization**: This project is optimized to minimize memory consumption, allowing for operation with a high data throughput without critically affecting dynamic memory

<br/>

<hr/>

## Getting Started

<hr/>

### Prerequisites

- Python: 3.10.10 (Libraries built-in)

### Installation

#### 1 . Clone the repository:    
    
    git clone https://github.com/acevedoesteban999/String-Weighting-through-Socket-Communication 

#### 2 . Create a .env file in the root of the project:

    HOST = localhost
    PORT = 8080
    MAX_LINES_TO_SEND = 100
    GENERATE_MAX_LINES = 1000
    READ_WRITE_MAX_LINES = 1000
    FILE_STRINGS = chains.txt
    FILE_RESPONSE = response.txt

#### 3 . Init Server
    
    python server.py
    
It should look something like: '*Server init on localhost:8080*'

#### 4 . Init Client:

    python client.py

It should look something like

    How many strings the file will contain?
        * Only integers are supported
        * Minimum 1 string
        * Maximum 1 000 000 strings

#### 5 . Insert string counter:

Wait for the process to finish and see something like:

     Process completed in [0.003992795944213867] seconds
When you reach this point, you will have two files: one with the generated strings and another with their weights
<br/>
<br/>
<hr/> 

###### Important

- The server only starts if a socket connection to the server is established, to avoid unnecessary work on the files
- The parameters MAX_LINES_TO_SEND and READ_WRITE_MAX_LINES are responsible for optimizing memory usage against speed
-  Since the maximum is 1 million possible lines, and each line has a maximum of 100 characters, this amounts to 100 million bytes, or 100 MB. To avoid this large memory usage, both in the generation of the strings, writing, reading, and transmission, it is divided into portions and will be processed cyclically to optimize the use of dynamic memory. 

<hr/>