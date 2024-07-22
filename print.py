a = 1
even=[]
odd=[]
while(a<20):
    if(a%2==1):
        odd.append(a)
    else:
        even.append(a)
    a+=1

print("\nEven:",even,"\n","Odd:",odd)
print("Max of two:",max(even),max(odd))
even.sort(reverse=True)
odd.sort(reverse=True)
print("Reverse list:",even,"\n\t",odd)
print("\n\n")

l1=[x for x in range(100,121)]
print(l1)

