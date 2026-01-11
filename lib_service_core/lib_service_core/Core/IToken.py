from abc import ABC, abstractmethod;

class IToken:
    @abstractmethod
    def Validate(self, data: dict) -> bool:
        pass;

    @abstractmethod
    def Authenticate(self) -> str:
        pass;