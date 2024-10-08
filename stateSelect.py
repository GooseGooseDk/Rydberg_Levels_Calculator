from matplotlib import cm
import State, States
import matplotlib.pyplot as plt

state1 = State.State(6,0,0.5)
state2 = State.State(6,1,1.5)

min510, max510 = 2*2.99792e8/1029e-9, 2*2.99792e8/1007.0e-9
states3 = States.States.allStates(20,70)
states3 = states3.allowedTo(state2)
states3, a = states3.matchTrans(state2,freqStart=min510,freqEnd=max510)

freqss,dipoless=[],[]
freqStart, freqEnd = 0.1e12, 10e12

f=open('log.txt','w')
for state3 in states3.states:
    states4 = States.States.allStates(7,state3.n)
    states4 = states4.allowedTo(state3)
    statesMatched, freqs = states4.matchTrans(state3,freqStart,freqEnd)
    dipoles = statesMatched.getDipoleMatrixElement(state3)
    freqs = [abs(freq) for freq in freqs]
    dipoles = [abs(dipole) for dipole in dipoles]

    freqC=state2.getTransitionFrequency(state3)
    for i in range(0,len(statesMatched.states)):
        state4, freq, dipole = statesMatched.states[i], freqs[i], dipoles[i]
        print(f'-----{state3} {state4} %.3fTHz %.3fTHz %.3fea-----' 
                  % (freq*1e-12,freqC*1e-12,dipole))
        f.write(f'-----{state3} {state4} %.3fTHz %.3fTHz %.3fea-----\n' 
                  % (freq*1e-12,freqC*1e-12,dipole))

    color=cm.jet(state3.n/100)
    plt.stem(freqs,dipoles,markerfmt='',basefmt='',linefmt=color)
    freqss.extend(freqs)
    dipoless.extend(dipoles)

f.close()
plt.xscale('log')
plt.xlim([1e11,1e13])

# plt.stem(freqss,dipoless,markerfmt='',basefmt='')
plt.show()
