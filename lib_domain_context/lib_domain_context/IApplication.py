from abc import ABC, abstractmethod;

class IApplication:
    @abstractmethod
    def Load(self, data: dict) -> dict:
        pass;

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