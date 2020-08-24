from array import *             #importing of array
arr1=array('i',[1,2,3,1,2,5])   #creation of array
arr2=array('i',[5,7,6])
li1=[9,8,7]
arr1.append(4)                   #appending of new element
arr1.insert(2,5)                 #inserting 5 into the desired position
arr1.pop(5)                      #deleting the element in the position specified
arr1.remove(2)                   #removing the element's first occurence
index=arr1.index(5)              #returns the first occuring index of the element
arr1.reverse()                   #Reverses the array
arr1.extend(arr2)                #extending of another array
arr1.fromlist(li1)               #importing elements from a tolist
for i in range(len(arr1)):       #printing of array
    print(arr1[i],end=" ")
print("\r")
print(arr1.typecode)             #returns the type of the array
print(arr1.itemsize)             #returns the size of the array
print(arr1.buffer_info())        #returns a tuple which contains the address and no of elements
print(arr1.count(5))             #returns the occurence of a particular element
print(arr1.tolist())             #returns the array as a list
