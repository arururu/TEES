class IdSet:    
    def __init__(self, firstNumber=1):
        self.Ids = {}
        self.firstNumber = firstNumber
        self._namesById = {}
    
    def getId(self, name, makeIfNotExist=True):
        if not self.Ids.has_key(name):
            if makeIfNotExist:
                id = len(self.Ids) + self.firstNumber
                self.Ids[name] = id
                self._namesById[id] = name
            else:
                return None
        return self.Ids[name]
    
    def getName(self, id):
        if self._namesById.has_key(id):
            return self._namesById[id]
        else:
            return None
    
    def getNames(self):
        names = self.Ids.keys()
        names.sort()
        return names
    
    def write(self, filename):
        f = open(filename, "wt")
        keys = self.Ids.keys()
        keys.sort()
        for key in keys:
            f.write(str(key)+": "+str(self.Ids[key])+"\n")
        f.close()
    
    def toStrings(self, rowLength=80):
        strings = [""]
        keys = self.Ids.keys()
        keys.sort()
        currLen = 0
        for key in keys:
            pair = str(key)+":"+str(self.Ids[key])
            currLen += len(pair) + 1
            if currLen > rowLength:
                currLen = 0
                strings.append("")
            if strings[-1] != "":
                strings[-1] += ";"
            strings[-1] += pair
        return strings
    
    def load(self, filename):
        self.Ids = {}
        self.firstNumber = 0
        
        f = open(filename, "rt")
        lines = f.readlines()
        f.close()
        for line in lines:
            key, value = line.split(":")
            key = key.strip()
            value = int(value.strip())
            if self.firstNumber > value:
                self.firstNumber = value
            self.Ids[key] = value
