N,A,B=list(map(int,input().split()))
print(N,A,B)

sum_list=[]
for i in range(1,N+1):
    print(i,A,B)
    if(i%A!=0):
        None
    else:
        continue
    print("Aæã")
    
    if(i%B!=0):
        None
    else:
        continue
    print("Bæã")
    sum_list.append(i)
    
print(sum_list)
print(sum(sum_list))
