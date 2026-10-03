n=int(input())
arr=list((map(int,input().split())))

position=0
for i in arr:
    if i!=0:
        arr[position]=i
        position+=1
for i in range(position,n):
    arr[i]=0
print(arr)