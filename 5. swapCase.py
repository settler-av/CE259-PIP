'''
Function to swap the case of all letters in a string.
i.e. 'Hello World' becomes 'hELLO wORLD'.
'''


def swap_case(x):
    ans = list(x)

    # iterate through each character in the string
    for i in range(len(x)):
        # if the character is a lowercase letter, convert to uppercase
        if x[i].isupper():
            ans[i]= (x[i].lower())
        # vise versa
        else:
            ans[i] = (x[i].upper())
    return ''.join(ans)


# dirver code starts here
if __name__ == '__main__':
    s = input()
    ans = swap_case(s)
    print(ans)
