n,t=map(int,input().split())
for i in range(1,t+1):
    if i%2!=0:
        print(n,'x',i,'=',n*i)