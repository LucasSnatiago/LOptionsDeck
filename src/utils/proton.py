import protonup
import os

class proton():
    def __init__(self) -> None:
        self.installDir = os.path.expanduser('~/.steam/root/compatibilitytools.d/')

    # Get Latest Release's infos of Proton GE from github
    def latestRelease(self) -> dict:
        data = protonup.fetch_data(tag="latest")
        return data

    # Verify if has new release of Proton GE
    def newRelease(self) -> bool:
        if os.path.exists(self.installDir):
            installedVersions = os.listdir(self.installDir)
            latest = self.latestRelease()
            latestVer = latest['version']
            
            if latestVer in installedVersions:
                return False
        
        return True

    # Download new release
    def downloadNewRealease(self):
        latest = self.latestRelease
        url = latest["download"]
        tempDir = "/tmp/proton/"
        tempDir += url.split('/')[-1]
        tempDir = os.path.expanduser(tempDir)
        os.mkdir(tempDir)

        if not protonup.api.download(url=url, destination=tempDir, show_progress=False):
            return

        tarfile.open(tempDir, "r:gz").extractall(self.installDir)
        shutil.rmtree(tempDir)
