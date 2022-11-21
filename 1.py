def convert_to_base3_number (num):
    if num == 0:
        return '0'
    vals = []
    while num:
        num, rem = divmod(num, 3)
        vals.append(str(rem))
    return ''.join(reversed(vals))

num=int(input("enter number "))
print(convert_to_base3_number(num))