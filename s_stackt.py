# -*- coding: latin-1 -*-
'''
name: Alberto Ferreira de Melo Filho
course: Datastrukturer och algoritmer
Teacher: Johan Eliasson
date: 5 september 2013
python 3.3.2
Assignment 1
'''

from Stack1Cell import Stack1Cell
import sys

def stars(test):
    if (test == "slut"):
        print ("*************************************************")
        print ("")
    else:
        print ("****************"+test+"****************************")

#Test if the function Stack1Cell creates an empty stack
def test1():
    stars("Test1")
    Stack1Cell()
    print ("Test1 Success (Stack1Cell)! --> variable L is created")    
    stars("slut")
    
#Test if the variable L is empty *PS. There is no way to know if isempty works since you need to use another function as push, but then there is now way to know if push works! 
def test1_5():
    stars("Test2")
    L = Stack1Cell()
    print ("running ... testing if the stack is empty")
    if L.isempty() == True:
        print ("Test1_5 ... empty OK")        
    else:
        print ("Test1_5 (isempty) did NOT succeeded! --> the stack was NOT empty")
        sys.exit()
    stars("slut")


#Check if the variable L is empty
def test2():
    stars("Test2")
    L = Stack1Cell()
    test1 = 0
    test2 = 0
    print ("running ... testing if the stack is empty")
    if L.isempty() == True:
        print ("Test2/1 ... empty OK")
        test1 = 1
    else:
        print ("Test2/1 (isempty) did NOT succeeded! --> the stack was NOT empty")
        sys.exit()
    print ("running ... testing if the stack is NOT empty")
    L.push ("34")
    print ("pushing 34 to the stack")
    if L.isempty() == False:
        print ("Test2/2 ... NOT empty OK")
        test2 = 1
    else:
        print ("Test2/2 (isempty) did NOT succeeded! --> the stack was empty")
        sys.exit()
    if (test1 == 1 and test2 == 1):
        print ("Test2 (isempty) Success!")
    stars("slut")

#Add an element to the L variable and test if the stack is empty or not 
def test3():
    stars("Test3")
    L = Stack1Cell()
    test = 0
    if L.isempty() == False:
            print ("running ... the stack was NOT empty")
    else:
        print ("running ... the stack is empty")
        test = 1 
    L.push(34)    
    print ("Pushing...")
    if (L.isempty() == False and test == 1):
            print ("Test3 (push) Success! --> the stack was NOT empty")
    else:
        print ("Test3 (push) did NOT succeeded! --> the stack is empty")
        sys.exit()    
    stars("slut")
    
#Print out the last value added to the stack        
def test4():
    stars("Test4")
    L = Stack1Cell()
    L.push(34)
    print ("running ... pushing 34")
    if(L.top() != 34):
        sys.exit("Fail - The value is not the same as push")
    print ("the value of the last added item from the stack is "+ str(L.top()))
    L.push(76)
    print ("running ... pushing 76")
    print ("the value of the last added item from the stack is "+ str(L.top()))
    if (L.top() != 76):
        sys.exit("Fail - The value is not the same as push")
    L.push(6)
    print ("running ... pushing 6")
    print ("the value of the last added item from the stack is "+ str(L.top()))
    if (L.top() != 6):
        sys.exit("Fail - The value is not the same as push")
    stars("slut")

    
#Test the function pop()
def test5():
    stars("Test5")
    L = Stack1Cell()
    L.push(5)
    L.pop()
    if L.isempty() == True:
        print("Test 5(pop) Success!")
        stars("slut")
    else:
        sys.exit("Test 5(pop) Fail!")



#Test of the function pop which it removes the last item added to the stack untill it is empty
def test6():   
    stars("Test6") 
    L = Stack1Cell()
    L.push(34)
    print ("running ... pushing 34")
    L.push(56)
    print ("running ... pushing 56")
    L.push(78)
    print ("running ... pushing 78")
    test = 1
    lista=[34,56,78]
    x = len(lista)-1
    while (test == 1):
        print ("running ... the value of the first item from the stack is "+ str(L.top()))        
        print ("running ... popping")
        if L.top() != lista[x]:
            sys.exit("Test 6 last value of pop failed!")
        x-=1
        L.pop()
        if x == -1:
            print ("Test6 (pop) Success! --> the stack is empty")
            test = 0
            stars("slut")
        else:
            print ("running ... the stack was NOT empty")
            
        
    
    
test1()
test1_5()
test2()
test3()
test4()
test5()
test6()
print ("end of tests!")

