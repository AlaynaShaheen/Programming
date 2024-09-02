# The function accepts two strings ‘str1’ and ‘str2’ as its argument. The function needs to return
# the index of the first occurrence of substring ‘str2’ in string ‘str1’ or -1 if the substring is not
# found.

s=input()
s1=input()
n=len(s)
m=len(s1)
f=0
for i in range(n-m+1):
    if s[i:i+m]==s1:
        print(i)
        f=1
        break
if f==0:
    print(-1)
