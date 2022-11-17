"""
Algorithm to find sublists:
Run one loop in the range of 0 to length of the list.
Run one inner loop in the range of current outer loop to length of the list.
Get the slice of the list in between the current indices pointed by the outer loop and inner loop.
"""

def sublist(nucleotides):
    for outer_left in range(0, len(nucleotides)):
        for inner_right in range(len(nucleotides), 0, -1):
            if inner_right > outer_left:
                #print ("outer_left=" + str(outer_left) + "; inner_right=" + str(inner_right))
                print(nucleotides[outer_left : inner_right])

if __name__ == '__main__':
    nucleotides = ["A", "T", "G", "C"]
    sublist(nucleotides)