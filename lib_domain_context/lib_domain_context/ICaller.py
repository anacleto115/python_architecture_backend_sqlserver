from abc import ABC, abstractmethod;
from lib_domain_context import IFactory;

class ICaller:
    @abstractmethod
    def Execute(self, data: dict) -> dict:
        pass;

class FactoryCaller:
    iFactoryCaller: IFactory.IFactory = None;
    
    @staticmethod
    def Get(data: dict) -> object:
        if FactoryCaller.iFactoryCaller == None:
            return None;

        return FactoryCaller.iFactoryCaller.Get(data);
    
    @staticmethod
    def SetFactory(value: IFactory.IFactory) -> None :
        FactoryCaller.iFactoryCaller = value;
        
    @staticmethod
    def GetFactory() -> IFactory.IFactory:
        return FactoryCaller.iFactoryCaller;