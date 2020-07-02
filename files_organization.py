import os

# Create a new dirictory
def mkdir(dirictory):
    if not os.path.exists(dirictory):
        os.mkdir(dirictory)

# Create a new txt file
def touch(directory, base_url):
    wait_list_file = os.path.join(directory, 'waiting.txt')
    crawled_file = os.path.join(directory, 'crawled.txt')
  
    if not os.path.exists(wait_list_file):
        write(wait_list_file, base_url)
   
    if not os.path.exists(crawled_file):
        write(crawled_file, '')       

# Override on a file with a string
def write(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data + '\n')

# Override on a file with a set
def write_set(file_path, links):
    clear(file_path)
    with open(file_path, 'w') as file:
        for url in links:
            file.write(url + '\n')

# Read the data from a file, put each line in a set recored 
def read(file_path):
    temp_Set = set()
    with open(file_path, 'r') as file:
        for url in file:
            temp_Set.add(url.replace('\n', ''))

    return temp_Set
            
# Append a string to a file 
def append(file_path, data):
    with open(file_path, 'a') as file:
        file.write(data + '\n')

# Delete a file
def clear(file_path):
    if os.path.exists(file_path):
        os.unlink(file_path)

