#problem:
"""
Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

correct answer is 17, 24 total values -> 17 true and 7 false

"""
#function to count sheeps
def countingsheep(sheep_array):
    n = len(sheep)
    count = 0
    for i in range(0,n):
        if sheep_array[i] == True:
            count += 1

    #returning total number of sheeps
    return count        

#driver code
sheep = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ] 

#print
print('The correct answer would be ', countingsheep(sheep))