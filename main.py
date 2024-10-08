from arc import *
from freq2state import *
import matplotlib.pyplot as plt
import math

atom=Caesium()
freqL, freqH=2*292.766e12, 2*298.824e12
freqCenter=(freqH+freqL)/2
freqSpan=freqH-freqL

state2=[6,1,1.5]
# states3 = findMatchTrans(state2,freqCenter=freqCenter,freqSpan=freqSpan)
# print(states3)

states3=allStates(21,50,lAllowed=[2])
states3=[[40,2,2.5]]
states40=allStates(20,80)
freqs=[]
dipoles=[]
for state3 in states3:
    n3, l3, j3 = state3[0], state3[1], state3[2]
    # states4=higherFilter(state3,states40)
    states4=allowedFilter(state3,states40)
    for state4 in states4:
        n4, l4, j4 = state4[0], state4[1], state4[2]
        freq=atom.getTransitionFrequency(n3,l3,j3,n4,l4,j4)
        dipole=atom.getDipoleMatrixElement(n3,l3,j3,0.5,n4,l4,j4,0.5,0)
        dipole2=atom.getDipoleMatrixElement(n3,l3,j3,-0.5,n4,l4,j4,0.5,1)
        dipole3=atom.getDipoleMatrixElement(n3,l3,j3,0.5,n4,l4,j4,-0.5,-1)
        print('state3: %d %d %.1f state4: %d %d %.1f  %.3fTHz %.3fea' % (n3,l3,j3,n4,l4,j4,freq*1e-12,dipole))
        freqs.append(abs(freq))
        dipoles.append(abs(dipole))
        freqs.append(abs(freq))
        dipoles.append(abs(dipole2))
        freqs.append(abs(freq))
        dipoles.append(abs(dipole3))
    

plt.stem(freqs,dipoles,markerfmt='',basefmt='')
plt.show()



