def f_prime(n):
    if n>1:
        for i in range(2,n):
            if(n%i==0):
                return False
                break
        else:
            return True
    else:
         return False

def perfect(n):
    sumf=0
    for i in range(1,n):
        if (n%i==0):
            sumf=sumf+i
    if(sumf==n):
        return True
    else:
        return False
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def factor(n):
    for i in range(1,n+1):
        if (n%i==0):
            
            
def fun_tab(a,b,c):
    for i in range(b,c+1):
        print( a, "  X ", i," = ", a*i)

