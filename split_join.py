'''

You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Sample Input : this is a string

Sample Output : this-is-a-string

'''

#PROGRAM

def split_and_join(line):
    ls = line.split(' ')
    return('-'.join(ls))
line = input()
result = split_and_join(line)
print(result)
