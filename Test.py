def f(lis, n):
    global kis
    lis = lis.copy()
    lis.pop()
    kis = lis

kis = []
lisq = [1, 2, 3]
lisq = f(lisq, 1)
print(kis)