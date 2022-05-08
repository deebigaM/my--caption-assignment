
  
li1=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li1.append(e)
  

print("Positive numbers in",li1,"are: ")
  

for i in li1:   
    
    if i >= 0:
       print(i, end = " ")
       
li2=[]
n=int(input("Enter size of list "))
for j in range(0,n):
     e=int(input("Enter element of list "))
     li2.append(e)
     
print("Positive numbers in",li2,"are: ")
     
for j in li2:   
     
     if j >= 0:
        print(  j, end = " ")
  
  
