# 0,1,1,2,3,5,8,13,21,34,55,89
# f(n) = f(n-1) + f(n-2)


# brute force

def fib_brute(n):
    if n == 1:
        return 0
    if n < 4:
        return 1
    f_n = 0
    f1 = 1
    f2 = 1
    i = 4
    while i <= n:
        f_n = f1+f2
        # print(f'{i=}, {f_n=}')
        f1 = f2
        f2 = f_n
        i += 1
    return f_n


# recursion

def fib_recursion(n: int):
    if n == 1:
        return 0
    if n < 4:
        return 1
    return fib_recursion(n-1)+fib_recursion(n-2)


number = 11
print(fib_brute(number), fib_recursion(number))
