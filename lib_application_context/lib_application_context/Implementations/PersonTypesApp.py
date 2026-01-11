import sys;
from lib_application_core.Interfaces import IPersonTypesApp;
from lib_data_core.Core import FactoryRepository;
from lib_infrastructure.Implementations import PersonTypesParser;
from lib_application_context.Core import App;
from lib_domain_context import Enumerables;

class PersonTypesApp(App.App, IPersonTypesApp.IPersonTypesApp):
    def __init__(self, data: dict):
        pass;

    def Load(self, data: dict) -> dict:
        data = super().Load(data);
        if "Architecture" in data.keys() and data["Architecture"] == Enumerables.Architecture.Services: 
            self.parser = PersonTypesParser.PersonTypesParser();
        if not "IRepository" in data.keys(): 
            self.iRepository = FactoryRepository.FactoryRepository.Get(data);
        return data;