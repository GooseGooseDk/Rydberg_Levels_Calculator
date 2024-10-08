
from arc import *
import matplotlib.pyplot as plt

def allStates(nStart,nEnd,lAllowed=[]):
    """All atomic quantum states from nStart to nEnd with allowed l

    Args:
        nStart (int): first principle number
        nEnd (int): last principle number
        lAllowed (list): allowed angular number. Default not limited.

    Returns:
        list: List of states
    """
    states = []
    for n in range(nStart,nEnd+1):
        ls = range(0,n-1+1)
        if lAllowed:
            ls=list(set(ls)&set(lAllowed))
              
        for l in ls:
            if l:
                states.append([n,l,l-0.5])
                states.append([n,l,l+0.5])
            else:
                states.append([n,l,0.5])   
    return states

def isHigher(stateStart, stateEnd):
    """ stateStart < stateEnd: True; stateStart > stateEnd: False

    Args:
        stateStart (_type_): _description_
        stateEnd (_type_): _description_
        
    Retures: bool
    """
    n1, l1, j1 = stateStart[0], stateStart[1], stateStart[2]
    n2, l2, j2 = stateEnd[0], stateEnd[1], stateEnd[2]
    if n1 != n2:
        return n1 < n2
    else:
        if l1 != l2:
            return l1 < l2
        else:
            return j1 < j2
        
def higherFilter(stateStart, states):
    statesHigher=[]
    for state in states:
        if isHigher(stateStart, state):
            statesHigher.append(state)
    return statesHigher

def isAllowed(stateStart, stateEnd):
    n1, l1, j1 = stateStart[0], stateStart[1], stateStart[2]
    n2, l2, j2 = stateEnd[0], stateEnd[1], stateEnd[2]
    judge1=(abs(l1-l2)==1)
    judge2=(abs(j1-j2)<=1)
    return judge1 and judge2

def allowedFilter(stateStart, states):
    statesAllowed=[]
    for state in states:
        if isAllowed(stateStart, state):
            statesAllowed.append(state)
    return statesAllowed

def findMatchTrans(stateStart, freqCenter, freqSpan, atom=Caesium()):
    statesMatched, freqs, dipoles=[],[],[]
    state3 = stateStart
    n3, l3, j3 = state3[0], state3[1], state3[2]
    states4 = allowedFilter(stateStart,states=allStates(n3,80))
    for state4 in states4:
        n4, l4, j4 = state4[0], state4[1], state4[2]
        freqTrans=atom.getTransitionFrequency(n3,l3,j3,n4,l4,j4)
        if (freqCenter-freqSpan <= freqTrans <= freqCenter+freqSpan):
            statesMatched.append(state4)
            freqC=atom.getTransitionFrequency(6,1,1.5,n3,l3,j3)
            freqs.append(abs(freqTrans))
            dipole=atom.getDipoleMatrixElement(n3,l3,j3,0.5,n4,l4,j4,0.5,0)
            dipoles.append(abs(dipole))
            print(f'-----{n3} {l3} {j3} {n4} {l4} {j4} %.3fTHz %.3fTHz %.3fea-----' 
                  % (freqTrans*1e-12,freqC*1e-12,dipole))
        else:
            # print(f'{n3} {l3} {j3} {n4} {l4} {j4} {freqTrans*1e-12}THz')
            pass
    return statesMatched, freqs, dipoles

if __name__ == '__main__':
    state1 = [6,0,0.5]
    state2 = [6,1,1.5]
    states3 = allowedFilter(stateStart=state2,states=allStates(7,30))
    freqss,dipoless=[],[]
    freqCenter, freqSpan = 4655*1e9, 20*1e9
    for state3 in states3:
        a,freqs,dipoles=findMatchTrans(state3, freqCenter, freqSpan)
        freqss.extend(freqs)
        dipoless.extend(dipoles)
    plt.stem(freqss,dipoless,markerfmt='',basefmt='')
    plt.show()
        

