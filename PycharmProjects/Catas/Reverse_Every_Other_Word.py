def reverse_alternate(string):
    # your code here
    init_str_lenhgth = len(string)  # variable to store length of string

    if len(string) == 0:
        return ""
    else:
        while (string[0] == " "):
            string = string[1:]
            if len(string) == 0:
                return ""

        while (string[len(string) - 1] == " "):
            string = string[:init_str_lenhgth - 1]

        if len(string) == 0:
            return ""

        func_list = []
        func_list = string.split()
        number_of_elements = len(func_list)

        i = 1
        while i <= number_of_elements - 1:
            reversed_item = func_list[i][::-1]
            func_list[i] = reversed_item
            i = i + 2

        res_string = ""
        res_string = " ".join(func_list)
        return res_string
# main function should not be passed to CodeWars
if __name__ == '__main__':
    test_string="This si not a test "
    print(len(test_string))
    print(reverse_alternate(test_string))