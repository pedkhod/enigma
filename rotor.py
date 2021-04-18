#
#
import pickle
import random
alphabet='abcdefghijklmnopqrstuvwxyz'
r2=list(alphabet)
r3=list(alphabet)
r1=list(alphabet)

#print (r1)
random.shuffle(r1)
print (r1)
random.shuffle(r2)
random.shuffle(r3)
print(r1)
print(r2)
print(r3)
f= open('./t_r_s', 'wb')
pickle.dump((r1,r2,r3),f)
f.close()