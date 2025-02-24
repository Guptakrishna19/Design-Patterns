#implementing borg's singleton pattern in python
class Borg:
    shared_state = {}
    def __init__ (self):
        self.__dict__ = self.shared_state  
class Singleton(Borg):
    def __init__(self,value=None):
        super().__init__() #calling the parent class constructor
        if value is not None:
            self.value=value
    def set_value(self,value):
        self.value=value
    def get_value(self):
        return self.value
s1=Singleton()
s2=Singleton()
s1.set_value(10)
print(s1.get_value())
print(s2.get_value()) 




# Double Checked Locking singleton pattern
import threading
class SingletonDoubleChecked(object):
    # resources shared by each and every
    # instance
    __singleton_lock = threading.Lock()
    __singleton_instance = None
    
    
    @classmethod # this decorator define the classmethod
    def instance(cls):

        # check for the singleton instance
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls()

        # return the singleton instance
        return cls.__singleton_instance


# main method
if __name__ == '__main__':

    # create class X
    class X(SingletonDoubleChecked):
        pass

    # create class Y
    class Y(SingletonDoubleChecked):
        pass

    A1, A2 = X.instance(), X.instance()
    B1, B2 = Y.instance(), Y.instance()

    assert A1 is not B1 #this line contains assertions that are used to check the correctness of the code
    assert A1 is A2
    assert B1 is B2

    print('A1 : ', A1)
    print('A2 : ', A2)
    print('B1 : ', B1)
    print('B2 : ', B2)

           