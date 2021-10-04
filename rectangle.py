for _ in range(int(input())):
    a= list(map(int, input().split()))
    f=0
    for i in a:
        if i<=0 or a.count(i)%2!=0:
            print('NO')
            f=1 
            break 
    if f==0:
        print('YES')
