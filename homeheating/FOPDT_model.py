
class FOPDTModel(HeatModel):
    def __init__(self):
        self.__gain = random(-100,100)
        self.__time_constant = random(0,100)
        self.__dead_time = random(0,10)

    def siso_process(self, y, t, u):
        Kp = self.__gain
        taup = self.__time_constant
        thetap = self.__dead_time

        # calculate derivative
        dydt[0] = (-y[0] + Kp * u)/(taup/n)
        for i in range(1,n):
            dydt[i] = (-y[i] + y[i-1])/(taup/n)
        return dydt

    @dead_time.setter
    def set_dead_time(self, dead_time):
        if(dead_time < 0): 
            raise ValueError("Sorry you can not have non-causal systems where an input affects a change in the past")

        self.__dead_time = dead_time