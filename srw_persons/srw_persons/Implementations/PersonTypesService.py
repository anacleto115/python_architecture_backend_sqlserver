from srw_persons.Core import ServiceBase;
from lib_domain_context import Enumerables;
from lib_application_core.Core import FactoryApplication;

class PersonTypesService(ServiceBase.ServiceBase):
    def Load(self, data: dict) -> dict:
        data = super().Load(data);
        data["Type"] = Enumerables.Types.PersonTypes; 
        if self.iApp == None and not "IApplication" in data.keys():
            self.iApp = FactoryApplication.FactoryApplication.Get(data);
        return data;