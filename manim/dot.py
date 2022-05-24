# slope_of_line.py
# explaining the concept of derivative for a line

from manim import *
import sympy
from sympy import Integral
from sympy import latex
from sympy.abc import x, y, m, c

f = sympy.sin(x)

y = Integral(f, (x, -3, 5))

g = y.doit()
h = g.n(3)


class DifferentDots(Scene):
	def construct(self):
		tex=TexFontTemplates.times_fourier_it
		
		table = Table([['Hello this is text'], ['This is last sentence']])

		m0 = Dot()
		m1 = AnnotationDot()
		m2 = MathTex(latex(y), tex_template=tex).set_color(RED)
		m3 = MathTex('{0} = {1}'.format(latex(g),  latex(h)), tex_template=tex).set_color(RED)
		self.add(m0, m1, m2, m3)
		
		m0.shift(UP*3)
		m1.shift(UP*2)
		
		m3.shift(DOWN*2)

		#for i, obj in enumerate(self.mobjects):
		#	obj.shift(DOWN*(i-1))

