import os
import pickle
import shutil



saved = False



def save(var):
    pass

    saved = True

    datatosave = ()

    datatosave = {
        "f_unlocked": var
    }

    os.makedirs("savedata", exist_ok=True)

    with open('savedata/savedata.bastille', 'wb') as f:
        pass

        pickle.dump(datatosave, f)

def load():
    pass

    global unlocked

    if os.path.isfile("savedata/savedata.bastille"):
        pass

        with open('savedata/savedata.bastille', 'rb') as f:
            pass

            loadeddata = pickle.load(f)

            unlocked = loadeddata["f_unlocked"]

            return loadeddata["f_unlocked"]
    else:
        pass

        u_var = {
            "chapter2": False,
            "chapter3": False,
            "chapter4": False,

            "completed_chapter4": False,

            "text_speed": 0.08,
        }

        return u_var

def reset():
    pass

    try:
        pass

        os.remove("savedata/savedata.skin")
        os.rmdir("savedata")
    except:
        pass



def makesoul():
    pass

    os.makedirs("soul", exist_ok=True)

    shutil.copy2("assets/soul/soul.exe", "soul")


