n=int(input())
temp=n
palin=0
while n!=0:
    r=n%10
    palin=palin*10+r;
    n=n//10
if temp==palin:
    print('True')
else:
    print("False")