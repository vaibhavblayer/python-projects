# calculation of torque
import math

def torque(f, r, a):
	return f*r*math.sin(math.radians(a))
