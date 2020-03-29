#arr = list(map(int, input().split))
arr = [3,5,5]
k = int(input("enter the number of stones that can be picked once: "))
#[3,5,5]
count=0
for i in range(len(arr)):
    div = arr[i]//k
    count+=div
    if (arr[i]%k)!=0:
        count+=1
print(count)

s=arr[-1]%k
if count%2==0:
    print("Alex wins the game!")
else:
    print("Sam wins the game")

    








        
    
    
     
        
        
