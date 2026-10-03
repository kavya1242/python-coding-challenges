#missing number
arr=[1,2,3,5]
b=[]
for i in range(1,len(arr)+2):
    b.append(i)

'''for i in range(len(b)):
    if b[i]!=arr[i]:
        print(b[i])
        break'''

'''
   
for i in range(1,len(b)+1):
    if i not in arr:
        print(i)'''
n=len(b)
a=sum(arr)
c=(n*(n+1))//2
d=c-a
print(d)

   
            
    

