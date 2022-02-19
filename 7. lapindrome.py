# By 20CE155 ADNAN VAHORA
# Run a for loop for each testcase
for _ in range(int(input())):
    s = input()
    # slice the string according to the length of the string
    if len(s)%2 == 0:
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:]
    elif len(s)%2 == 1:
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2+1:]
    # convert the string to list
    l1, l2 = list(s1), list(s2)
    # sort the list
    l1.sort(), l2.sort()
    # if both sorted list are equal then it is a palindrome
    if l1 == l2:
        print("YES")
    else:
        print("NO")
