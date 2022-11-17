def array_diff(a, b):
    for i in b:
        while i in a:       #loop is to be used, not 'if' as remove method deletes only first instance found
            a.remove(i)
    return a

if __name__ == '__main__':
    a=[1,2,2,2,3]
    b=[2]
    print(array_diff(a, b))