arr=list(map(int,input("Enter the array elements: ").split()))
l=[]
for i in range(len(arr)):
    count=0
    for j in range(1,int(arr[i]/2)+1):
        if arr[i]%j==0:
            count+=1
    l.append(count)
factor=[]
for k in range(len(l)):
    index_= l.index(min(l))
    factor.append(arr[index_])
    l.remove(l[index_])
    arr.remove(arr[index_])
print(factor)
