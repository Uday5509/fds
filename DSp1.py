"""
Assignment No. 1 : In a second year computer engineering class, group A students play cricket, group B students play
                   badminton and group C students play football.
                   Write a python program using functions to compute following:
                   a) List of students who play both cricket and badminton.
                   b) List of students who play either cricket or badminton but not both.
                   c) Number of students who play neither cricket nor badminton.
                   d) Number of students who play cricket and football but not badminton.
(NOTE : While realising the group, duplicate entries should be avoided. Do not use SET built-in functions)
"""
# Function for removing duplicate entries from the group
def removeduplicates(d):
    list1=[]
    for i in d:
        if(i not in list1):
            list1.append(i)
    return list1

# Function for finding intersection between two sets (A&B)
def Intersection(list1,list2):
    list3=[]
    for val in list1:
        if val in list2:
            list3.append(val)
    return(list3)

# Function for finding union of two sets (A|B)
def Union(list1,list2):
    list3=list1.copy()
    for val in list2:
        if val not in list3:
            list3.append(val)
    return(list3)

# Function for finding difference between two sets (A-B)
def Difference(list1,list2):
    list3=[]
    for val in list1:
        if val not in list2:
            list3.append(val)
    return(list3)

# Function for finding symmetric difference of two sets (A^B)
def SymmetricDiff(list1,list2):
    list3=[]
    d1=Difference(list1,list2)
    print("Difference between Cricket and Badminton (C-B) is : ", d1)
    d2=Difference(list2,list1)
    print("Difference between Badminton and Cricket (B-C) is : ", d2)
    list3=Union(d1,d2)
    return(list3)

# Functon for finding List of students who play both cricket and badminton
def CB(list1,list2):
    list3=Intersection(list1,list2)
    print("\n\nList of students who play both cricket and badminton is : ", list3)
    return(len(list3))

# Function for finding List of students who play either cricket or badminton but not both

def eCeB(list1,list2):
    list3=SymmetricDiff(list1,list2)
    print("\nList of students who play either cricket or badminton but not both is : ",list3)
    return(len(list3))

# Function for finding Number of students who play neither cricket nor badminton
def nCnB(list1,list2,list3):
    list4=Difference(list1,Union(list2,list3))
    print("\n\nList of students who play neither cricket nor badminton is : ",list4)
    return(len(list4))

# Function for finding Number of students who play cricket and football but not badminton
def CFnB(list1,list2,list3):
    list4=Difference(Intersection(list1,list2),list3)
    print("\n\nList of students who play cricket and football but not badminton is : ",list4)
    return(len(list4))

# Creating an empty list for SE COMP
SEcomp=[]
n=int(input("Enter number of students SEcomp:"))
print("please enter name of" ,n , " students")
for i in range(0,n):
    ele=input()
    SEcomp.append(ele)
print("The original list of SEcomp student:"+str(SEcomp))

# Creating an empty list for Cricket
Cricket=[]
n=int(input("Enter number of student playing Cricket"))
for i in range(0,n):
    name=input("please enter the name of student")
    Cricket.append(name)
print("The original list of student playing cricket:"+str(Cricket))
Cricket=removeduplicates(Cricket)
print("List of student play Cricket"+str(Cricket))

# Creating an empty list for Badminton
Badminton=[]
n=int(input("Enter number of student playing Badminton"))
for i in range(0,n):
    name=input("please enter the name of student")
    Badminton.append(name)
print("The original list of student playing Badminton:"+str(Badminton))
Badminton=removeduplicates(Badminton)
print("List of student play Badminton"+str(Badminton))

# Creating an empty list for Football
Football=[]
n=int(input("Enter the number of student playing Football"))
for i in range(0,n):
    name=input("please enter the name of student")
    Football.append(name)
print("The original list of student playing Football"+str(Football))
Football=removeduplicates(Football)
print("List of student play Football"+str(Football))

while True:
    print("\n\n--------------------MENU--------------------\n")
    print("1. List of students who play both cricket and badminton")
    print("2. List of students who play either cricket or badminton but not both")
    print("3. List of students who play neither cricket nor badminton")
    print("4. Number of students who play cricket and football but not badminton")
    print("5. Exit\n")
    ch=int(input("Enter your Choice (from 1 to 5) :"))

    if ch==1:
        print("Number of students who play both cricket and badminton : ", CB(Cricket,Badminton))

    elif ch==2:
        print("Number of students who play either cricket or badminton but not both : ", eCeB(Cricket, Badminton))

    elif ch==3:
        print("Number of students who play neither cricket nor badminton : ", nCnB(SEcomp,Cricket,Badminton))

    elif ch==4:
        print("Number of students who play cricket and football but not badminton : ", CFnB(Cricket,Football,Badminton))

    elif ch==5:
        print("Thanks for using this program!")
        break
    else:
        print("!!Wrong Choice!! ")

#<---------------------------------------------END OF PROGRAM--------------------------------------->
