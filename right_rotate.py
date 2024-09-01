# right rotatiion

n,k=map(int,input().split())
a=list(map(int,input().split()))
k=k%n
for i in range(k):
    t=a[0]
    for j in range(n-1):
        a[j]=a[j+1]
    a[n-1]=t
print(a)
