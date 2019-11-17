from abc import ABC, abstractmethod
from typing import Iterable
from ..entity.region_fee_entity import RegionFeeEntity


class RegionFeeBase(ABC):

    @abstractmethod
    def findByState(self, state: str) -> RegionFeeEntity:
        raise NotImplementedError()

    @abstractmethod
    def findByZipcode(self, zipcode: int) -> RegionFeeEntity:
        raise NotImplementedError()

    @abstractmethod
    def findByDays(self, num_days: int) -> Iterable[RegionFeeEntity]:
        raise NotImplementedError()

    @abstractmethod
    def findByValue(self, value: int) -> Iterable[RegionFeeEntity]:
        raise NotImplementedError()