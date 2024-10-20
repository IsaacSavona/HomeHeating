from random import uniform
from gekko import GEKKO
from .heating_model import HeatingModel, register_model


@register_model("FOPDT")
class FOPDTModel(HeatingModel):
    def __init__(self):
        self.__gain = uniform(-100, 100)
        self.__time_constant = uniform(0, 100)
        self.__dead_time = uniform(0, 10)

    def define_ss(self):
        """Define the first-order-plus-dead-time model ode. This is to be used with the scipy function `odeint`

        Args:

        Returns:
            state_space_model: state space representation of FOPDT

        """

        Kp = self.__gain
        taup = self.__time_constant
        thetap = self.__dead_time

        A = -1 / taup
        B = Kp / taup
        C = 1

        model = GEKKO(remote=False)
        x, y, u = model.state_space(A, B, C, D=None, discrete=True, dt=self.sample_time)
        cv_in = y[0]

        cv = model.CV()
        model.delay(cv_in, cv, thetap)  # delay of 4 steps (8 sec)

        return model

    @property
    def dead_time(self):
        return self.__dead_time

    @dead_time.setter
    def set_dead_time(self, dead_time):
        if dead_time < 0:
            raise ValueError(
                "Sorry you cannot have non-causal systems where an input affects a change in the past"
            )

        self.__dead_time = dead_time

    @property
    def time_constant(self):
        return self.__time_constante

    @time_constant.setter
    def set_time_constant(self, time_constant):
        self.__time_constant = time_constant

    @property
    def gain(self):
        return self.__gain

    @gain.setter
    def set_gain(self, gain):
        self.__gain = gain
