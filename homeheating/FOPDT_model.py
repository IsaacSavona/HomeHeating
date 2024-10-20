from random import uniform
from gekko import GEKKO
import numpy as np
from .heating_model import HeatingModel, register_model


@register_model("FOPDT")
class FOPDTModel:
    def __init__(self, heating_model: HeatingModel):
        # Access attributes from HeatingModel instance
        self.sample_time = heating_model.sample_time
        self.add_noise = heating_model.add_noise
        self.time_steps = heating_model.time_steps

        self.__gain = uniform(0, 100)  # can't have a negative temperature
        self.__time_constant = uniform(0, 100)
        self.__dead_time = uniform(0, 50)

    def define_ss(self):
        """Define the first-order-plus-dead-time model ode. This is to be used with the scipy function `odeint`

        Args:

        Returns:
            state_space_model: state space representation of FOPDT

        """

        Kp = self.gain
        taup = self.time_constant
        thetap = self.dead_time

        # Define state-space matrices as NumPy arrays
        # A = np.array([[-1 / taup]])  # 1 state, so shape (1, 1)
        # B = np.array([[Kp / taup]])   # 1 input, so shape (1, 1)
        # C = np.array([[1]])            # 1 output, so shape (1, 1)
        A = np.zeros((1, 1))
        B = np.zeros((1, 1))
        C = np.zeros((1, 1))
        A[0, 0] = -1 / taup
        B[0, 0] = Kp / taup
        C[0, 0] = 1

        # Create time array based on the sample time
        time_array = np.linspace(0, self.sample_time * self.time_steps, self.time_steps)

        # Initialize the GEKKO model
        model = GEKKO(remote=False)
        model.time = time_array  # Set the time array for the model

        x, y, u = model.state_space(A, B, C, D=None)

        cv_in = y[0]

        cv = model.CV()
        model.x = x
        model.y = y
        model.u = u

        delay_steps = int(thetap / self.sample_time)
        model.delay(cv_in, cv, delay_steps)
        model.cv = cv
        # delay_steps = int(thetap / self.sample_time)
        # if delay_steps != 0:
        #     model.delay(cv_in,cv,delay_steps)

        # model.delay(
        #     model.MV, model.CV, int(thetap / self.sample_time)
        # )  # delay with an integer number of time steps

        # # Define manipulated variable and controlled variable as attributes
        # self.mv = model.MV(value=0)  # Initialize MV
        # self.cv = model.CV(value=0)  # Initialize CV

        # # Set the manipulation over time (step change)
        # self.mv.value = np.zeros(self.time_steps)
        # self.mv.value[50:100] = 1  # Step change

        # # Delay in the system
        # model.delay(self.mv, self.cv, int(thetap / self.sample_time))

        return model

    @property
    def dead_time(self):
        return self.__dead_time

    @dead_time.setter
    def dead_time(self, dead_time):
        if dead_time < 0:
            raise ValueError(
                "Sorry you cannot have non-causal systems where an input affects a change in the past"
            )

        self.__dead_time = dead_time

    @property
    def time_constant(self):
        return self.__time_constant

    @time_constant.setter
    def time_constant(self, time_constant):
        self.__time_constant = time_constant

    @property
    def gain(self):
        return self.__gain

    @gain.setter
    def gain(self, gain):
        self.__gain = gain
