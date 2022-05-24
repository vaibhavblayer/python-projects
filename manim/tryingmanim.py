from manim import *


config.background_color = RED

import sympy
from sympy.abc import a,b,c, x, y, z
from sympy import latex


f = sympy.tan(x)
intf = latex(sympy.integrate(f, x))


class Brace(Scene):
	def construct(self):
		dot = Dot([-2, -1, 0])
		dot2 = Dot([2, 1, 0])
		line = Line(dot.get_center(), dot2.get_center())
		fn = MathTex(intf)
		self.add(line, dot, dot2, fn)
