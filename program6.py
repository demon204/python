def sort(a):
    zeros=a.count(0)
    k=0
    while zeros:
        a[k]=0
        zeros=zeros-1
        k=k+1
    for k in range(k,len(a)):
        a[k]=1
a=[0,0,1,0,1,0,1,8,5,2]
sort(a)
print(a)        
      