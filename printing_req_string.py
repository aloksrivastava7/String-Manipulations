'''

You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.

Sample Input : Ross
               Taylor

Sample Output : Hello Ross Taylor! You just delved into python.

'''

#PROGRAM

def print_full_name(a, b):
    print("Hello",a,b+'!','You just delved into python.')


first_name = input()
last_name = input()
print_full_name(first_name, last_name)
