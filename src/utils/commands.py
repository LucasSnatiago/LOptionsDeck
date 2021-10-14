from xml.etree import ElementTree
from dataclasses import dataclass

@dataclass
class OptionData():
    name: str
    command: str
    descrition: str

class OptionParser():

    def __init__(self, path : str) -> None:
        self.commands = ElementTree.parse(path)

    def save(self, name:str,command: str, descrition: str):
        root = self.commands.getroot()

        new_option = ElementTree.SubElement(root, "option", {"name": name})
        com = ElementTree.SubElement(new_option, "command")
        com.text = command
        desc = ElementTree.SubElement(new_option, "description")
        desc.text = descrition
        element = root.append(new_option)

    def find(self, name: str) -> OptionData:
        el = self.commands.find(f"option[name={name}]")
        if el == None: return

        command = el.find("command").text
        description = el.find("description").text

        return OptionData(name=name, command=command, descrition=description)