def check_password() :
        password = input("enter the password :  ")
        
        if len(password)<8 :
            return False
        
        has_alpha = False
        has_digit = False

        for ch in password :
            if ch.isaplha() :
                has_alpha = True
            if ch.isdigit() :
                has_digit = True

        

        if has_alpha  and has_digit :
            return "strong"
        else :
             return "weak"

result = check_password()
print(result)