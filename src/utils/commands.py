from xml.etree import ElementTree

path = "data/commands.xml"


tree = ElementTree.parse(path)

for option in tree.findall("option"):
    print(option.get("name"), ": ", option.find("command").text)
