def palindrome(s):
    return str(s) == str(s)[::-1]

s = int(input("enter a number: "))
print(palindrome(s))