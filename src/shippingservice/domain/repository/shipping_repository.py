from abc import ABC, abstractmethod
from typing import Iterable
from entity.zipcode_fee_entity import ZipcodeFeeEntity


class ShippingRepository(ABC):

    @abstractmethod
    def findByState(state: str) -> ZipcodeFeeEntity:
        raise NotImplementedError()

    @abstractmethod
    def findByZipcode(zipcode: int) -> Iterable[ZipcodeFeeEntity]:
        raise NotImplementedError()

    @abstractmethod
    def findByDays(num_days: int) -> Iterable[ZipcodeFeeEntity]:
        raise NotImplementedError()

    @abstractmethod
    def findByValue(value: int) -> Iterable[ZipcodeFeeEntity]:
        raise NotImplementedError()