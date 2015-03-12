"""
TP CH 14 practice
used to do this toolbox
"""

"""
fout = open('output.txt','w')
print fout

line1 = "This here's the wattle,\n"
fout.write(line1)

line2 = "the emblem of our land./n"
fout.write(line2)

fout.close()
"""

"""
import anydbm
db = anydbm.open('captions.db','c')
db['cleese.png'] = 'Photo of John Cleese.'

for key in db:
	print key
"""

import pickle
t = [1,2,3]
pickle.dumps(t)

t1 = [1,2,3]
s = pickle.dumps(t1)
t2 = pickle.loads(s)
print t2