from xml.etree import ElementTree

class CommandParser():

    def __init__(self, path : str) -> None:
        self.commands = ElementTree.parse(path)

    def save(self, name:str,command: str, descrition: str):
        new_option = ElementTree.SubElement(self.commands.getroot, "option", {"name": name})
        com = ElementTree.SubElement(new_option, "command")
        com.text = command
        desc = ElementTree.SubElement(new_option, "description")
        desc.text = descrition
        element = self.commands.getroot().append(new_option)

    def find_with_name(self, name: str):
        return self.commands.find(f"option[name={name}]")