#Given a list L and an integer n,rotate
# L to the right by n places
#if n is negative rotate L to the left by n places
#example
#L=[1,2,3,4,5,6,7,8,9,10]
#if n is3 then L=[8,9,10,1,2,3,4,5,6,7]
#if n is -3 then L=[4,5,6,7,8,9,10,1,2,3]

def rotate(L,n):
    if n==0:
        return
    if n>0:
        for i in range(n): #n is 3
            x=L.pop()
            L.insert(0,x)#L=[4,5,6,7,8,9,10,1,2,3,]
    else:
        for i in range(-n):
            x=L.pop(0)
            L.append(x)
    return

L=[1,2,3,4,5,6,7,8,9,10]
n=int(input("enter an integer n to rotate"))
rotate(L,n)
print(L)
'''
#POP fu nction
l=[1,2,3,4]
x=l.pop()#pop() last index position thng will removed
print(l)
print(x)

#slicing
list=[1,2,3,4,5,5,6,7,8]
n=int(input('enter a number'))
list_1=(list[-n:]+list[:-n])
print(list_1)
'''
#assignment---2 using function
#fibonacci sequence is 1,1,2,3,5,8,13,12
#given a n,write a function to return n numbers
#of fibonacci sequence
def fabonacci(number):
    L=[0]
    a,b=0,1
    for k in range(number):
        a,b=b,a+b
        L.append(a)
    return L
number=int(input('Enter a number'))
print(fabonacci(number))



#assighnment 3----using function write a function to check whther it is palindrom
def checkPalindrom(x):

    if x==x[::-1]:
        print("palindrom")
    else:
        print("notpalindrom")

x=input('Enter a string')
print(checkPalindrom(x))



