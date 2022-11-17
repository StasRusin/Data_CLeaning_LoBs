def binary_tree(n, users_array):
    int_list = [ int(i) for i in users_array.split(' ') ]
    tree_dict = {}

    curr_depth = 0              #variable to store deepest leaf as of now
    for std_in_val in int_list:
        print(f"working with std_in_val: {std_in_val}")
        print(f"current depth: {curr_depth}")
        if curr_depth == 0:
            tree_dict.setdefault(std_in_val, [" ", " ", 0])
            #print( tree_dict.key(curr_depth) )
            print( tree_dict.get(curr_depth) )
        else:
            for list_leafs_elem in tree_dict.get(curr_depth):
                if list_leafs_elem[0] == " " and std_in_val > tree_dict.key(curr_depth):
                    list_leafs_elem = std_in_val[0]
                    #next(std_in_val)
                if list_leafs_elem[0] != " " and std_in_val > tree_dict.key(curr_depth):
                    curr_depth = curr_depth + 1
                    tree_dict.setdefault(list_leafs_elem, [std_in_val, " ", curr_depth])

                if list_leafs_elem[1] == " " and std_in_val < list_leafs_elem[1]:
                    list_leafs_elem = std_in_val[1]
                    #next(std_in_val)
                if list_leafs_elem[1] != " " and std_in_val < list_leafs_elem[1]:
                    curr_depth = curr_depth + 1
                    tree_dict.setdefault(list_leafs_elem, [" ", std_in_val, curr_depth])
    return tree_dict
        #if std_in_val < tree_dict.key[curr_depth]: # and tree_dict.get(curr_depth) != None:

def binary_tree1(n, users_array):
    int_list = [ int(i) for i in users_array.split(' ') ]
    tree_dict = {}
    curr_depth = 0

    for std_in_val in int_list:
        if len(tree_dict) == 0:
            tree_dict.setdefault(std_in_val, [0, 0, 0])
            #print( tree_dict.key(curr_depth) )
            print( tree_dict.get(curr_depth) )
        else:
            for curr_node in tree_dict.keys():
                print(f"curr_node: {curr_node}")
                print (f"curr_node_list: { tree_dict.get(curr_node) }")
                #for list_leafs_elem in tree_dict.get(curr_node):

                if std_in_val > curr_node and tree_dict[curr_node][1] ==0:
                    tree_dict[curr_node][1] = std_in_val
                    tree_dict.setdefault(std_in_val, [" ", " ", tree_dict[curr_node][2]+1] )
                if std_in_val < curr_node and tree_dict[curr_node][0] == 0:
                    tree_dict[curr_node][0] = std_in_val
                    tree_dict.setdefault(std_in_val, [" ", " ", tree_dict[curr_node][2] + 1])
    return tree_dict

if __name__ == '__main__':
    n = input("Enter number of array elements: ")
    users_array = input("Enter integers array separated by space: ")
    print(binary_tree1(n, users_array))