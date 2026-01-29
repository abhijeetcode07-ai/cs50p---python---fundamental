def main() :
    while True :
        try :
            num = int(input("Enter the number :  "))
            if num == 0 :
                print("zero division is not allowed")
                continue
            return divide_table(num)
        except ValueError :
            print("invalid input please try again ")
        
def divide_table(n) :
    for i in range(1,11) :
        print(f"{n}/{i} = {n/i}")
         
main()