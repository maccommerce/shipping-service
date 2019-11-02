import pytest
import random

from src.shippingservice.domain.entity.zipcode_fee_entity import (
    ZipCodeFeeEntity
)

from src.shippingservice.domain.entity.region_entity import RegionEntity

@pytest.fixture(module='local')
def new_zipcode_fee_entity():
    new_region = RegionEntity()

    new_fee = ZipCodeFeeEntity(
        random.randint(10, 30), random.choice([5,10,15,20,25], new_region))
