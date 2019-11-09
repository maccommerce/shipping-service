from service.shipping_calc import ShippingCalcService
from repository.region_fee_repository import RegionFeeRepository
from shipping_data import ShippingData


class ShippingRequestAdapter(object):

    def __init__(self, shipping_repo: RegionFeeRepository):
        self.shipping_service = ShippingCalcService(shipping_repo)
    
    def get_service_cost(self, zipcode: str, quantity: int) -> float:
        """docstring"""
        shipping_info = self.__shipping_to_data(zipcode, quantity)
        return self.shipping_service.calculate_fee(shipping_info)

    @classmethod
    def __shipping_to_data(cls, zipcode: str, quantity: int) -> ShippingData:
        """docstring"""
        zipcode_value = int("".join(zipcode.split('-')))
        return ZipcodeData(
            label=zipcode, value=zipcode_value, quantity=quantity)
