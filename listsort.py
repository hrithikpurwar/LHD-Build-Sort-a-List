#Reading The List
list1=[]
count=int(input("Enter the total number of list elements: "))
for i in range(count):
    val=int(input("Enter element %d : " %(i+1)))
    list1.append(val)

#Sorting The List
i = 0
for i in range(count):
    for j in range(count):
        if(list1[i] < list1[j]):
            list1[i],list1[j]=list1[j],list1[i]

#Displaying the List
print("Sorted list in Ascending Order is : ", list1)