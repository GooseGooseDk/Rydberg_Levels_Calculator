from arc import *

class State(object):
    def __init__(self,n,l,j):
        """
        Atom state with principle/angular/inner quantum number

        Args:
            n (double): principal quantum number
            l (double): angular quantum number
            j (double): inner quantum number
        """        
        self.n, self.l, self.j = n, l, j

    @classmethod
    def initsec(self,numbers):
        """
         Atom state with principle/angular/inner quantum number

        Args:
            numbers (List): [n,l,j]
        """
        return self(numbers[0], numbers[1], numbers[2])
    
    def __str__(self):
        return f"n:{self.n}, l:{self.l}, j:{self.j}"
    
    def __lt__(self,state2):
        """
        Whether n2, l2, j2 > n1, l1, j1

        Args:
            state2 (State): _description_

        Returns:
            bool: _description_
        """        
        n1, l1, j1 = self.n, self.l, self.j
        n2, l2, j2 = state2.n, state2.l, state2.j
        if n1 != n2:
            return n1 < n2
        else:
            if l1 != l2:
                return l1 < l2
            else:
                return j1 < j2

    def get(self):
        """
        Returns:
            List: [n,l,j]
        """        
        numbers = [self.n, self.l, self.j]
        return numbers
    
    def set(self,numbers):
        """
        Args:
            numbers (List): [n,l,j]
        """        
        n, l, j = numbers[0], numbers[1], numbers[2]
        self.n, self.l, self.j = n, l, j
            
    def isAllowedto(self, state2):
        n1, l1, j1 = self.n, self.l, self.j
        n2, l2, j2 = state2.n, state2.l, state2.j
        judge1=(abs(l1-l2)==1)
        judge2=(abs(j1-j2)<=1)
        return judge1 and judge2
            
    def getTransitionFrequency(self,state2,atom=Caesium()):
        """_summary_

        Args:
            state2 (State): target state
            atom (_type_, optional): _description_. Defaults to Caesium().

        Returns:
            float: Transition freqency
        """        
        n1, l1, j1 = self.n, self.l, self.j
        n2, l2, j2 = state2.n, state2.l, state2.j
        freqTrans=atom.getTransitionFrequency(n1,l1,j1,n2,l2,j2)
        return freqTrans
    
    # @staticmethod
    # def getTransitionFrequency(state1,state2,atom=Caesium()):
    #     """_summary_

    #     Args:
    #         state2 (State): target state
    #         atom (_type_, optional): _description_. Defaults to Caesium().

    #     Returns:
    #         float: Transition freqency
    #     """        
    #     n1, l1, j1 = state1.n, state1.l, state1.j
    #     n2, l2, j2 = state2.n, state2.l, state2.j
    #     freqTrans=atom.getTransitionFrequency(n1,l1,j1,n2,l2,j2)
    #     return freqTrans
    
    def getDipoleMatrixElement(self,state2,mj1=0.5,mj2=0.5,q=0,atom=Caesium()):
        """_summary_

        Args:
            state2 (State): target state
            mj1: projection of total angular momentum for state 1
            mj2: projection of total angular momentum for state 2
            q (int): specifies transition that the driving field couples to,
                    +1, 0 or -1 corresponding to driving :math:`\sigma^+`,
                    :math:`\pi` and :math:`\sigma^-` transitions respectively.
            atom (_type_, optional): _description_. Defaults to Caesium().

        Returns:
            float: Dipole matrix element
        """        
        n1, l1, j1 = self.n, self.l, self.j
        n2, l2, j2 = state2.n, state2.l, state2.j
        dipole=atom.getDipoleMatrixElement(n1,l1,j1,mj1,n2,l2,j2,mj2,q)
        return dipole
    
    @staticmethod
    def getDipoleMatrixElement(state1,state2,mj1=0.5,mj2=0.5,q=0,atom=Caesium()):
        """_summary_

        Args:
            state2 (State): target state
            mj1: projection of total angular momentum for state 1
            mj2: projection of total angular momentum for state 2
            q (int): specifies transition that the driving field couples to,
                    +1, 0 or -1 corresponding to driving :math:`\sigma^+`,
                    :math:`\pi` and :math:`\sigma^-` transitions respectively.
            atom (_type_, optional): _description_. Defaults to Caesium().

        Returns:
            float: Dipole matrix element
        """        
        n1, l1, j1 = state1.n, state1.l, state1.j
        n2, l2, j2 = state2.n, state2.l, state2.j
        dipole=atom.getDipoleMatrixElement(n1,l1,j1,mj1,n2,l2,j2,mj2,q)
        return dipole
      
if __name__ == "__main__":
    state1=State(6,0,0.5)
    state2=State.initsec([6,1,1.5])

    print(state1.l)
    print(state2.j)