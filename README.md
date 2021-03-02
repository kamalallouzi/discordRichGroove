## Details:

* Groove Music Rich Presence will pull the metadata from the now playing file
* There was another one written in c#, while that one works I created a python version with a similar but also different approach 
* This version also has a coutdown for the length of the song
* No Admin Privaleges are required here
* The terminal prompt will display the current song and artist playing

## How to Use:

* Download the exe from the Releases tab
* Music must be in the "Music" folder of Windows, if not see below
* If you want the music to be in a different folder then go into the code on line 19, change the "\Music" to "\YourFolder". The code will have to recompiled with the command "pyinstaller .\discordRichGroove.py --onefile" after installing pyinstaller or you could just run the code natively and leave it running.

## Known bugs or future improvements:

* The startup for the utility is a little long from some limitations with how I am grabbing the file
* A GUI that can be minimized into the system tray instead of having a terminal window always open
* The length of the song is calculated with system time + length of song found in the meta data. If the music is paused or scrubbed then the timer will not update. This is a current limitation to as I do not know a way to pull that information from a UWP app like Groove Music currently.
* If nothing pops up in the terminal after a while, try playing a song till it displays something. If nothing is displayed, restart the app and try again. The open_files() function or the print function can act up sometimes.
