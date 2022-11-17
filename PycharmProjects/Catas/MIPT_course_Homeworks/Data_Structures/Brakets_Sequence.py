def brackets_sequence(s):
    s=s.replace(' ','')
    if len(s) <= 1:
        print("no")
        return
    corr_sequence = { ")":"(", "]":"[", "}":"{" }
    my_steak = list()
    for st in s:
        if st in corr_sequence and my_steak[len(my_steak)-1] == corr_sequence[st]:
            my_steak.pop()
        else:
            my_steak.append(st)
    if len(my_steak) == 0:
        return "yes"
    else:
        return "no"

if __name__ == "__main__":
    #s = input ("Enter brackets sequence as a string: ")
    s = input()
    print (brackets_sequence(s))