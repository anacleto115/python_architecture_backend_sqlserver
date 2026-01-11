from abc import ABC, abstractmethod;

class IService:
    @abstractmethod
    def Select(self, data: str) -> str:
        pass;

    @abstractmethod
    def Insert(self, data: str) -> str:
        pass;

    @abstractmethod
    def Update(self, data: str) -> str:
        pass;

    @abstractmethod
    def Delete(self, data: str) -> str:
        pass;