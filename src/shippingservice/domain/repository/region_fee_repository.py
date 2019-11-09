from abc import ABC, abstractmethod
from typing import Iterable
from entity.region_fee_entity import RegionFeeEntity


class RegionFeeRepository(ABC):

    @abstractmethod
    def findByState(state: str) -> RegionFeeEntity:
        raise NotImplementedError()

    @abstractmethod
    def findByZipcode(zipcode: int) -> RegionFeeEntity:
        raise NotImplementedError()

    @abstractmethod
    def findByDays(num_days: int) -> Iterable[RegionFeeEntity]:
        raise NotImplementedError()

    @abstractmethod
    def findByValue(value: int) -> Iterable[RegionFeeEntity]:
        raise NotImplementedError()