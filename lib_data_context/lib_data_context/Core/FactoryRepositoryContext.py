from lib_domain_context import Enumerables, IFactory, IRepository;
from lib_data_context.Implementations import PersonTypesRepository;

class FactoryRepositoryContext(IFactory.IFactory):
    def Get(self, data: dict) -> object:
        implementation: IRepository.IRepository = None;
        _type: int = data["Type"];
        if _type == Enumerables.Types.PersonTypes:
            implementation = PersonTypesRepository.PersonTypesRepository(data);
        return implementation;