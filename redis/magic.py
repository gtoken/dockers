from time import sleep
from datetime import datetime
import webbrowser
import subprocess
import urllib
import os
download_asset = False
camouflage = True
confessed = False

def confess():
    print """


 _        _____   _____   _____       __    __      ___  
| |      /  ___| /  _  \ |_   _|      \ \  / /     /   | 
| |      | |     | | | |   | |         \ \/ /     / /| | 
| |      | |  _  | | | |   | |          \  /     / / | | 
| |      | |_| | | |_| |   | |          / /     / /  | | 
|_|      \_____/ \_____/   |_|         /_/     /_/   |_| 



Hello Kait,

When this message gets to you, the fun has already began hahaha

Don't freak out. It is just some simple python scripts, no privacy or security is compromised.

Once this script stops, everything stops. I have no access to your computer.

Why I am doing this? Because home is far and I was bored :)

Hope you have some good laughs. I would pay anything to see your surprised face.

Cheers

"""


while True:
    if camouflage:
        print """
        Step 78 : RUN mkdir -p /etc/nginx/sites-enabled/
        ---> Using cache
        ---> 5ee2f9b9a91f
        """
        sleep(3)
        print """
        Step 79 : RUN ln -s /etc/nginx/sites-available/goplay-python /etc/nginx/sites-enabled/goplay-python
        ---> Using cache
        ---> 610ec18a61bb
        """
        sleep(3)
        print """
        Step 80 : RUN rm /etc/nginx/sites-available/default
        ---> Using cache
        ---> 1d2ef224d36b
        """
        sleep(3)
        print """
        Step 81 : RUN rm /etc/nginx/sites-enabled/default
        ---> Using cache
        ---> 7b6f3d030f42
        """
        sleep(3)
        print """
        Step 82 : ADD start.sh .
        ---> Using cache
        ---> ff07f23ee84a
        """
        sleep(3)
        print """
        Step 83 : RUN chmod 775 start.sh
        ---> Using cache
        ---> ccd97497f9e3
        """
        sleep(3)
        print """
        Step 84 : ENTRYPOINT /start.sh
        ---> Using cache
        ---> b8948d4f9cc7
        """
        sleep(3)
        print """
        Step 85 : EXPOSE 80
        ---> Using cache
        ---> 010f84c5b7c4
        """
        sleep(3)
        print """
        Step 86 : CMD
        ---> Using cache
        ---> 20e23b8acbf5
        """
        sleep(3)
        print """
        Successfully built 20e23b8acbf5
        ERROR:  role "goplaydb" already exists
        ALTER ROLE
        ERROR:  database "goplaydb" already exists
        """
    else:
        sleep(60)
    if not download_asset:
        testfile = urllib.URLopener()
        testfile.retrieve("https://www.dropbox.com/s/tssoarn5t2ssgxm/recording20150520221241.mp3?dl=0", "1.mp3")
        testfile.retrieve("https://www.dropbox.com/s/hw46xredetkd5qx/recording20150520221345.mp3?dl=0", "2.mp3")
        download_asset = True

    current = datetime.now()
    if current.hour >= 2: # go off at 2PM
        camouflage = False
        if not confessed:
            confess()
            confessed = True
        if current.minute >= 14 and current.minute <= 15:
            webbrowser.open('https://i.warosu.org/data/vr/img/0024/16/1432151589868.png', new=2, autoraise=True)
        elif current.minute >= 24 and current.minute <= 25:
            webbrowser.open('http://9gag.com/gag/aP4q9nn?sc=gif', new=2, autoraise=True)
        elif current.minute >= 33 and current.minute <= 34:
            webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&autoplay=1', new=2, autoraise=True)
        elif current.minute >= 44:
            webbrowser.open('https://www.youtube.com/watch?v=nDGKW3PmtkA&autoplay=1', new=2, autoraise=True)
            break
    if current.hour >= 3:
        break
