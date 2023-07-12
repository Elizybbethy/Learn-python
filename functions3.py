def add(cup1,cup2):
    cup3 = cup1 + cup2
    print(cup3)
    
def sub(cup1,cup2):
    cup3 = cup1 - cup2
    print(cup3)

#Allowing/Forcing functions to communicate.
def add2(cup1,cup2):  #cup1 & cup2 are called paramenters
    cup3 = cup1 + cup2
    print(cup3)
    return cup3  
    
'''
This gives out the number to follwing function.
Return makes the end of excuation
'''

def sub2(cup1):
    cup3 = add2(5,25) - cup1
    print(cup3)
sub2(10) # the vales in () are called arguements like(10) (2,25) or actual/formal paramenters.

add2(1,3)
ans = add2(6,1)
print(ans)
print(add2(2,6))