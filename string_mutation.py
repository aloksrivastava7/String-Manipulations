'''

Read a given string, change the character at a given index and then print the modified string.

Sample Input : abracadabra
               5 k

Sample Output : abrackdabra

'''

#PROGRAM

def mutate_string(string, position, character):
    ls = list(string)
    ls[position] = character
    ss = ''.join(ls)
    return ss


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)
