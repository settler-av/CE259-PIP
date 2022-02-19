# link : https://www.hackerrank.com/challenges/py-the-captains-room/problem
# read the k and arr in single line
k,arr = int(input()),list(map(int, input().split()))
# convert the arr to set
myset = set(arr)
# the main logic

print("Sum of myset: ",sum(myset)*k)

print("Sum of k: ",sum(arr))
# print(((sum(myset)*k)-(sum(arr)))//(k-1))