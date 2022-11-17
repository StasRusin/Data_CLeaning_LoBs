def intssquaresmatrix (m, n):
    for ver_l in range(0,n):
        current_list = list()       # creating a new list
        current_list.append(ver_l**2)
        for k in range(1, m):
            #print(f"ver_l= {ver_l}, k={k} hor_l = k*(n+ver_l)")
            hor_l = (k*n)+ver_l
            current_list.append(hor_l ** 2)
        ver_l = ver_l + 1
        print(f"current_list {current_list}")

if __name__=='__main__':
    intssquaresmatrix(4, 6)