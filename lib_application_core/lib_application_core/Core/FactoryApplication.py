from lib_domain_context import IFactory;

class FactoryApplication:
    iFactoryApplication: IFactory.IFactory = None;
    
    @staticmethod
    def Get(data: dict) -> object:
        if FactoryApplication.iFactoryApplication == None:
            return None;

        return FactoryApplication.iFactoryApplication.Get(data);
    
    @staticmethod
    def SetFactory(value: IFactory.IFactory) -> None :
        FactoryApplication.iFactoryApplication = value;
        
    @staticmethod
    def GetFactory() -> IFactory.IFactory:
        return FactoryApplication.iFactoryApplication;