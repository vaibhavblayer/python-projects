
fib_cache = {}

def fib(n):
	if n in fib_cache:
		return fib_cache[n]

	if n == 1:
		value = 1
	elif n == 2:
		value = 1
	elif n > 2:
		value = fib(n-1) + fib(n-2)

	fib_cache[n] = value
	return value



import functools

@functools.lru_cache(maxsize=100)
def fact(n):
	if n == 0:
		return 1
	elif n > 0:
		return n*fact(n-1)


@functools.lru_cache(maxsize=1000)
def fb(n):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	elif n > 2:
		return fb(n-1) + fb(n-2)







