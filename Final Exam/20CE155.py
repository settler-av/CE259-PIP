"""
A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.


Following are the criteria for checking the password:
At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]

Minimum length of transaction password: 6
Maximum length of transaction password: 12

Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.

Input:
ABd1234@1,a F1#,2w3E*,2We3345
Output
ABd1234@1
"""
import string

'''
By - 20CE155 ADNAN VAHORA
SUBJECT: CE259-PIP
INPUT: ABd1234@1,a F1#,2w3E*,2We3345
OUTPUT: ABd1234@1

coding standards - PEP8
'''


def contains_any(test_str, char_list):
    return True in [c in test_str for c in char_list]


if __name__ == "__main__":
    special_char = ['$', '#', '@']
    out_list = []
    for password in input("Enter the password: ").split(','):
        test_conditions = [6 <= len(password) <= 12,
                           contains_any(password, string.ascii_lowercase),
                           contains_any(password, string.ascii_uppercase),
                           contains_any(password, string.digits),
                           contains_any(password, special_char)]
        if all(test_conditions):
            out_list.append(password)
    print(','.join(out_list))
