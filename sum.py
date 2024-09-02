# . Find Two Numbers with Sum N

seen=set()
a=list(map(int,input().split()))
s=int(input())
for i in range(len(a)):
    f=s-a[i]
    if f in seen:
        print(a[i],f)
        break
    seen.add(a[i])
