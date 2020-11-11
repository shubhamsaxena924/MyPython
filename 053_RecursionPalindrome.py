#This program uses a recursove function to check whether a string is palindrome or not.
def palin(s):
    if(len(s)==0 or len(s)==1):
        return True
    else:
        if s[0]==s[-1]:
            return palin(s[1:-1])               #return string leaving first and the last element
        else:
            return False
str=input("Enter a string to check whether it is palindrome or not: ")
y=palin(str)
if(y):
    print("The string you entered is Palindrome.")
else:
    print("The string you entered is not a Palindrome.")
