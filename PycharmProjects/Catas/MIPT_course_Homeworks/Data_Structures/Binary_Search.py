import sys

def binary_search1(n, sorted_list, thought_num):
    thought_num = int(thought_num)
    sorted_list_int = [int(i) for i in sorted_list.split(' ')]      # using list comprehension to perform conversion
    left_border = 0
    right_border = len(sorted_list_int)
     #two following ifs are check of extremal values (out of range values)
    if thought_num > sorted_list_int[right_border-1]:
        return right_border
    if thought_num < sorted_list_int[0]:
        return 0
    while not (right_border - left_border == 1 or right_border - left_border == 0):
        med_val = int(int(left_border + right_border) / 2)
        print(f"med_val init= {med_val}")
        if thought_num < sorted_list_int[med_val]:
            right_border = med_val
            print(f"right_border = {right_border}")
            print(f"med_val from right= {med_val}")
        elif thought_num > sorted_list_int[med_val]:
            left_border = med_val
            print(f"left_border = {left_border}")
            print(f"med_val from left= {med_val}")
        else:
            return med_val
    else:
        #sys.stdout.write(str(pot_position))
        return right_border

if __name__ == '__main__':
    """
    n = input('Number of elements in the array: ')
    sorted_list = input('Enter array elements separated with spaces: ')
    thought_num = input('Number thought by Alice: ')
    """
    n = input()
    sorted_list = input()
    thought_num = input()

    print(binary_search1(n, sorted_list, thought_num))
