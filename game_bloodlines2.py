import os
import mobase

from PyQt6.QtCore import QDir, qInfo
from ..basic_game import BasicGame

class Vampire2Game(BasicGame):

    Name = "VtM:B 2"
    Author = "iunPause"
    Version = "1.1.1"
    GameName = "Vampire: The Masquerade - Bloodlines 2"
    GameShortName = "vtmbloodlines2"
    GameNexusName = "vtmbloodlines2"
    GameBinary = "Bloodlines2.exe"
    GameSteamId = 532790

    GameDataPath = "Bloodlines2/Content/Paks/~mods"
    _local_app_data = os.environ["LOCALAPPDATA"]
    GameDocumentsDirectory = os.path.join(_local_app_data, "Bloodlines2", "Steam", "Saved")
    GameSaveExtension = "sav"
    
    GameIniFiles = [
        os.path.join(_local_app_data, "Bloodlines2", "Steam", "Saved", "Config", "Windows", "GameUserSettings.ini"),
        os.path.join(_local_app_data, "Bloodlines2", "Steam", "Saved", "Config", "Windows", "Engine.ini"),
    ]

    def savesDirectory(self):
        return QDir(self.documentsDirectory().absoluteFilePath("SaveGames"))

    def init(self, organizer: mobase.IOrganizer) -> bool:
        initialized = super().init(organizer)
        qInfo(f"Resolved SAVE GAMES: {self.savesDirectory().absolutePath()}")
        for ini_path in self.iniFiles():
            qInfo(f"Resolved GAME INI: {ini_path}")
        return initialized

    # Snippet taken from the Kingdom Come Deliverance plugin
    def initializeProfile(self, directory: QDir, settings: mobase.ProfileSetting):
        # Create the mods directory if it doesn't exist
        modsPath = self.dataDirectory().absolutePath()
        os.makedirs(modsPath, exist_ok=True)

        super().initializeProfile(directory, settings)