from lib_domain_context import IFactory;

class FactoryRepository:
    iFactoryRepository: IFactory.IFactory = None;
    
    @staticmethod
    def Get(data: dict) -> object:
        if FactoryRepository.iFactoryRepository == None:
            return None;

        return FactoryRepository.iFactoryRepository.Get(data);
    
    @staticmethod
    def SetFactory(value: IFactory.IFactory) -> None :
        FactoryRepository.iFactoryRepository = value;
        
    @staticmethod
    def GetFactory() -> IFactory.IFactory:
        return FactoryRepository.iFactoryRepository;