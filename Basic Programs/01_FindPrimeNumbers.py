def check_prime(n):
    if n <2:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if i % n == 0:
            return False
    return True 

if check_prime(1):
    print("this is prime number")
else:
    print("this is not a prime number") 
    

