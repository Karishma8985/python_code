def string_test(s):
    a = { "Lower_Case":0 , "Upper_Case":0} #intiail count of lower and upper
    for ch in s: #for loop
        if(ch.islower()): #if-elif-else condition
            a["Lower_Case"] = a["Lower_Case"] + 1
        elif(ch.isupper()):
            a["Upper_Case"] = a ["Upper_Case"] + 1
        else:
            pass



print("String in testing is:  ",string_test(v)) #printing the statements.
print("Number of Lower Case characters in String: ",string_test.a["Lower_Case"])
print("Number of Upper Case characters in String: ",string_test.a["Upper_Case"])