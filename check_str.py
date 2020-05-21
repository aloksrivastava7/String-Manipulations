'''

You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

OUTPUT FORMAT : In the first line, print True if string has any alphanumeric characters. Otherwise, print False.
                In the second line, print True if string has any alphabetical characters. Otherwise, print False.
                In the third line, print True if string has any digits. Otherwise, print False.
                In the fourth line, print True if string has any lowercase characters. Otherwise, print False.
                In the fifth line, print True if string has any uppercase characters. Otherwise, print False.

Sample Input : qA2

Sample Output : True
                True
                True
                True
                True                


'''

#PROGRAM

s = input()
if (s.isalnum() == True):
    print('True')
else :
    print('False')
flag2 = False    
for i in range(0,len(s)):
        
    if s[i].isalpha() :
        flag2 = True
        break    
    else :
        continue
if flag2 == True :
    print('True')
else :
    print('False')
flag3 = False    
for i in range(0,len(s)):
        
    if s[i].isdigit() :
        flag3 = True
        break    
    else :
        continue
if flag3 == True :
    print('True')
else :
    print('False')
flag4 = False    
for i in range(0,len(s)):
        
    if s[i].isupper() :
        flag4 = True
        break    
    else :
        continue
if flag4 == True :
    print('True')
else :
    print('False')
flag5 = False    
for i in range(0,len(s)):
        
    if s[i].islower() :
        flag5 = True
        break    
    else :
        continue
if flag5 == True :
    print('True')
else :
    print('False')                          
