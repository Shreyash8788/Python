def find_prime(n):
    if n < 2:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

lst =[1,2,3,4,5,6,7,8,9,10]

prime = [num for num in lst if find_prime(num)]

print(prime)
    
