def survey():
    avg=0
    L=[]
    a=int(input("Enter the sound level"))
    L.append(a)
    avg+=a
    while a!=0: 
        for j in L:
           if L[j]==0:
             print("average sound level",int(avg/n))
             print("highest recorded sound level",max(L))
survey()

