from abc import ABC, abstractmethod;

class IRepository:
    @abstractmethod
    def Select(self, data: dict) -> dict:
        pass;

    @abstractmethod
    def Insert(self, data: dict) -> dict:
        pass;

    @abstractmethod
    def Update(self, data: dict) -> dict:
        pass;

    @abstractmethod
    def Delete(self, data: dict) -> dict:
        pass;

