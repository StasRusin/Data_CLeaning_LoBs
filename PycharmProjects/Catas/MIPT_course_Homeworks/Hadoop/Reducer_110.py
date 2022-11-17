import sys
from random import randint

def read_stdin():
    temp_list = []                    # list to store read keys from stdin before
    random_num = randint(1, 5)
    for line in sys.stdin:
        line = line[2:20]
        if len(temp_list) < random_num:
            temp_list.append(line)
        else:
            output_str = ','.join([str(item) for item in temp_list])
            print(output_str)
            temp_list.clear()
            random_num = randint(1, 5)

def read_file(file_path):

    with open(file_path, 'r') as file_read:
        lines = file_read.readlines()
        temp_list = []  # list to store read keys from stdin before
        random_num = randint(1, 5)
        for line in lines:
            line = line[2:20]
            if len(temp_list) < random_num:
                temp_list.append(line)
            else:
                output_str = ','.join([str(item) for item in temp_list])
                print(output_str)
                temp_list.clear()
                random_num = randint(1, 5)
        file_read.close()

if __name__ == '__main__':
    file_path = r"C:\Users\stasr\OneDrive\Data_Engineering\Keys_randoms.txt"
    read_file(file_path)