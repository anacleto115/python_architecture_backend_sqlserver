from abc import ABC, abstractmethod;

class IFactory:
    @abstractmethod
    def Get(self, data: dict) -> object:
        pass;