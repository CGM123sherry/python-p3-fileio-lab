
# lib/file_io.py
def write_file(file_name, file_content):
   
    # my directory
    full_file_name = f"{file_name}.txt"
    
    # Opening the file in write mode ('w')
    with open(full_file_name, 'w') as file:
        file.write(file_content)


def append_file(file_name, file_content):
    
    # directory
    full_file_name = f"{file_name}.txt"
    
    # Opening the file in append mode ('a')
    with open(full_file_name, 'a') as file:
        file.write(file_content)

def read_file(file_name):
 
    # directory
    full_file_name = f"{file_name}.txt"
    
    # Open the file in read mode ('r')
    try:
        with open(full_file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: {file_name}.txt not found"
