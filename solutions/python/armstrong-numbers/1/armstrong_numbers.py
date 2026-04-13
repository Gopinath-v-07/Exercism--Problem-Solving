def is_armstrong_number(number):
    num_str=str(number)
    num_len=len(num_str)
    total=0
    for i in num_str:
        total+=int(i)**num_len
    if total==number:
        return True
    else:
        return False
        
