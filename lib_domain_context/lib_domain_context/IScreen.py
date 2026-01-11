from abc import ABC, abstractmethod;
from lib_domain_context import Enumerables;

class IScreen:
    @abstractmethod
    def Loading(self, action: int) -> None:
        pass;

    @abstractmethod
    def MoveFocus(self) -> None:
        pass;

    @abstractmethod
    def Change(self, data: dict) -> None:
        pass;