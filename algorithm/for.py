def for_loop(n:int)->int:
    res=0
    for i in range(1,n+1):
        res+=i
    return res

def while_loop(n:int)->int:
    res=0
    while n>0:
        res+=n
        n-=1
    return res

def while_loop_1(n:int)->int:
    res=0
    i=0
    while i<n:
        res+=i
        i*=2
    return res

def nested_for_loop(n:int)->str:
    res=""
    for i in range(1,n+1):
        for j in range(1,n+1):
            res+=f"({i},{j}) , "
        res+="\n"
    return res


def recursion(n:int)->int:
    if n==1:
        return 1
    res= recursion(n-1)
    return n+res

def recur(n:int)->int:
    if n==1:
        return 2
    res=2*n
    return res+recur(n-1)

def tail_recur(n:int,res:int=0)->int:
    if n==0:
        return res
    return tail_recur(n-1,res+n)


def fib(n:int)->int:
    if n==1 or n==2:
        return n-1
    return fib(n-1)+fib(n-2)

def fib1(n:int,a:int =0,b:int =1)->int:
    if n==3:
        return a+b
    return fib1(n-1,b,a+b)

def fib2(n: int, a: int = 0, b: int = 1) -> int:
    if n == 1:
        return a
    if n == 2:
        return b
    return fib2(n - 1, b, a + b)


if __name__ == "__main__":
    # print(nested_for_loop(10))

    n=int(input("请输入一个整数："))
    # print(recursion(n))
    # print(recur(n))
    # print(tail_recur(n))
    print(fib(n))
    print(fib1(n))
    print(fib2(n))

    