def swap(a,i,j):
    temp=a[i]
    a[i]=a[j]
    a[j]=temp
def rearrangeArray(a):
    for i in range(1,len(a),2):
        if a[i-1]>a[i]:
            swap(a,i-1,i)
a=[9,6,8,3,2,5]
rearrangeArray(a)
print(a)            
            