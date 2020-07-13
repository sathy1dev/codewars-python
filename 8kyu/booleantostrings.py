#problem:
#Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

#function to convert boolean to word
def booleantoword(boolean):
    if boolean == True:
        return str('Yes')
    else:
        return str('No')




#driver code
boolean = False
print(booleantoword(boolean))