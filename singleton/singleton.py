"""
This code shows how the Singleton pattern can be implemented in Python.
The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.
"""

class Singleton:
    __instance = None

    @staticmethod 
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("The Singleton class is initialized more than once!")
        else:
            Singleton.__instance = self

    def showMessage(self):
        print("An instance of a Singleton")

Singleton.getInstance().showMessage()