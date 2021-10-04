for i in range(int(input())):
    str1=input()
    str2=input()
    mini=0
    maxi=0
    for i in range(len(str1)):
        if str1[i]=="?" or str2[i]=="?":
            maxi=maxi+1
        elif str1[i]!=str2[i]:
            mini+=1
            maxi+=1
    print(mini,maxi)
