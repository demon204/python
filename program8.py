def reorder(a):
    k=0
    for i in a:
        if i:
            a[k]=i
            k=k+1
    for i in range(k,len(a)):
        a[i]=0
a=[6,0,8,2,3,0,4,0,1]
reorder(a)
print(a)                