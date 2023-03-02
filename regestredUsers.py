import numpy

class User:
    def __init__(self,user:str,passwd:str):
        self.user = user
        self.passwd = passwd
        self.toDos = list()

    def appendToDos(self,todos:list):
        self.toDos.append(todos)
    def setToDos(self,todos:list):
        self.toDos = todos
    def getToDos(self):
        return self.toDos
