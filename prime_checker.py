def is_prime(n) :
    
    if n<2 :
        return False
    for i in range(2,n) :
        if n%i == 0 :
            return False
    return True

while True :
    try :
        num = int(input("enter the number to check :  "))
        break
    except ValueError :
        print("please try again")

result = is_prime(num)
print(result)