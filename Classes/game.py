import json
import os
import time
from .player import Player
from .room import Room


class Game:
    """
    Represents an instance of the game ScaryAttic.
    """
    def __init__(self, saveFile) -> None:
        self.running = True
        self.saveFile = saveFile
        self.currentSaveName = None
        self.rooms = []
        self.items = []
        self.player = Player()

        # Build instances of all the rooms
        self.buildRooms()
        # TODO: Rooms will need to be connected after all Rooms are created

    def isRunning(self):
        """
        Returns True if Game is still being played or False if user
        has exited the game.
        """
        return self.running

    def titleScreen(self):
        """
        Displays game title screen.
        """
        # TODO:: print title screen
        print("Welcome to the game! (placeholder)\n")
        print("Enter the command 'exit game' to stop playing.\n")

    def selectGameState(self):
        """
        Prompts the user to select a new game or load a saved game.
        """
        while True:
            # print message to input new game or load game
            print("Enter 'New' to start a new game or 'Load' to load a saved game:")
            userInput = input("> ")
            if userInput.replace(" ", "").lower() == "new":
                self.newGameIntro()
                return  # Default game state is new game
            if userInput.replace(" ", "").lower() == "load":   
                print("!!! UNDER CONSTRUCTION !!!")
                # TODO::
                # print names of available saveSates (not default state)
                # take input for selected save and load corresponding saveState
            else:
                print("That's not a valid option.")

    def newGameIntro(self):
        """
        Displays introduction at the start of a new game.
        """
        # Set directory path to narrative file
        path = os.path.realpath(__file__)
        dir = os.path.dirname(path)
        dir = dir.replace("Classes", "Narrative")
        os.chdir(dir)

        # Open narrative file and print new game intro
        with open("../Narrative/newGameIntro.json") as introFile:
            newGameIntro = json.load(introFile)
        print("")
        print(newGameIntro["newGameIntro1"],"\n")
        time.sleep(5)
        print(newGameIntro["newGameIntro2"],"\n")
        time.sleep(5)
        print(newGameIntro["newGameIntro3"],"\n")
        time.sleep(5)

    def saveGame(self):
        """
        Saves the current state of a Game to file.
        """
        if self.currentSaveName is None:
            # TODO:: Prompt user to enter new save name
            # Write saveState object to file with new save name
            # Set currentSaveName to new save name
            pass
        # TODO:: overwrite game state to saveState with name==currentSaveName
        # overwrite player inventory and location
        # overwrite room states

    def loadGame(self, loadName):
        """
        Loads a Game state from file.
        """
        # TODO:: Set state of game to state with loadName
        # Update user inventory and location states
        # Update room states
        self.currentSaveName = loadName

    def exitGame(self):
        """
        Confirms user input and terminates the current game instance.
        """
        print("Are you sure you want to exit the game? Any unsaved progress will be lost.")
        exitInput = input("Y / N: ").replace(" ", "").lower()
        while exitInput not in ["y", "yes", "n", "no"]:
            print("Your response was not valid. Are you sure you want to exit the game?")
            exitInput = input("Y / N: ").replace(" ", "").lower()
        if exitInput == "y" or exitInput == "yes":
            self.running = False

    def buildRooms(self):
        """
        Builds room instances automatically from files
        """
        # Iterate through all Room JSON Files and build the instances
        room_dir = "Rooms"
        for filename in os.listdir(room_dir):
            file = os.path.join(room_dir, filename)
            # If it's a valid file, create the Room
            if os.path.isfile(file):
                self.rooms.append(Room(file))
