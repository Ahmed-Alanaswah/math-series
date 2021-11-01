def fibonacci(n):
   if n == 0:
       return 0
       
   if n == 1:
       return 1
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

n=5

for i in range(n+1):
	print(fibonacci(i))
    
    
def lucas(m):
   if m == 0:
       return 2
       
   if m == 1:
       return 1
   else:
       return(lucas(m-1) + lucas(m-2))
       

m= 5

    
print("==============")
    
for i in range(m+1):
	print(lucas(i))    


def sum_series(n,n1=0,n2=1):
   if n == 0:
       return n1
       
   if n == 1:
   		return n2
   else:
       return(sum_series(n-1,n1,n2) + sum_series(n-2,n1,n2))
       

n=5

for i in range(n+1):
	print(sum_series(i,0,1))
