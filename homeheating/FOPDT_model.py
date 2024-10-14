from random import uniform
from heating_model import HeatingModel


class FOPDTModel(HeatingModel):
    def __init__(self):
        self.__gain = uniform(-100, 100)
        self.__time_constant = uniform(0, 100)
        self.__dead_time = uniform(0, 10)

    def siso_process(self, y, t, u):
        Kp = self.__gain
        taup = self.__time_constant
        thetap = self.__dead_time

        dydt = 0

        # calculate derivative
        dydt = (-y + Kp * u(t - thetap)) / (taup)

        return dydt

    @property
    def dead_time(self):
        return self.__dead_time

    @dead_time.setter
    def set_dead_time(self, dead_time):
        if dead_time < 0:
            raise ValueError(
                "Sorry you can not have non-causal systems where an input affects a change in the past"
            )

        self.__dead_time = dead_time
