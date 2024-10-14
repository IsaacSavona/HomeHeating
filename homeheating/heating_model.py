class HeatingModel:
    def __init__(
        self, model_type, noise, constant_disturbance, time_varying_disturbance
    ):
        self.model_type = model_type
        self.noise = noise
        self.constant_disturbance = constant_disturbance
        self.time_varying_disturbance = time_varying_disturbance
