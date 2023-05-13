"""
This code demonstrates how to use the Abstract Factory pattern in Python to create a GUI factory that can create
buttons and checkboxes for different platforms (Windows and Mac).

The Abstract Factory pattern provides an interface for creating families of related objects without specifying
their concrete classes.
"""

from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class WinButton(Button):
    def paint(self):
        print("Windows Button")

class MacButton(Button):
    def paint(self):
        print("Mac Button")

class CheckBox(ABC):
    @abstractmethod
    def paint(self):
        pass

class WinCheckBox(CheckBox):
    def paint(self):
        print("Windows CheckBox")

class MacCheckBox(CheckBox):
    def paint(self):
        print("Mac CheckBox")

class GUIFactory(ABC):
    @abstractmethod
    def createButton(self) -> Button:
        pass

    @abstractmethod
    def createCheckBox(self) -> CheckBox:
        pass

class WinFactory(GUIFactory):
    def createButton(self) -> Button:
        return WinButton()

    def createCheckBox(self) -> CheckBox:
        return WinCheckBox()

class MacFactory(GUIFactory):
    def createButton(self) -> Button:
        return MacButton()

    def createCheckBox(self) -> CheckBox:
        return MacCheckBox()

if __name__ == "__main__":
    # Create an instance of the factory based on the platform
    import sys
    if sys.platform == "win32":
        factory = WinFactory()
    else:
        factory = MacFactory()

    # Use the factory to create a button and a checkbox
    button = factory.createButton()
    button.paint()
    checkbox = factory.createCheckBox()
    checkbox.paint()

    # Clean up
    del button
    del checkbox