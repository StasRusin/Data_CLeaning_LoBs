import sys
from random import randint

def reading_stdin_word_count():
    for line in sys.stdin:
        words = line.strip().split()
        for word in words:
            print(f"({word},\t1)")

#reading from file instead of reading from stdin (rehearsle)
def reading_text_file_word_count(file_path):
    with open(file_path, 'r') as file_read:
        lines_read = file_read.readlines()
        for line in lines_read:
            words = line.strip().split(" ")
            for word in words:
                print(f'({word},\t1)')
    file_read.close()

def reading_keys_stdin():
    for key in sys.stdin:
        key = str( str(randint(1, 5)) + " " + key )
        print(key)

def reading_keys(file_path):
    with open(file_path, 'r') as file_read:
        keys = file_read.readlines()
        for key in keys:
            key = str( str(randint(1, 5)) + " " + key )
            key = key[0:20]
            print(f"new key: {key}")
    file_read.close()

def reading_file_chunk(file_path):              # reading file portionally instaed of full read to save cache
    chunk_size = 17                             # setting shuck size in bytes
    with open(file_path, 'r') as file_read:
        chunk = file_read.read(chunk_size)              # reading file 20 bytes by 20 bytes file_read.read(20)
        while chunk:
            print(chunk)
            chunk = file_read.read(chunk_size)


if __name__ == '__main__':
    # file for word count exercise
    # file_path = r"C:\Users\stasr\OneDrive\Data_Engineering\bin_search.txt"
    # reading_text_file_word_count(file_path)

    file_path = r"C:\Users\stasr\OneDrive\Data_Engineering\keys.txt"
    #reading_file_chunk(file_path)
    reading_keys(file_path)
    #reading_keys_stdin()