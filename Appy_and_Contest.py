t=int(input())
for i in range(t):
    n,a,b,k=map(int,input().split())
    if a%b==0:
        count=n/b-n/a
    elif b%a==0:
        count = n/a-n/b
    else:
        count = n/a+n/b-2*(n/(a*b))
    if count>=k:
        print("Win")
    else:
        print("Lose")
