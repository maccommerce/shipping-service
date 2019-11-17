from .region_fee_entity import RegionFeeEntity


class ShippingRequestEntity(object):

    def __init__(
        self, zipcode: str, num_items: int, region_fee: RegionFeeEntity):
        
        self.__zipcode = zipcode
        self.__num_items = num_items
        self.__region_fee = region_fee

    def get_shipping_cost(self) -> float:
        """
            Provides the shipping cost for a given shipping request.
        """
        
        if self.__num_items <= self.__region_fee.region.max_base_items:
            total = self.__region_fee.base_price
        else:
            extra_items = (
                self.__num_items - self.__region_fee.region.max_base_items
            )

            extra_tax = self.__region_fee.region.extra_item_tax * extra_items

            total = self.__region_fee.base_price * (1.0 + extra_tax)

        return total

    @property
    def zipcode(self) -> str:
        return self.__zipcode
    
    @zipcode.setter
    def zipcode(self, new_zipcode: str):
        self.__zipcode = new_zipcode

    @property
    def num_items(self) -> int:
        return self.__num_items
    
    @num_items.setter
    def num_items(self, new_num_items: int):
        self.__num_items = new_num_items
    
    @property
    def region_fee(self) -> RegionFeeEntity:
        return self.__region_fee
    
    @region_fee.setter
    def region_fee(self, new_region_fee: RegionFeeEntity):
        self.__region_fee = new_region_fee