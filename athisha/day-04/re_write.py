"""3. Please Re-write to disk."""
import json  # json library imported
# Define the dictionary
my_dict = {"Name": "Syam", "Age": 20, "remarks": "Modified"}

# Open the file in append mode
with open(r"E:\zlight\2023-bm-batch-01\athisha\day-04\file_Re-write_read.txt", 'a') as file:
    # Convert the dict to a string ,json.dumps() written to a file called file_Re-write_read.txt
    data = json.dumps(my_dict)
    file.write(data)  # The string to the file
    print("hi")


# Note:  Include Exception handling, proper comments and meaningful variable names

"""Exceptions: Exceptions are raised when the program is syntactically correct, but the code resulted in an error. 
This error does not stop the execution of the program, however, it changes the normal flow of the program.

example


import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug('This message should go to the log file')

try:    
    1/0
except Exception as e:
    logging.exception(e)"""
