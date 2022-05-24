# modeling of polynomial

class Polynomial:
	def __init__(self, *coeffs):
		self.coeffs = coeffs

	def __repr__(self):
		return 'Polynomial{}'.format(self.coeffs)

	def __add__(self, other):
		return Polynomial(*(x+y for x, y in zip(self.coeffs, other.coeffs)))

	def __sub__(self, other):
		return Polynomial(*(x-y for x, y in zip(self.coeffs, other.coeffs)))

	def __len__(self):
		return len(self.coeffs)

	def deg(self):
		return len(self.coeffs)-1

	def __mul__(self, other):
		pol = [0]*(self.deg()+other.deg()+1)
		
		for x in range(len(self.coeffs)):
			for y in range(len(other.coeffs)):
				pol[x+y] += self.coeffs[x] * other.coeffs[y]

		return Polynomial(*(c for c in pol))


if __name__ == '__main__':
	
	p1 = Polynomial(4, 6, 3)
	p2 = Polynomial(4, 1, 2)
