n = input()
A = input()

my_list = [int(i) for i in A.split(' ')]
my_dict = {}

for a_element in my_list:
    if a_element not in my_dict:
        my_dict.setdefault(a_element, [1,])
    else:
        my_dict[a_element].append(1)
#print(f"my_dict {my_dict}")
for my_dict_elem in my_dict.keys():
    my_dict.update( {my_dict_elem : len(my_dict.get(my_dict_elem))} )

#print(f"my_dict after update {my_dict}")
my_dict_1  = {v: k for (k, v) in my_dict.items()}
#print(f"my_dict1 {my_dict_1}")
"""Затем вам надо определить уникальность значений из первого словаря - 
для этого снова используйте словарь, 
где ключи - это значения из первого словаря, а значения - это количество их появлений среди значений первого словаря
"""
if len(my_dict_1) == len(my_dict):
    print("YES")
else:
    print("NO")