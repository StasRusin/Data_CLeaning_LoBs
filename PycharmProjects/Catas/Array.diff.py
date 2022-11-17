def array_diff(a, b):
  #your code here
    for i in b:

        if i in a:
            num_i = a.count(i)              # variable to store number of instances in minuend
                                            # считаем количество вхождений данного элемента в уменьшаемое
            print(i)
            print(num_i)

            for k in range(1, num_i+1):
                a.remove(i)
                k=k+1
    print("print in the end of function")
    print(a)
    return a

if __name__ == '__main__':
    a=[1,2,2]
    b=[1]
    print(array_diff(a, b))
