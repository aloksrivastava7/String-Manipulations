'''

You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

Sample Input : HackerRank.com presents "Pythonist 2"

Sample Output : hACKERrANK.COM PRESENTS "pYTHONIST 2"

'''

#PROGRAM

def swap_case(str):
    ss = str.swapcase()
    return ss


s = input()
result = swap_case(s)
print(result)
