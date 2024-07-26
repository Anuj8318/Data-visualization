import numpy as np 
arr = np.arange(1,15)
print(arr)
print(arr%2==0)
print(arr%2!=0)
print(arr[arr>8])
arr[arr%2==0]=0
print(arr)

arr1= np.arange(1,8)
print(arr1+2)
print(arr1*2)
print(arr1**2)


arr2= np.array([10,20,30,25,6,2])
print(np.min(arr2))
print(np.max(arr2))
print(np.argmin(arr2))
print(np.argmax(arr2))
print(np.sqrt(arr2))

def fibo(arr):
    dimensions = arr.shape
    rows, col = dimensions
    ans =[]
    sum =0
    for i in  range(rows):
        for j in range(col):
            sum+=arr[i,j]
            ans.append(sum)
    return ans

np.random.seed(122)           
mat = np.random.randint(1,21,9).reshape(3,3)
print(mat)
dimensions = mat.shape
rows, col = dimensions

arr4 = fibo(mat)
print(arr4)


print(np.max(mat,axis=1))
print(np.cumsum(mat,axis=1))


print("----------------------------------------------------")
np.random.seed(123)
mat2= np.random.randint(1,21,10)
print(mat2)
np.random.shuffle(mat2)
print(mat2)
print(np.unique(mat2,return_index=True, return_counts=True))
print(np.unique(mat).size)


print("-----------------------------")
a1=np.array([10,20,30,40])
a2=np.array([50,60,70,80])
print(a1)
print(a2)
print(np.vstack((a1,a2)))
print(np.hstack((a1,a2)))


a3=np.array([10,25,65,85,25,63,95,65])
w=np.where(a3==65)
print(w)

print("----------------------------")
a4= np.array([10,25,36,78,89,94])
ss= np.searchsorted(a4,90)
print(ss)






