x=int(input("enter the number:"))
temp=n
res=0
while(n>0):
    dig=x%10
    res=res*10+dig
    x=x//10
if(temp==res):
    print("this is palindrome")
else:
    print("this is not palindrome")
