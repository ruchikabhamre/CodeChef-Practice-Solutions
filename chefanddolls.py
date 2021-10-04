for i in range(int(input())):
    n=int(input())
    li=[]
    for j in range(n):
        li.append(int(input()))
    for k in li:
        if li.count(k)%2!=0:
            print(k)
            break
