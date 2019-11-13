from typing import Iterable
from ..entity.models import ZipcodeFee
from ...domain.entity.region_entity import RegionEntity
from ...domain.entity.region_fee_entity import RegionFeeEntity
from ...domain.repository.region_fee_base import RegionFeeBase


class RegionFee(RegionFeeBase):
    
    def findByState(self, state: str) -> RegionFeeEntity:
        """docstring"""

        return ZipcodeFee.objects(region__state=state).first() 
        
    def findByZipcode(self, zipcode: int) -> RegionFeeEntity:
        """docstring"""
        query = {
            "region.start_zipcode": {"$lte": zipcode},
            "region.end_zipcode": {"$gte": zipcode}
        }

        fee_data = ZipcodeFee.objects(__raw__=query).first()
        region_entity = RegionEntity(
            fee_data.region.state,
            fee_data.region.start_zipcode,
            fee_data.region.end_zipcode,
            fee_data.region.max_base_items,
            fee_data.region.extra_item_tax
        )
        
        fee_entity = RegionFeeEntity(
            fee_data.base_price, fee_data.num_days, region_entity)

        return fee_entity
    
    def findByDays(self, num_days: int) -> Iterable[RegionFeeEntity]:
        """docstring"""
        raise NotImplementedError()

    def findByValue(self, value: int) -> Iterable[RegionFeeEntity]:
        """docstring"""
        raise NotImplementedError()