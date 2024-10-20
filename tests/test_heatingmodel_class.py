import pytest
from homeheating import HeatingModel


def test_heatingmodel_FOPDT():
    heatingmodel_FOPDT = HeatingModel(
        model_type="FOPDT", add_noise=False, sample_time=0.1, time_steps=100
    )
    heatingmodel_FOPDT.model
    assert heatingmodel_FOPDT.noise_avg == 0
    assert heatingmodel_FOPDT.noise_avg == 0
    assert heatingmodel_FOPDT.noise == 0


def test_heatingmodel_FOPDT_with_noise():
    heatingmodel_FOPDT_with_noise = HeatingModel(
        model_type="FOPDT", add_noise=True, sample_time=0.1, time_steps=100
    )
    assert heatingmodel_FOPDT_with_noise.noise_avg == 0
    assert heatingmodel_FOPDT_with_noise.noise_stdev == 1
    assert heatingmodel_FOPDT_with_noise.noise <= 1
    assert heatingmodel_FOPDT_with_noise.noise >= -1
