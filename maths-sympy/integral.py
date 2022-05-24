import sympy
import os
from sympy import latex, Integral, Rational
from sympy.abc import a, b, c, n, x, y
from sympy import tan, sin, cos, log, exp


integrals = dict(
item1 = Integral(x**n, x),
item2 = Integral(exp(x), x),
item3 = Integral(sin(x), x),
item4 = Integral(cos(x), x),
item5 = Integral(tan(x), x),
item6 = Integral(sin(a*x), x),
item7 = Integral(log(x), x),
item8 = Integral(1/(x**2 + a**2), x)
)



tex = 'integral.tex'

with open(tex, 'w') as f:
	f.write('\\begin{enumerate}\n')
	for i in integrals.values():
		item = '\\item ${0}$\\\\ \n ${1}$\n'.format(latex(i), latex(i.doit()))
		f.write(item)

	f.write('\\end{enumerate}\n')
