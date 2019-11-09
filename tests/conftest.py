import pytest
import random

from src.shippingservice.domain.entity.zipcode_fee_entity import (
    ZipcodeFeeEntity
)

from src.shippingservice.domain.entity.region_entity import RegionEntity

@pytest.fixture(scope='module')
def new_zipcode_fee():
    new_region = RegionEntity("Some State", 60417235, 60455996)

    new_fee = ZipcodeFeeEntity(
        random.randint(10, 30), random.choice([5,10,15,20,25]), new_region)

    return new_fee