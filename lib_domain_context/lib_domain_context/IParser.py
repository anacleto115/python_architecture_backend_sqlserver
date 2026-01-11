from abc import ABC, abstractmethod;

class IParser:
    @abstractmethod
    def CreateEntity(self, ItemArray: list) -> object:
        pass;

    @abstractmethod
    def ToEntity(self, data: dict) -> object:
        pass;

    @abstractmethod
    def ToDictionary(self, entity: object) -> dict:
        pass;

    @abstractmethod
    def Validate(self, entity: object) -> bool:
        pass;