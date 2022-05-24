# combination.py

import itertools

class MakeComb:
	def __init__(self, *integers, n=2):
		self.integers = integers
		self.n = n

	def make(self):
		l = list(self.integers)
		c = itertools.combinations(l, self.n)
		return list(c)

