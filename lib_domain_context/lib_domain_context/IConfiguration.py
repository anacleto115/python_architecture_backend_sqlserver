from abc import ABC, abstractmethod;

class IConfiguration:
    @abstractmethod
    def Get(self, key: str) -> str:
        pass;