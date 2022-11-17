"""
Create 'decoded' list from 'encoded'
Example:
encode_list = [0, [1, 2], 4, [1, 0, 3]]
decode_list = [0, 1, 2, 4, 1, 0, 3]
"""

def decode_list (encode_list):
    decoded_list = list()
    for elem in encode_list:
        if elem.__class__ != list:
            decoded_list.append(elem)
        else:
            for elem1 in elem:
                decoded_list.append(elem1)
    return  decoded_list

if __name__ == '__main__':
    encode_list = [0, [1, 2], 4, [1, 0, 3]]
    print(f"decode_list {decode_list (encode_list)}")