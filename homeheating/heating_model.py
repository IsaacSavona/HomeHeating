import random


class HeatingModel:
    def __init__(self, model_type, add_noise):
        self.model_type = model_type
        self.add_noise = add_noise
        self.__noise_stdev = 0.0  # default added noise is no noise
        self.__noise_avg = 0.0  # default added noise is no noise

        if self.add_noise:
            self.__noise_stdev = 1.0
            self.__noise_avg = 0.0

    # getter method for the standard deviation of the added noise
    @property
    def noise_stdev(self):
        return self.__noise_stdev

    # setter method for the standard deviation of the added noise
    @noise_stdev.setter
    def set_noise_stdev(self, noise_stdev):
        if noise_stdev < 0:
            raise ValueError("Sorry you cannot have a negative standard deviation")

        self.__noise_stdev = noise_stdev

    # getter method for the average of the added noise
    @property
    def noise_avg(self):
        return self.__noise_avg

    # setter method for the average of the added noise
    @noise_avg.setter
    def set_noise_avg(self, noise_avg):
        self.__noise_avg = noise_avg

    # random noise property which can be added to a system
    @property
    def noise(self):
        # Assign a random number to the noise variable
        return random.gauss(mu=self.__noise_stdev, sigma=self.__noise_avg)
