def arifsequence(n, A):
    my_list = [int(a) for a in A.split(" ")]
    my_sorted_list =sorted(my_list)
    for i in range (0, n-2):
        #print (i)
        if my_sorted_list[i+1]-my_sorted_list[i] != my_sorted_list[i+2]-my_sorted_list[i+1]:
            return "no"
        else:
            continue

    return "yes"


if __name__ == '__main__':
    """
    n = int(input("Enter number of elements in array: "))
    A = input("Enter array elements separated by space: ")
    """
    n = int(input())
    A = input()

    print(arifsequence(n, A))