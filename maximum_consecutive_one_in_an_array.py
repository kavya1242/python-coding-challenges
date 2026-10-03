n=int(input())
arr=list(map(int,input().split()))
count=0
maxone=[]
for i in arr:

    if i==1:
        count+=1
    else:
        count=0
    maxone.append(count)
print(max(maxone))
    
