# created by M7md-5shbh
# checks if a number is prime or not
#--------------------------------------------

def is_prime(num):
    divisable = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisable += 1
    
    if divisable == 2:
        return True
    if divisable > 2:
        return False

print(is_prime(73))
