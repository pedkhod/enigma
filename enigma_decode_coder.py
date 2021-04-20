import pickle
f = open('./t_r_s.enigma','rb')
r1,r2,r3=pickle.load(f)
f.close()
print(r1,r2,r3)
alphabet='abcdefghijklmnopqrstuvwxyz'
def reflactor(oc):
     return alphabet[len(alphabet )-alphabet.find(oc)-1]

def enigma_coder(oc):
    oc1=r1[alphabet.find(oc)]
    oc2=r2[alphabet.find(oc1)]
    oc3=r3[alphabet.find(oc2)]
    reflacted= reflactor(oc3)
    oc3= alphabet[r3.find(reflacted)]
    oc2=alphabet[r2.find(oc3)]
    oc1=alphabet[r1.find(oc2)]
    return oc1
def rotoing():
    global r1 , r2 , r3,state
    r1=r1[1:]+r1[0]
    if state % 26:
        r2=r2[1:]+r2[0]
    if state%(26*26):
        r3=r3[1:]+r3[0]
plain = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
cipher=''
state =0
for oc in plain:
    state+=1
    cipher += enigma_coder(oc)
    rotoing()
print (cipher)