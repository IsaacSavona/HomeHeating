import random

# A global registry to store model types
model_registry = {}


def register_model(model_type: str):
    """Decorator to register a new model class."""

    def decorator(cls):
        model_registry[model_type] = cls
        return cls

    return decorator


class HeatingModel:
    def __init__(self, model_type: str, add_noise: bool, sample_time: float):
        # Lookup the model type in the registry
        model_class = model_registry.get(model_type)
        if model_class is None:
            raise ValueError(f"Model type '{model_type}' is not registered.")

        # Initialize the model
        self.__model = model_class()
        self.add_noise = add_noise
        self.sample_time = sample_time
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
    def set_noise_stdev(self, noise_stdev: float):
        if noise_stdev < 0:
            raise ValueError("Sorry you cannot have a negative standard deviation")

        self.__noise_stdev = noise_stdev

    # getter method for the average of the added noise
    @property
    def noise_avg(self):
        return self.__noise_avg

    # setter method for the average of the added noise
    @noise_avg.setter
    def set_noise_avg(self, noise_avg: float):
        self.__noise_avg = noise_avg

    # random noise property which can be added to a system
    @property
    def noise(self):
        # Assign a random number to the noise variable
        return random.gauss(mu=self.__noise_stdev, sigma=self.__noise_avg)
