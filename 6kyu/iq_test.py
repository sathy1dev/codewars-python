#problem:
"""
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

 ->Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
"""

#example input(" 2 4 7 8 10 ") -> expected position is 3, since it is a iq test index starts from 1

#function
def iq_test(numbers):
    list_strings = numbers.split(" ")

    #list of strings to list of integer conversion
    list_strings = [ int(i) for i in list_strings]
    #counting number of odd values and even values in the list
    odd_count, even_count = 0, 0

    #finding number of odd and even  numbers in the given list
    for i in range(0 , len(list_strings)):
        if list_strings[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    if odd_count < even_count:
        odd_no = list(filter(lambda x : (x % 2 != 0), list_strings))
        print(int((list_strings.index(odd_no[0])) + 1))
    else:
        even_no = list(filter(lambda x : (x % 2 == 0), list_strings))
        print(int((list_strings.index(even_no[0]))+1))

    """
        code wars solution:
        def iq_test(numbers):
             e = [int(i) % 2 == 0 for i in numbers.split()]
             return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1

    """ 
    
    


numbers = "1 2 1 1"

iq_test(numbers)