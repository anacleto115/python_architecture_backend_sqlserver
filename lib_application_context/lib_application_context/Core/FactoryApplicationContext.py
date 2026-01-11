from lib_domain_context import IFactory, Enumerables, IApplication;
from lib_application_context.Implementations import PersonTypesApp;

class FactoryApplicationContext(IFactory.IFactory):
    def Get(self, data: dict) -> object:
        implementation: IApplication.IApplication = None;
        _type: int = data["Type"];
        if _type == Enumerables.Types.PersonTypes:
            implementation = PersonTypesApp.PersonTypesApp(data);
        return implementation;