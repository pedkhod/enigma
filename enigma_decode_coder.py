import pickle
f = open('./t_r_s.enigma','rb')
r1,r2,r3=pickle.load(f)
f.close()
print(r1,r2,r3)
alphabet='abcdefghijklmnopqrstuvwxyz'
def reflactor(oc)
     return alphabet[len(alphabet )-alphabet.find(oc)-1]
def enigma_coder(oc)
    oc1=r1[alphabet.find(oc)]
    oc2=r2[alphabet.find(oc1)]
    oc3=r3[alphabet.find(oc2)]
    reflacted= reflactor(oc3)
    oc3= alphabehet[r3.find(reflacted)]
    oc2=alphabet[r2.find(oc3)]
    oc1=alphabet[r1.find(oc2)]