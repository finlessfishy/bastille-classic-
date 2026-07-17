import os
import msvcrt
import plyer



def restart():
    pass

    clearscreen()

    os.system("run.cmd")
    os.system("taskkill /IM 'WindowsTerminal.exe' /F")

def clearscreen():
    pass

    os.system('cls' if os.name == 'nt' else 'clear')

def clearinput():
    pass

    while msvcrt.kbhit():
        pass

        msvcrt.getch()



def makefile(location="desktop", filename="filename", content="content", type=".txt"):
    pass

    homedir = os.path.expanduser('~')

    filepath = ""

    if location == "desktop":
        pass
        
        try:
            pass

            filepath = os.path.join(homedir, 'Downloads', 'Desktop')
        except:
            pass

            return   
    elif location == "downloads":
        pass

        filepath = os.path.join(homedir, 'Downloads')
    elif location == "game":
        pass

        filepath = os.path.join(homedir, 'Documents', 'python', 'bastille')
    elif location == "export":
        pass

        os.makedirs("exports", exist_ok=True)

        filepath = os.path.join(homedir, 'Documents', 'python', 'bastille', 'exports')

    filename = f"{filename}{type}"

    filepath = os.path.join(filepath, filename)

    with open(filepath, 'w') as f:
        pass
        
        f.write(content)

def makenotification(n_title="title", n_message="message", n_appname="appname", n_timeout=10):
    pass

    plyer.notification.notify(
        title=n_title,
        message=n_message,
        app_name=n_appname,
        timeout=n_timeout
    )