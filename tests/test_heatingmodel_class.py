import pytest
from homeheating import HeatingModel


def test_heatingmodel_FOPDT():
    heatingmodel_FOPDT = HeatingModel(
        model_type="FOPDT",
        add_noise=False,
    )


def test_heatingmodel_FOPDT_with_noise():
    heatingmodel_FOPDT_with_noise = HeatingModel(
        model_type="FOPDT",
        add_noise=True,
    )
    assert heatingmodel_FOPDT_with_noise.noise_avg == 0
    assert heatingmodel_FOPDT_with_noise.noise_stdev == 1
