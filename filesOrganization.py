import os

#create a new directory for each website..
def mkdir(dirictory):
    if not os.path.exists(dirictory):
        os.mkdir(dirictory)

def touch(directory, base_url):
    wait_list_file = os.path.join(directory, 'waiting.txt')
    crawled_file = os.path.join(directory, 'crawled.txt')
    
    if not os.path.exists(wait_list_file):
        write(wait_list_file, base_url)
   
    if not os.path.exists(crawled_file):
        write(crawled_file, '')
        


def write(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data + '\n')


def write_set(file_path, set):

    with open(file_path, 'w') as file:
        for url in set:
            file.write(url + '\n')


def read(file_path):
    temp_Set = set()
    with open(file_path, 'r') as file:
        for url in file:
            temp_Set.add(url.replace('\n', ''))

    return temp_Set
            

def append(file_path, data):
    with open(file_path, 'a') as file:
        file.write(data + '\n')

def clear(file_path):
    if os.path.exists(file_path):
        os.unlink(file_path)

