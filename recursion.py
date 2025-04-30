def fib(n):
    if n==1:
        return 1
    if n==2:
        return 1
    elif n>2:
        return fib(n-1) + fib(n-2)

#for number in range(1,5):
    #print(f"{number}: {fib(number)}")

f_cache = {}

def fib2(number):


    if number in f_cache:
        return f_cache[number]


    if number==1:
        value=1

    elif number==2:
        value=1
    elif number > 2:
        value = fib2(number-1) + fib2(number-2)

    f_cache[number]=value
    return value

#for number in range(1,1000):
 #   print(number,":", fib2(number))
  #  print(f"{number} : {fib2(number)}")


from functools import lru_cache
# least recently used cache

@lru_cache(maxsize = 100)
def fib3(k):

    if k==1:
        return 1
    elif k==2:
        return 1
    elif k > 2:
        return fib3(k-1)+ fib3(k-2)

for i in range(1000):
    print(f"{i} : {fib3(i)}")



