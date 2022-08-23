def magic_square(n):
    magicsquare=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicsquare.append(l)
    i=n//2
    j=n-1
    num=n*n
    c=1
    while(c<=num):
        if(i==-1 and j==n):
            j=n-2
            i=0
        else:
            if(j==n):
                j=0
            if(i<0):
                i=n-1
        if(magicsquare[i][j]!=0):
            j-=2
            i+=1
            continue
        
        else:
            magicsquare[i][j] = c
            c+=1
        i-=1
        j+=1
    for i in range(n):
        for j in range(n):
            print(magicsquare[i][j],end='')
        print()
    print("the sum of the each row /coloumn/diagonal is:"+str(n*(n**2+1)/2))
magic_square(7)