def string_occurance(str1,str2):
    last_digit = str2[-1]
    occurance_count= 0
    for alp in str1:
        if alp==last_digit:
            occurance_count+=1
    return occurance_count

str1=input("Enter First String")
str2 = input("Enter second strig")
print(string_occurance(str1, str2)