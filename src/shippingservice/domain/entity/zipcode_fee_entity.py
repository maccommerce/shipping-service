from .region_entity import RegionEntity


class ZipcodeFeeEntity(object):
    """
    Class that represents the domain entity that models shipping fees defined by
    zip code regions.
    """
    
    def __init__(self, base_price: int, num_days: int, region: RegionEntity):
        self.__base_price = base_price
        self.__num_days = num_days
        self.__region = region
    

    @property
    def base_price(self) -> int:
        return self.__base_price
    
    @base_price.setter
    def base_price(self, new_price: int):
        self.__base_price = new_price

    @property
    def num_days(self) -> int:
        return self.__num_days
    
    @num_days.setter
    def num_days(self, new_num_days: int):
        self.__num_days = new_num_days
    
    @property
    def region(self) -> RegionEntity:
        return self.__region
    
    @region.setter
    def region(self, new_region: RegionEntity):
        self.__region = new_region