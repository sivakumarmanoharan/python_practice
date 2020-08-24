arr=[]
rotleftarr=[]
rotrightarr=[]
def rotateLeftArray(arr,k):
    temp=arr[0:k]
    del arr[0:k]
    arr.extend(temp)
    return arr

def rotateRightArray(arr1,k):
    start=len(arr1)-2-k
    end=len(arr1)-2
    temp=arr1[start:end]
    del arr1[start:end]
    for i in range(k):
        arr1.insert(i,temp[i])
    return arr1

n=int(input())
for i in range(n):
    arr.append(int(input()))
k=int(input())
rotleftarr=rotateLeftArray(arr,k)
print(rotleftarr)
rotrightarr=rotateRightArray(arr,k)
print(rotrightarr)
