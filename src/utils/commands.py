from xml.etree import ElementTree

class CommandParser():

    def __init__(self, path : str) -> None:
        self.commands = ElementTree.parse(path)

    def find_with_name(self, name: str):
        return self.commands.find(f"option[name={name}]")