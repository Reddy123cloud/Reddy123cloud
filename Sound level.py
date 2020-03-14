def survey():
    L=[]
    avg=0
    count=0
    while True:
        a=int(input("Enter the sound level"))
        L.append(a)
        avg+=a
        count+=1
        if a==0:
           print("average sound level",int(avg/count))
           print("highest recorded sound level",max(L))
           break
survey()
