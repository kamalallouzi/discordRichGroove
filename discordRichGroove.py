from __future__ import print_function
from pypresence import Presence
from time import time
from time import sleep
from os import popen
from os import name
from os import system
from psutil import Process
import audio_metadata
RPC = Presence(805717663975473162)
RPC.connect()
def cls():
    system('cls' if name=='nt' else 'clear')
try:
    pid = popen('wmic process get description, processid').read()
    pid = int(pid[pid.index("Music.UI.exe") + 12: pid.index("Music.UI.exe") + 50])
    p = Process(pid)
    openHandles = p.open_files()
    matching = [s for s in openHandles if "\Music" in str(s)]
    music = str(matching[0])
    info = music[music.index("path=") + 6: music.index(", fd") - 1]
    info = info.replace('\\\\', '/')
    metadata = audio_metadata.load(info)
    infoTemp = info
    metadata = audio_metadata.load(info)
    RPC.update(pid=10276, state=metadata.tags['artist'][0], details=metadata.tags['title'][0], large_image="groove", small_image="mad", large_text="Groove Music", small_text="madge", end=int(time())+int(metadata.streaminfo['duration']))
except ValueError:
    print("Groove Music not running")
except IndexError: 
    RPC.update(pid=10276, state="Idle", details="Idle", large_image="groove", small_image="mad", large_text="Groove Music", small_text="madge")
while True:
    try:
        pid = popen('wmic process get description, processid').read()
        pid = int(pid[pid.index("Music.UI.exe") + 12: pid.index("Music.UI.exe") + 50])
        p = Process(pid)
        openHandles = p.open_files()
        matching = [s for s in openHandles if "\Music" in str(s)]
        music = str(matching[0])
        info = music[music.index("path=") + 6: music.index(", fd") - 1]
        info = info.replace('\\\\', '/')
        if infoTemp == info:
            sleep(3)
        else:
            infoTemp = info
            metadata = audio_metadata.load(info)
            RPC.update(pid=10276, state=metadata.tags['artist'][0], details=metadata.tags['title'][0], large_image="groove", small_image="mad", large_text="Groove Music", small_text="madge", end=int(time())+int(metadata.streaminfo['duration']))
            cls()
            print("Artist: ", metadata.tags['artist'][0], "\nSong: ", metadata.tags['title'][0])
    except ValueError:
        cls()
        print("Groove Music not running")
        RPC.update(pid=10276, state="Idle", details="Idle", large_image="groove", small_image="mad", large_text="Groove Music", small_text="madge")
    except IndexError:
        cls()
        print("Idle")
        RPC.update(pid=10276, state="Idle", details="Idle", large_image="groove", small_image="mad", large_text="Groove Music", small_text="madge")
    except NameError:
        infoTemp = info
