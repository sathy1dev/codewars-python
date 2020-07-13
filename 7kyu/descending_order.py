# PROBLEM: 
# Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

#example input : 42145 , expected output : 54421

#function 
def descending(number):
    #first let's convert this number into a list
    list_strings = list(map(int,str(number)))

    #changing our list in descending order
    list_strings.sort(reverse = True)

    #now we have to combine our list together and make it as integer type
    #we make all the integers in our list as individual strings
    strings = [str(i) for i in list_strings]

    #joining our invidual characters together and we have to convert it into integer
    joined_strings = int("".join(strings))

    
    return joined_strings

#driver code
number = int(input('Enter your number \t'))
print('The descending order of your number is ',descending(number))