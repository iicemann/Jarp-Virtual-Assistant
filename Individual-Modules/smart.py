with open('test.py') as f:
	lines = f.readlines()

with open('test.py') as f:
    for i, l in enumerate(f):
        pass
print(i+1)

with open('test.py', 'w') as f:
	lines.insert(i-1, '\n	elif value == 5:')
	lines.insert(i, '\n		print(\'Five\')\n')
	f.write("".join(lines))
	#f.write('\nprint(a+1)')
	#f.write('\nif a == 1: print(\'a=1\')')
	
