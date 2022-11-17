from random import seed
from random import randint

def read_file(file_path):
    with open(file_path, 'r') as file_content:
        #numb_elem = file_content.read.s
        my_list = file_content.readline(2)
        for l in file_content.readlines():
            print(l)
    print (numb_elem)
    print(my_list)

def sorted_unique_int_generator(interval_start, interval_finish):
    my_list = list()
    for _ in range (7954):
        value = randint(interval_start, interval_finish)
        my_list.append(int(value))
    my_list = sorted(my_list, reverse=False)
    my_set = set(my_list)
    print(len(my_set))
    print(my_set)               # this will prtint elements separated with coma
    """
    for elem in my_set:         # this is a column print   
        print( str(elem) )
    """
    my_str = str(my_set)
    my_str = my_str[1 : len(my_str) - 1 ]
    print(my_str.replace(',',''))
    return

def is_unique_counts(A):            # A is a string elements to be spilt with space
    my_dict = {}
    #my_list = [int(i) for i in A.split(' ')]
    my_list = [i for i in A.split(' ')]
    #print(my_list)
    for a_element in my_list:
        print(f"a_element= {a_element}")
        my_dict[a_element] = my_list.count(a_element)
        for k in range (1, my_list.count(a_element)+1):
            my_list.pop(my_list.index(a_element))
        print(f"my_dict = {my_dict}")
        #my_list.pop(my_list.index(a_element))

        print(f"my_list {my_list}")
    print(f"my_dict = {my_dict}")

if __name__ == '__main__':
    #file_path = 'C:/Users/stasr/OneDrive/Data_Engineering/bin_search.txt'
    #file_path = 'C:\\Users\\stasr\\OneDrive\\Data_Engineering\\bin_search.txt'
    #my_list = [int(i) for i in random(-10000, -1) ]

    #sorted_unique_int_generator(-10000, 10000)
    A = input("Enter arraly elements sepaprated by space ")
    print(is_unique_counts(A))