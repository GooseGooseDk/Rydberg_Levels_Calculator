import State
from arc import *

class States(object):
    """
    List of States
    """    
    def __init__(self):
        self.states = [State.State(1,2,3)]

    @classmethod
    def initsec(self,states):
        """_summary_

        Args:
            states (List): List of State
        """        
        obj_states=self()
        obj_states.states = states
        return obj_states
    
    @classmethod
    def allStates(self,nStart,nEnd,lAllowed=[]):
        """All atomic quantum states from nStart to nEnd with allowed l

        Args:
            nStart (int): first principle number
            nEnd (int): last principle number
            lAllowed (list): allowed angular number. Default not limited.

        Returns:
            States: List of State
        """
        states = []
        for n in range(nStart,nEnd+1):
            ls = range(0,n-1+1)
            if lAllowed:
                ls=list(set(ls)&set(lAllowed))
                
            for l in ls:
                if l:
                    states.append(State.State(n,l,l-0.5))
                    states.append(State.State(n,l,l+0.5))
                else:
                    states.append(State.State(n,l,0.5))
        return self.initsec(states)
    
    def myprint(self):
        states=self.states
        for state in states:
            print(state)
    
    def higherThan(self,state2):
        """A filter

        Args:
            state2 (State): _description_

        Returns:
            States: List of states > state2
        """        
        statesHigher = []
        for state in self.states:
            if state > state2:
                statesHigher.append(state)
        return self.initsec(statesHigher)
    
    def allowedTo(self,state2):
        """A filter

        Args:
            state2 (State): target state

        Returns:
            States: List of states allowed transiting to state2 by select rule.
        """   
        statesAllowed=[]
        for state in self.states:
            if state.isAllowedto(state2):
                statesAllowed.append(state)
        return self.initsec(statesAllowed)

    def matchTrans(self,state2,freqStart,freqEnd,atom=Caesium(),isPrint=False):
        """A filter to find matched transitions whose transition frequency ∈ [freqStart, freqEnd]

        Args:
            state2 (State): target state
            freqStart (double): _description_
            freqEnd (double): _description_
            atom (_type_, optional): _description_. Defaults to Caesium().

        Returns: Matched states
            States: _description_
            List: List of transition frequencies
        """        
        obj_states=self.allowedTo(state2)
        n2, l2, j2 = state2.n, state2.l, state2.j
        states=obj_states.states
        statesMatched=[]
        freqTranss=[]
        for state1 in states:
            n1, l1, j1 = state1.n, state1.l, state1.j
            freqTrans=atom.getTransitionFrequency(n1,l1,j1,n2,l2,j2)
            freqTrans=abs(freqTrans)
            if (freqStart <= freqTrans <= freqEnd):
                statesMatched.append(state1)
                freqTranss.append(freqTrans)
                if isPrint:
                    print(state1)
        return self.initsec(statesMatched), freqTranss 
    
    def getTransitionFrequency(self,state2,atom=Caesium()):
        """_summary_

        Args:
            state2 (State): target state
            atom (_type_, optional): _description_. Defaults to Caesium().

        Returns:
            List: List of transition freqencies
        """        
        freqTranss=[]
        n2, l2, j2 = state2.n, state2.l, state2.j
        states1=self.states
        for state1 in states1:
            n1, l1, j1 = state1.n, state1.l, state1.j
            freqTrans=atom.getTransitionFrequency(n1,l1,j1,n2,l2,j2)
            freqTranss.append(freqTrans)
        return freqTranss
    
    def getDipoleMatrixElement(self,state2,mj1=0.5,mj2=0.5,q=0,atom=Caesium()):
        """
        _summary_

        Args:
            state2 (State): target state
            mj1: projection of total angular momentum for state 1
            mj2: projection of total angular momentum for state 2
            q (int): specifies transition that the driving field couples to,
                    +1, 0 or -1 corresponding to driving :math:`\sigma^+`,
                    :math:`\pi` and :math:`\sigma^-` transitions respectively.
            atom (_type_, optional): _description_. Defaults to Caesium().

        Returns:
            List: List of dipole matrix elements
        """        
        dipoles=[]
        n2, l2, j2 = state2.n, state2.l, state2.j
        states1=self.states
        for state1 in states1:
            n1, l1, j1 = state1.n, state1.l, state1.j
            dipole=atom.getDipoleMatrixElement(n1,l1,j1,mj1,n2,l2,j2,mj2,q)
            dipoles.append(dipole)
        return dipoles
        
    
if __name__ == "__main__":
    state2=State.State(6,1,1.5)
    states3=States()
    print(type(states3))
    states3.myprint()
    states4=States.initsec([state2])
    print(type(states4))
    states4.myprint()
    states5=States.allStates(1,3)
    print(type(states5))
    states5.myprint()
    print(1)