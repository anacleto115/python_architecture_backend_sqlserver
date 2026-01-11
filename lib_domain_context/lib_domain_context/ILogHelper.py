import sys;
from abc import ABC, abstractmethod;

class ILogHelper:
    @abstractmethod
    def Log(self, exception: Exception) -> None:
        pass;

class LogHelper:
    iLogHelper: ILogHelper = None;
    
    @staticmethod
    def Log(exception: Exception) -> None:
        if LogHelper.iLogHelper == None:
            return None;

        return LogHelper.iLogHelper.Log(exception);