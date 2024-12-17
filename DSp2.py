'''
Experiment Number 2 : Write a python program to store marks scored in subject "Fundamentals of Data Structure" by
                         N students in the class. Write functions to compute following:
                         1. The average score of the class.
                         2. Highest score a==nd lowest score of the class.
                         3. Count of students who were absent for the test.
                         4. Display mark with highest frequency.
'''

# Function for average score of the class

def average(listofmarks):
    sum=0
    count=0
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-1:
            sum+=listofmarks[i]
            count+=1
    avg=sum/count
    print("Total Marks : ", sum)
    print("Average Marks :", avg)

#<----------------------------------------------------------------------------------------------------->

# Function for Highest score in the test for the class

def Maximum(listofmarks):
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-1:
            Max=listofmarks[0]
            break

    for i in range(1,len(listofmarks)):
        if listofmarks[i]>Max:
            Max=listofmarks[i]
    return(Max) 

#<------------------------------------------------------------------------------------------------------>

# Function for Lowest score in the test for the class

def Minimum(listofmarks):
    for i in range(len(listofmarks)):
        if listofmarks[i] != -1:
            Min = listofmarks[0]
            break
    for i in range(1,len(listofmarks)):
        if listofmarks[i]!=-1 and listofmarks[i]<Min:
            Min=listofmarks[i]
    return(Min)

#<------------------------------------------------------------------------------------------------------->

# Function for counting the number of students absent for the test

def absentcount(listofmarks):
    count=0
    for i in range(len(listofmarks)):
        if listofmarks[i]==-1:
              count+=1
    return(count)

#<------------------------------------------------------------------------------------------------------->

# Function for displaying marks with highest frequency
def maxFrequency(listofmarks):
    Max=0
    for j in listofmarks:
        if listofmarks.count(j)>Max and j!=-1:
            Max=listofmarks.count(j)
            mark=j

    return(mark,Max)

#<------------------------------------------------------------------------------------------------------->

# Main function

marksinFDS=[]
numberofstudents=int(input("Enter total number of students : "))
for i in range(numberofstudents):
    print("Enter marks of student ", i+1 ," : ")
    marks=int(input())
    marksinFDS.append(marks)

while True:
    print("\n\n--------------------MENU--------------------\n")
    print("1. Total and Average Marks of the Class")
    print("2. Highest and Lowest Marks in the Class")
    print("3. Number of Students absent for the test")
    print("4. Marks with Highest Frequency")
    print("5. Exit\n")
    ch=int(input("Enter your Choice (from 1 to 5) :"))

    if ch==1:
        average(marksinFDS)

    elif ch==2:
        print("Highest Score in Class : ", Maximum(marksinFDS))
        print("Lowest Score in Class : ", Minimum(marksinFDS))

    elif ch==3:
        print("Number of Students absent in the test : ", absentcount(marksinFDS))

    elif ch==4:
        mark,fr = maxFrequency(marksinFDS)
        print("Highest frequency is of marks",mark," that is",fr)

    elif ch==5:
       print("Thanks for using this program!")
       break

    else:
        print("!!Wrong Choice!! ")
