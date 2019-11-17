from abc import ABC, abstractmethod
from ..repository.region_fee_base import RegionFeeBase
from ..entity.shipping_request_entity import ShippingRequestEntity
from ..adapters.shipping_data import ShippingData



class ShippingCalcService(ABC):
    """docstring"""

    @abstractmethod
    def calculate_fee(shipping_data: ShippingData) -> float:
        raise NotImplementedError()


class RegionShippingCalc(ShippingCalcService):
    """docstring"""

    def __init__(self, shipping_repo: RegionFeeBase):
        self.shipping_repo = shipping_repo

    def calculate_fee(self, shipping_data: ShippingData) -> float:
        """docstring"""
        
        region_fee = self.shipping_repo.findByZipcode(shipping_data.value)
        shipping_request = ShippingRequestEntity(
            shipping_data.label, shipping_data.quantity, region_fee)
        
        return shipping_request.get_shipping_cost()
    