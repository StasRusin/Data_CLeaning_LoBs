import time
def sum_dividers(q):
    sum_of_dividers=1
    div_list = [1]
    for i in range(2, int(q**0.5+1), 1):
        if q % i == 0 and i != q/i:
            div_list.append(i)
            div_list.append(q//i)
            sum_of_dividers = sum_of_dividers + i + q//i
    print(div_list)
    print("sum_of_dividers = " + str(sum_of_dividers))
    return sum_of_dividers

def buddy(start, limit):
    for n in range(start, limit, 1):
        print("n=" + str(n))
        m = sum_dividers(n) - 1
        if m>n:
            print("sum_dividers(m)-1 =" + str(sum_dividers(m) - 1))
            if sum_dividers(m) - 1 == n:
                return [n, m]
                break
    return "Nothing"

if __name__ == '__main__':
    launch_time = time.time()

    start = int(input("Введите начало интервала" ))
    limit = int(input("Введите верхнюю границу интервала"))
    print(buddy(start, limit))
    print(time.time() - launch_time)