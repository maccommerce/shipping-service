from abc import ABC, abstractmethod
from repository.region_fee_repository import RegionFeeRepository
from entity.shipping_request_entity import ShippingRequestEntity
from adapters.shipping_data import ShippingData



class ShippingCalcService(ABC):
    """docstring"""

    @abstractmethod
    def calculate_fee(shipping_info: ShippingData) -> float:
        raise NotImplementedError()


class RegionShippingCalc(ShippingCalcService):
    """docstring"""

    def __init__(self, shipping_repo: RegionFeeRepository):
        self.shipping_repo = shipping_repo

    def calculate_fee(self, shipping_info: ShippingData) -> float:
        """docstring"""
        
        region = self.shipping_repo.findByZipcode(shipping_info.value)
        shipping_request = ShippingRequestEntity(
            shipping_info.label, shipping_info.quantity, region)
        
        return shipping_request.get_shipping_cost()
    