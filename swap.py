def swap_case(s):
    res=""
    for i in s:
        j=i 
        if j.isalpha():
            if j in i.lower():
                res=res+j.upper()
            if j in i.upper():
                res=res+j.lower()
        else:
            res=res+j
                
    return res
print(swap_case("Welcome to STEPIN programming!!!"))