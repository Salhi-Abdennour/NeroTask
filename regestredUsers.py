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

t = numpy.array([numpy.array([int]*5)]*9)

def sim(m,x,y):
    for i in range(0,y):
        for j in range(0,x):
            m[i,j] = 0
    for i in range(0,y):
        m[i,0] = 1

    for i in range(round(y/2)+1,y):
        for j in range(1,x):
            m[i,j] = m[i-1,j-1] + m[i-1,j]

    for i in range(0,y):
        t[i] = t[y-1-i]
sim(t,5,9)
print(t)