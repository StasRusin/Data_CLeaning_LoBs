def first_non_repeating_letter(string):
# special cases section. special cases are:
    if len(string)==0:                                          # 1) empty string
        return ''
    elif len(string)==1:                                        # 2) string of one character
        return string
    else:
        processed_chars=list()                                  #creating list to store processed characters
        for i in range(0, len(string)):
            if string[i] in processed_chars:
                i+=1
            else:
                if string.find(string[i].upper(), i+1) ==-1 and string.find(string[i].lower(), i+1) ==-1:
                    return string[i]
                else:
                    processed_chars.append(string[i])
                    i+=1
        else:
            return ''


if __name__ == "__main__":
    string = input("Введите тестовую строку ")
    print(first_non_repeating_letter(string))