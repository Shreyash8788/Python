def is_palindrome(s):
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        
        left+=1
        right-=1
    return True

if is_palindrome("nitiin"):
    print("this is a palindrome")
else:
    print("this is not palindrome")
    

        