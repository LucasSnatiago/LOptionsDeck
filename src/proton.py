import protonup
import os

class proton():
    def __init__(self) -> None:
        self.installDir = os.path.expanduser('~/.steam/root/compatibilitytools.d/')

    def latestRelease(self) -> dict:
        data = protonup.fetch_data(tag="latest")
        return data
