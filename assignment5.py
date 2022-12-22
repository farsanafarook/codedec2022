#Write a function that take 2 sentance
#split the words by space and create 2 lists of words. then it should generate
# a new list with elements are commen to both lists
#the new lits should not have ANy duplicates and input list may be off different length
a=input("enter first sentence")
b=input("enter second sentence")
list1=a.split(" ")
print(list1)
list2=b.split(" ")
print(list2)
new_list=[]
for i in list1:
    for x in list2:
        if i==x:
            new_list.append(i)
print("new_list",new_list)
new_list1 = []
for k in list1:
    if k not in new_list:
        new_list1.append(k)
for r in list2:
    if r not in new_list:
            new_list1.append(r)
print("list with out duplicate",new_list1 )


#create a class called calculator
#while creating object pass two numbers into it
#then call object.add() multiply() devide(*)
class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
obj=calculator(a,b)
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Result: ",obj.add())
    elif choice==2:
        print("Result: ",obj.sub())
    elif choice==3:
        print("Result: ",obj.mul())
    elif choice==4:
        print("Result: ",round(obj.div(),2))
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
print()




