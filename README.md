## Details:

* Groove Music Rich Presence will pull the metadata from the now playing file
* There was another one written in c#, while that one works I created a python version with a similar but also different approach 
* This version also has a coutdown for the length of the song
* No Admin Privaleges are required here
* The terminal prompt will display the current song and artist playing
* discordRichGroove.py and the release both are command line versions that still work
* discordRichGrooveGUI.pyw was added recently with a new GUI and features such as multithreading and minimizing to tray
* The GUI will automatically update in discord but will have to be refreshed on the GUI to update it
* The GUI version has also been optimized better and code has been neated up
* ![image](https://user-images.githubusercontent.com/31010418/116780230-e4e87300-aa40-11eb-8fa7-7f0ab34a62f7.png)
* ![image](https://user-images.githubusercontent.com/31010418/116780242-fa5d9d00-aa40-11eb-819d-a9b8f9ed07af.png)
* ![image](https://user-images.githubusercontent.com/31010418/116780251-0ba6a980-aa41-11eb-9091-860d8ea5e6f2.png)



# How to Use:
## For command line version:
* Download the exe from the Releases tab
* Music must be in the "Music" folder of Windows, if not see below
* If you want the music to be in a different folder then go into the code on line 19, change the "\Music" to "\YourFolder". The code will have to be recompiled with the command "pyinstaller .\discordRichGroove.py --onefile" after installing pyinstaller or you could just run the code natively and leave it running.
# For GUI version:
* Install python and run "pip install PyQt5 pypresence qdarkstyle audio_metadata" for the required libraries
* Download the .pyw file and run it

# Known bugs or future improvements:

* ~~The startup for the utility is a little long from some limitations with how I am grabbing the file~~ Fixed and file cut down by compiling in a fresh enviroment
* ~~A GUI that can be minimized into the system tray instead of having a terminal window always open
* The length of the song is calculated with system time + length of song found in the meta data. If the music is paused or scrubbed then the timer will not update. This is a current limitation to as I do not know a way to pull that information from a UWP app like Groove Music currently.
* ~~If nothing pops up in the terminal after a while, try playing a song till it displays something. If nothing is displayed, restart the app and try again. The open_files() function or the print function can act up sometimes.~~ kinda fixed but still bugs 1% of the time
