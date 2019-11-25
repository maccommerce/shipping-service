import pytest
import random

from src.app.domain.entity.region_fee_entity import (
    RegionFeeEntity
)

from src.app.domain.entity.region_entity import RegionEntity

@pytest.fixture(scope='module')
def new_zipcode_fee():
    new_region = RegionEntity(
        "Some State", 60417235, 60455996,
        random.choice([5,10,15,20,25]), random.random())

    new_fee = RegionFeeEntity(
        random.randint(10, 30), random.choice([5,10,15,20,25]), new_region)

    return new_fee