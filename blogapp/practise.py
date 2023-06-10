# def pypart(n):
#     for i in range(0,n):
#         for j in range(0,i+1):
#             print("*",end=" ")
#         print("\r")
# pypart(5)

# def pypart(n):
#     k=n-1
#     for i in range(0,n):
#         for j in range(0,k):
#             print(end=" ")
#         k=k-1
#         for j in range(0,i+1):
#             print("*",end=" ")
#         print("\r")    
# pypart(5)




# def pypart(n):
#     k=2*(n-1)
#     for i in range(0,n):
#         for j in range(0,k):
#             print(end=" ")
#         k=k-2
#         for j in range(0,i+1):
#             print("*",end=" ")
#         print("\r")    
# pypart(5)


# def palindrome(n):
#     temp=n
#     rev=0
#     while(temp>0):
#         digit=temp%10
#         rev=rev*10+digit
#         temp=temp//10
#     if n==rev:
#         print(f" yes {n} is a palindrome ")
#     else:
#         print(f" no  {n} is a palindrome ")
    
# palindrome(121)

def palinddrome(s):
    temp=s[::-1]
    if s==temp:
        print(f" yes {s} is a palindrome ")
    else:
        print(f" no  {s} is a palindrome ")
s='NITIN'    
palinddrome(s)

def palindrome(s):
    n=len(s)
    for i in range(n):
        if s[i]!=s[n-i-1]:
            print(f" yes {s} is a palindrome ")
        else:
            print(f" no  {s} is a palindrome ")
s='NITIN'    
palinddrome(s)
    

