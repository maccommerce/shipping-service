class RegionEntity(object):
    """
    Class that represents a territorial region and its zip codes.
    """
    
    def __init__(self, state: str, start_zipcode: int, end_zipcode: int):
        self.__state = state
        self.__start_zipcode = start_zipcode
        self.__end_zipcode = end_zipcode

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
    def end_zipcode(self, new_zipcode):
        self.__end_zipcode = new_zipcode