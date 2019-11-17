from ..service.shipping_calc import RegionShippingCalc
from ..repository.region_fee_base import RegionFeeBase
from .shipping_data import ShippingData


class ShippingRequestAdapter(object):

    def __init__(self, shipping_repo: RegionFeeBase):
        self.shipping_service = RegionShippingCalc(shipping_repo)
    
    def get_service_cost(self, zipcode: str, quantity: int) -> float:
        """docstring"""
        shipping_data = self.__shipping_to_data(zipcode, quantity)
        return self.shipping_service.calculate_fee(shipping_data)

    @classmethod
    def __shipping_to_data(cls, zipcode: str, quantity: int) -> ShippingData:
        """docstring"""
        region_value = int(zipcode.split('-')[0])
        return ShippingData(
            label=zipcode, value=region_value, quantity=quantity)
