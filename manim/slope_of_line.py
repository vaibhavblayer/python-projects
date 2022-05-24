# slope_of_line.py
# explaining the concept of derivative for a line

from manim import *
from sympy import latex
from sympy.abc import x, y, m, c

y = m*x + c
c = 0
m = 1
x = 5
class SlopeOfLine(Scene):
	def construct(self):
		ax = Axes(
			x_range = [0, 10, 2],
			y_range = [0, 5, 2],
			tips = True,
			axis_config={'include_numbers': True}
		)

		line = ax.plot_line_graph(
			x_values = [0,5], 
			y_values = [0, 4],
		)
		self.add(ax, line)
		self.wait(2)
		
