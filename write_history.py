import readline
import time


t = time.ctime()

readline.add_history(t)
readline.write_history_file('./python-history/{0}'.format(t))
readline.add_history(t)



#lines = []
#with open(t, 'r') as f:
#	lines = f.readlines()
#
#
#with open(t, 'w') as f:
#	for number, line in enumerate(lines):
#		if number not in [1, 927]:
#			f.write(line)


