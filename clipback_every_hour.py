#iJ

import time
import pyperclip
from PIL import ImageGrab
from datetime import datetime


error = "<Error> Something went wrong"
success = "<Success> Backup done " + str(datetime.now())

while True:

    hours = datetime.now().hour
    minutes = datetime.now().minute

    if minutes == 0:
        image = ImageGrab.grabclipboard()
        
        if image:
            try:
                image.save("image.png")
                print(success)
            except:
                print(error)

        if not image:
            try:
                with open("text.txt", "w") as file:
                    text = pyperclip.paste()
                    file.write(text.replace("\n", ""))
                print(success)
            except:
                print(error)

    time.sleep(30)