# Interface 
from abc import ABCMeta,  abstractmethod

class Clothes(): 

    @abstractmethod
    def mensclothes(self): pass

    @abstractmethod
    def womenclothes(self): pass
   
    @abstractmethod
    def childrenclothes(self): pass
