from abc import ABC, abstractmethod;

class ICacheHelper:
    @abstractmethod
    def Add(self, key: str, value: object) -> None:
        pass;
    
    @abstractmethod
    def Instance(self) -> None:
        pass;

    @abstractmethod
    def Contains(self, key: str) -> bool:
        pass;

    @abstractmethod
    def Get(self, key: str) -> object:
        pass;

    @abstractmethod
    def Remove(self, key: str) -> None:
        pass;
    
class CacheDictionary(ICacheHelper):
    data: dict = None;

    def Add(self, key: str, value: object) -> None:
        self.Instance();
        self.data[key] = value;

    def Instance(self) -> None:
        if self.data != None:
            return;
        self.data = {};

    def Contains(self, key: str) -> bool:
        self.Instance();
        if key in self.data:
            return True;
        return False;

    def Get(self, key: str) -> object:
        self.Instance();
        if not self.Contains(key):
            return None;
        return self.data[key];

    def Remove(self, key: str) -> None:
        self.Instance();
        if not self.Contains(key):
            return;
        del self.data[key];
        
class CacheHelper:
    iCacheHelper: ICacheHelper = None;
    
    @staticmethod
    def Add(key: str, value: object) -> None:
        CacheHelper.CreateInstance();
        CacheHelper.iCacheHelper.Add(key, value);
        
    @staticmethod
    def CreateInstance(iCacheHelper: ICacheHelper = None) -> None:
        if CacheHelper.iCacheHelper != None:
            return;
        if iCacheHelper != None:
            CacheHelper.iCacheHelper = iCacheHelper;
        elif CacheHelper.iCacheHelper == None:
            CacheHelper.iCacheHelper = CacheDictionary();
        
    @staticmethod
    def Contains(key: str) -> bool:
        CacheHelper.CreateInstance();
        return CacheHelper.iCacheHelper.Contains(key);
    
    @staticmethod
    def Get(key: str) -> object:
        CacheHelper.CreateInstance();
        return CacheHelper.iCacheHelper.Get(key);
    
    @staticmethod
    def Remove(key: str) -> None:
        CacheHelper.CreateInstance();
        CacheHelper.iCacheHelper.Remove(key);