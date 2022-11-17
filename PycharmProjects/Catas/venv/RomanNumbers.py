def solution(roman):
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = max_n = 0
    for c in reversed(roman):
        n = symbols[c]
        #result += n if n >= max_n else -n
        result = result+n if n >= max_n else -n
        print("itereation run=" + str(n) + " result=" + str(result))
        max_n = max(max_n, n)
    return result

if __name__ == '__main__':
    roman = "IX"
    print(solution(roman))

