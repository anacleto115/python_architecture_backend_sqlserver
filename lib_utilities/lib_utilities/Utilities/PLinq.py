class JLinqList:
    list: list = None;

    def __init__(self, list: list):
        self.list = list;
        
    def ToList(self) -> list:
        return self.list;

    def ToArray(self) -> list:
        return self.list;

    def AsEnumerable(self) -> list:
        return self.list;
    
    def ToDictionary(self, condition = None) -> dict:
        response = {};
        temp = set([condition(x) for x in self.list]);
        count = 0;
        for item in temp:
            count = count + 1;
            response[str(count)] = item;
        return response;

    def Where(self, condition) -> object:
        return JLinqList([x for x in self.list if condition(x)]);

    def Select(self, condition) -> object:
        list: list = [];
        for x in self.list:
            if condition(x):
                list.append(True);
            else:
                list.append(False);
        return list;

    def OrderBy(self, condition = None) -> list:
        if condition == None:
            return self.list;
        return [condition(x) for x in self.list];

    def OrderByDesc(self, condition = None) -> list:
        response = self.OrderBy(condition);
        response.reverse();
        return response;

    def Join(self, list: list) -> object:
        return JLinqList(self.list + list);

    def GroupBy(self, condition = None) -> dict:
        return self.ToLookup(condition);

    def ToLookup(self, condition = None) -> dict:
        response: dict = { };
        temp = [condition(x) for x in self.list];
        for item in temp:
            response[item] = temp.count(item)
        return response;
    
    def Union(self, list: list) -> object:
        return JLinqList(set(self.list) | set(list));

    def Distinct(self, condition = None) -> list:
        return set([condition(x) for x in self.list]);

    def Intersect(self, list: list) -> object:
        return JLinqList(set(self.list) & set(list));

    def Except(self, list: list) -> object:
        return JLinqList(set(self.list) - set(list));
    
    def Any(self, condition = None) -> bool:
        for x in self.list:
            if condition(x):
                return True;
        return False;
    
    def All(self, condition = None) -> bool:
        for x in self.list:
            if not condition(x):
                return False;
        return True;
    
    def Constain(self, item) -> bool:
        for x in self.list:
            if x == item:
                return True;
        return False;
    
    def Take(self, size) -> object:
        response = [];
        count = 0;
        for item in self.list:
            count = count + 1;
            response.append(item);
            if count > size:
                return JLinqList(response);
        return JLinqList(response);
    
    def Skip(self, size) -> object:
        response = [];
        count = 0;
        for item in self.list:
            count = count + 1;
            if count <= size:
                continue;
            response.append(item);
        return JLinqList(response);
    
    def TakeWhile(self, condition = None) -> object:
        response = [];
        for item in self.list:
            if condition(item):
                response.append(item);
        return JLinqList(response);
    
    def SkipWhile(self, condition = None) -> object:
        response = [];
        for item in self.list:
            if not condition(item):
                response.append(item);
        return JLinqList(response);
    
    def First(self, condition = None) -> object:
        return self.FirstOrDefault(condition);
    
    def FirstOrDefault(self, condition = None) -> object:
        response: list = None;
        if len(self.list) == 0:
            return None;
        if condition == None:
            return self.list[0];
        else:
            for item in self.list:
               if condition(item):
                   return item;
        return None;
    
    def Last(self, condition = None) -> object:
        return self.LastOrDefault(condition);

    def LastOrDefault(self, condition = None) -> object:
        response: list = None;
        if len(self.list) == 0:
            return None;
        if condition == None:
            return self.list[len(self.list)-1];
        else:
            temp = self.OrderByDesc(None);
            for item in temp:
                if condition(item):
                    return item;
        return None;

    def ElementAt(self, position = None) -> object:
        return self.ElementAtOrDefault(position);

    def ElementAtOrDefault(self, position = None) -> object:
        if len(self.list) < position:
            return None;
        response = self.list[position];
        if response == None:
            return None;
        return response;

    def Count(self, condition = None) -> object:
        response: list = [];
        if len(self.list) == 0:
            return 0;
        if condition == None:
            return len(self.list);
        else:
            for item in self.list:
                if condition(item):
                    response.append(item);
        return len(response);

    def Sum(self, condition = None) -> int:
        return sum([condition(x) for x in self.list]);

    def Min(self, condition = None) -> int:
        return min([condition(x) for x in self.list]);

    def Max(self, condition = None) -> int:
        return max([condition(x) for x in self.list]);

    def Average(self, condition = None) -> float:
        response = [condition(x) for x in self.list];
        return sum(response) / len(response);

class PLinq(object):
    @staticmethod
    def From(list: list) -> JLinqList:
        if list == None:
            return None;
        return JLinqList(list);