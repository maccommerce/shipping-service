class RegionEntity(object):
    """
    Class that represents a territorial region and its zip codes.
    """
    
    def __init__(
        self,
        state: str,
        start_zipcode: int,
        end_zipcode: int,
        max_base_items: int,
        extra_item_tax: float):
        
        self.__state = state
        self.__start_zipcode = start_zipcode
        self.__end_zipcode = end_zipcode
        self.__max_base_items = max_base_items
        self.__extra_item_tax = extra_item_tax

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, new_state: str):
        self.__state = new_state

    @property
    def start_zipcode(self) -> int:
        return self.__start_zipcode

    @start_zipcode.setter
    def start_zipcode(self, new_zipcode: int):
        self.__start_zipcode = new_zipcode

    @property
    def end_zipcode(self) -> int:
        return self.__end_zipcode

    @end_zipcode.setter
    def end_zipcode(self, new_zipcode: int):
        self.__end_zipcode = new_zipcode

    @property
    def max_base_items(self) -> int:
        return self.__max_base_items

    @max_base_items.setter
    def max_base_items(self, new_max: int):
        self.__max_base_items = new_max

    @property
    def extra_item_tax(self) -> float:
        return self.__extra_item_tax

    @extra_item_tax.setter
    def extra_item_tax(self, new_tax: float):
        self.__extra_item_tax = new_tax