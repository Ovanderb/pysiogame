pySioGame - Educational Activity Pack for Kids
www.pysiogame.net

Please note - this application is playable but still unfinished - or rather is being continuously improved (not so much recently - not enough hours in a day).

Please let me know if you find any errors or bugs in the application or in translations, formulas or other content.

pySioGame is built with Linux users in mind - written in python and tested on Ubuntu, however it does work on Windows just not tested as thoroughly as on Linux.

The application is intended to be compatible with python 2.7.3+ including python 3.x.

----------------------------------------------
Installation:

Detailed installation instructions available at: www.pysiogame.net/installation/

Linux installation:

    In order to run this application you need the python-pygame package installed.
    To check if you have it run the following lines in terminal (Ctrl+Atl+T):
    $ python
    >>> import pygame
    >>> exit()
    If you have no errors importing it you are set, else you need to install it, in Debian based distros run:
    $ sudo apt-get install python-pygame

    Also if you are going to use Hebrew or Arabic lanugage please install python-pyfribidi package:
    $ sudo apt-get install python-pyfribidi

    If you would like to enable the voice you also need eSpeak which - if you are using Linux, is most likely already installed, if you are using any other OS - well no luck - I'm afraid it won't work - but can't test it really.

    In some cases you may also need to install fonts-freefont-ttf (Debian) or ttf-freefont (Ubuntu) or gnu-free-sans-fonts (Fedora) or equivalent in your distro - maintainers please add it to dependencies.

    To start the application from terminal:
    python /home/user/path/to/the/app/pysiogame.py

    #or using python3:
    python3 /home/user/path/to/the/app/pysiogame.py

    Should start with double click if marked as executable (Right-click -> Properties -> Permissions -> Allow executing file as program) or if you like you can create a custom launcher using one of the above lines for the command line field (obviously after changing the path to the program first). The pysiogame.ico file from res/icon folder can be used as the icon for the launcher.


----------------------------------------------
Windows running the exe file:

    If you happen to have a winexe version and you are reading this file it means you have it unpacked somewhere on your hard drive. All you need to do is to run the pysiogame.exe file.
    However if you would like to use its text to speech capabilities you will have to install espeak from http://espeak.sourceforge.net/download.html


Windows installation of required software to run from source.

    If you would rather run the software from source here's how:

    Download and install python 2.7 32bit - http://www.python.org/getit/
    Download and install pygame for python 2.7 + 32bit  - http://www.pygame.org/install.html
    Download and install espeak 32bit - http://espeak.sourceforge.net/download.html

    Add espeak to your path (visit www.pysiogame.net/installation/ if you are not sure how)
    Depending on your OS you may need to add one of the following to your your PATH variable:
    C:\Program Files (x86)\eSpeak\command_line;
    or
    C:\Program Files\eSpeak\command_line;
    or something else depending where your eSpeak is installed.

    Download pySioGame and extract it somewhere, for example C:\pysiogame

    To run pysiogame you can add a shortcut on the desktop to:
    C:\python27\python.exe C:\pysiogame\pysiogame.py

----------------------------------------------

The first time the application is run will be in normal windowed mode (not in fullscreen).
To display it in fullscreen press Ctrl+F at the start of the or go to Preferences (in login screen) and enable full screen.

----------------------------------------------
Translating:
    If you would like to help translating this application please use one of the included files within the i18n/po directory.
    If your langauage is not there yet copy the default.pot file rename it temporarily to te_ST.po and start working with the new file using ie. the Poedit.
    To test your translation save the file - Poedit will create the .mo file for you - move the .mo file to the locale/te_ST/ directory and rename the file to pysiogame.mo and start the app select the Test Language.
    Alternatively you can run the cleanup.py program to get the file renamed and moved where it should be (this program will also remove .pyc and some other temp files under pysiogame - this is used to automate the process of stripping pysiogame before compressing/packaging).

    There are some things translated using custom translation files in custom directory - these are usually done by me - but I might need some help to do them - I will get in touch with you if I'll be struggling.

    When everything is working ok please email me your .po file.

    The es_di.py, fr_di.py, etc. are lists of words used by word building activities.
    These are partial (google) translations from English. The English version is just a list of words most commonly used in English - you may like to check these as well for any words not necessarily suitable for children.
----------------------------------------------

Interface:
Menu Panel - left:
    left column         - list of categories
    right column        - list of activities in the current category

Top Panel:
    sound               - toggle sound effects
    voice               - toggle espeak voice synthesiser (if espeak is not installed this icon will not be available)
    colour modes        - switch between colour modes (full colour, black on white, white on black, yellow on black
    user name           - displays name of currently logged in user
    logout link         - takes you back to the initial screen where you can login as a different user

Controls - top:
    (some of these buttons are being hidden in some activities if they are not needed)

    tick button (ok)      - used to let the app know you have completed the task
                            and it's ready to be checked you can use ENTER instead to speed this up

    reload                - used to reload the task, or reset it to the start position
                            may be useful in the Connect activities if it appears unsolvable

    activity title        - displays current activity title (optional) when cursor is over the Activity panel
                            and acts as a hint text when cursor is over menu icons

    left/right arrows     - change levels or just some aspect of the activity (ie. photo to piece together)

    left/right            - fast forward/backward - will move by preset amount of levels or
    double arrows           to skip to the next type of activity (available in some activities
                            with large number of levels)

    level indicator       - top number is the level you are on, the bottom pair of numbers is usually
                            current game in the level / number of games per level
                            if there's no number of games at the bottom it's up to you to change the level
                            when ready for harder task.

    close button          - closes the application (2 clicks needed)

Activity Panel - centre - the largest part of screen:
    piece of screen where all activity objects are placed for you to drag around :)


Sorry for all the mess in the code, but this is my first and only pygame project after reading some books/tutorials, so do not expect professional product - this was my programming sandbox.
It was intended as a tool for my son to learn. He liked it so hopefully your kid(s) will like it too.

Enjoy!

Ireneusz Imiolek
