from pypresence import Presence
from time import time, sleep
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QSystemTrayIcon, QStyle, QAction, QMenu
from PyQt5.QtGui import QFont, QIcon
import qdarkstyle
import sys
import os
import psutil
import audio_metadata
from threading import Thread
import queue
import multiprocessing
from multiprocessing import Process, Queue
RPC = Presence(805717663975473162)
RPC.connect()
def window():
    def refreshGUI():
        for i in range(q.qsize()-1):
            q.get()
        while not q.empty():
            titleArtist.setText(q.get())
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('a.ico'))
    window = QMainWindow()
    window.setWindowIcon(QIcon('a.ico'))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

    window.setGeometry(300, 300, 300, 200)
    window.setWindowTitle("Groovy Rich Presence")

    titleArtist = QtWidgets.QLabel(window)
    titleArtist.setGeometry(50, 50, 1000, 100)
    titleArtist.move(3,5)
    titleArtist.setFont(QFont('Segoe', 12))

    button = QPushButton(window)
    button.setText("Refresh GUI")
    button.move(100, 150)
    button.clicked.connect(refreshGUI)

    trayIcon = QSystemTrayIcon()
    trayIcon.setIcon(window.style().standardIcon(QStyle.SP_MediaPlay))
    show_action = QAction("Show")
    hide_action = QAction("Hide")
    show_action.triggered.connect(window.show)
    hide_action.triggered.connect(window.hide)
    tray_menu = QMenu()
    tray_menu.addAction(show_action)
    tray_menu.addAction(hide_action)
    trayIcon.setContextMenu(tray_menu)
    trayIcon.show()

    window.show()
    sys.exit(app.exec_())
    
def updateDiscord():
    while True:
        try:
            pid = os.popen('wmic process get description, processid').read()
            pid = int(pid[pid.index("Music.UI.exe") + 12: pid.index("Music.UI.exe") + 45])
            p = psutil.Process(pid)
            openHandles = p.open_files()
            matching = [s for s in openHandles if "\Music" in str(s)]
            music = str(matching[0])
            info = music[music.index("path=") + 6: music.index(", fd") - 1]
            info = info.replace('\\\\', '/')
            metadata = audio_metadata.load(info)
            if infoTemp == info:
                sleep(1)
            else:
                infoTemp = info
                metadata = audio_metadata.load(info)
                q.put("Artist: " + metadata.tags['artist'][0]+ "\nSong: " + metadata.tags['title'][0])
                RPC.update(state=metadata.tags['artist'][0], details=metadata.tags['title'][0], large_image="groove", small_image="mad", large_text="Groove Music", small_text="madge", end=int(time())+int(metadata.streaminfo['duration']))
        except ValueError:
            RPC.update(state="Idle", details="Idle", large_image="groove", small_image="mad", large_text="Groove Music", small_text="madge")
            q.put("Groove Music not running")
        except IndexError:
            RPC.update(state="Idle", details="Idle", large_image="groove", small_image="mad", large_text="Groove Music", small_text="madge")
            q.put("Idle")
        except NameError:
            infoTemp = info
q = Queue()
richThread = Thread(target=updateDiscord)
richThread.daemon = True
richThread.start()
window()
