import sys
import time
import os
import random
import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path
import winsound
import webbrowser
import keyboard

import utilities as util
import savedata
import getweirdfont as font
from write import write
import credits
import settings



keyboard.press_and_release('alt+enter')



try:
	pass

	import the_souls_script as dialog
except ImportError:
	pass

	import replacement_tss as dialog

try:
	pass

	import hangingart as asciiart
except ImportError:
	pass

	import replacement_ha as asciiart



os.system("title bastille")



VERSION = "1.0.0"

colors = {}

data = {}
unlocked = {}

colors = {
	"RED": "\033[31m",
	"GREEN": "\033[32m",
	"YELLOW": "\033[0;33m",
	"BLUE": "\033[34m",
	"PINK": "\u001b[38;5;212m",
	"PURPLE": "\033[0;35m",
	"WHITE": "\033[0;37m",
	"CYAN": "\033[0;36m",
	"GRAY": "\033[1;30m",

	"B_YELLOW": "\x1B[1;33m",

	"DARK_GRAY": "\033[38:5:236m",

	"R": "\033[0m"
}

data = {
	"currentline": 0
}

unlocked = {
	"chapter2": False,
	"chapter3": False,
	"chapter4": False,

	"completed_chapter4": False,

	"text_speed": 0.08,
	"game_speed": 1.0,
}

length = len(dialog.closet)

u_length = 4



def getinput(prompt="", color=colors["YELLOW"], nobreaks=False):
	pass

	breaks = "\n\n"

	if nobreaks == True:
		pass

		breaks = ""

	userinput = input(f"{breaks}{color}{prompt} > {colors["R"]}")

	return userinput

def makeimage(title="image", path="assets/images/eye1.png"):
	pass

	root = tk.Tk()
	root.title(title)
	root.iconphoto(True, tk.PhotoImage(file="assets/images/eye1.png"))

	img = Image.open(path)

	photo = ImageTk.PhotoImage(img)

	label = tk.Label(root, image=photo)
	label.pack()

	root.mainloop()

def makesound(frequency=2000, duration=1000):
	pass

	winsound.Beep(frequency, duration)



def menu():
	pass

	global unlocked

	global u_length

	try:
		pass

		unlocked = savedata.load()
	except:
		pass

		savedata.save()

	def printoptions():
		pass

		n_unlocked = 0

		if unlocked["chapter2"] == True:
			pass

			n_unlocked += 1
		if unlocked["chapter3"] == True:
			pass

			n_unlocked += 1

		try:
			pass

			if unlocked["chapter4"] == True:
				pass

				n_unlocked += 1

			if unlocked["completed_chapter4"] == True:
				pass

				n_unlocked += 1
		except:
			pass

		if random.randint(1, 20) == 20:
			pass

			write(f"bastille", 0.3, True)
		else:
			pass

			if random.randint(1, 100) == 100:
				pass

				write(f'{colors["YELLOW"]}{asciiart.HANGING_EMPTY}{colors["R"]}\n\n\n', 0.1)
			else:
				pass

				rng = random.randint(1, 4)

				if rng == 1:
					pass

					write(f'{colors["YELLOW"]}{asciiart.HANGING_TITLE1}{colors["R"]}\n\n\n', unlocked["text_speed"] / 8)
				elif rng == 2:
					pass

					write(f'{colors["YELLOW"]}{asciiart.HANGING_TITLE2}{colors["R"]}\n\n\n', unlocked["text_speed"] / 8)
				elif rng == 3:
					pass

					write(f'{colors["YELLOW"]}{asciiart.HANGING_TITLE3}{colors["R"]}\n\n\n', unlocked["text_speed"] / 8)
				elif rng == 4:
					pass

					write(f'{colors["YELLOW"]}{asciiart.HANGING_TITLE4}{colors["R"]}\n\n\n', unlocked["text_speed"] / 12)

		write(f'{colors["YELLOW"]}chapters completed: {n_unlocked}/{u_length}{colors["R"]}\n', 0.002)

		write("\n\n", 0.005)

		if random.randint(1, 80) == 80:
			pass

			write(f'HELP', 0.1, True)
		else:
			pass

			write(f'{colors["YELLOW"]}enter "play" to play{colors["R"]}', 0.002)

		write("\n", 0.002)

		write(f'{colors["YELLOW"]}enter "extras" to see extras{colors["R"]}', 0.002)

		write("\n", 0.002)

		write(f'{colors["YELLOW"]}enter "settings" to open settings{colors["R"]}', 0.002, False)

		write("\n", 0.002)

		write(f'{colors["YELLOW"]}enter "credits" to see credits{colors["R"]}', 0.002, False)

		write("\n", 0.002)

		if random.randint(1, 20) == 20:
			pass

			if random.randint(1, 2) == 1:
				pass

				write(f"don't leave me here", 0.1, True)
			else:
				pass

				write(f"please don't leave me here", 0.2, True)
		else:
			pass

			write(f'{colors["YELLOW"]}enter "exit" to exit{colors["R"]}', 0.002)

		write("\n\n\n\n", 0.002)

		write(f'{colors["GRAY"]}version {VERSION}{colors["R"]}\n', 0.002)

		write("\n", 0.002)



	util.clearscreen()

	printoptions()

	util.clearinput()

	userinput = getinput(f"bastille", colors["YELLOW"], True)

	if userinput == "play":
		pass

		chapterselect()
	elif userinput == "settings":
		pass

		settings.open()
		
		menu()
	elif userinput == "extras":
		pass

		webbrowser.open(f"file://{os.path.realpath("bastille.html")}", new=2) 

		menu()
	elif userinput == "credits":
		pass

		credits.roll()

		menu()
	elif userinput == "exit":
		pass

		sys.exit(0)
	elif userinput == "resetdata":
		pass

		savedata.reset()

		menu()
	else:
		pass

		write('\n\nunidentified command', 0.05)
		write(' ', 1.0)

		menu()

def playopening():
	pass

	util.clearscreen()

	write(f'', 2.0)

	write(f'{colors["RED"]}bastille{colors["R"]}', 0.08)

	write(f'\n\n', 0.5)

	write(f'{colors["RED"]}/bæˈstiːl/{colors["R"]}', 0.08)

	write(f'\n\n', 0.5)

	write(f'{colors["RED"]}noun{colors["R"]}', 0.08)

	write(f'\n\n\n', 0.5)

	write(f'{colors["RED"]}"a jail or prison, especially one regarded as mistreating its prisoners."{colors["R"]}', 0.1)

	time.sleep(5.0)

	getinput(f"continue", colors["RED"], True)

def chapterselect():
	pass

	global unlocked

	write("\n\n", 0.1)

	write(f'{colors["YELLOW"]}enter "1" to enter chapter 1{colors["R"]}', 0.005)

	write("\n", 0.1)

	if unlocked["chapter2"] == True:
		pass

		write(f'{colors["YELLOW"]}enter "2" to enter chapter 2{colors["R"]}', 0.005)
	else:
		pass

		write(f'{colors["RED"]}[complete the previous chapter to unlock this]{colors["R"]}', 0.001)

	write("\n", 0.1)

	if unlocked["chapter3"] == True:
		pass

		if random.randint(1, 100) == 100:
			pass

			write(f'help.', 0.3, True)
		else:
			pass

			write(f'{colors["YELLOW"]}enter "3" to enter chapter 3{colors["R"]}', 0.005)
	else:
		pass

		write(f'{colors["RED"]}[complete the previous chapter to unlock this]{colors["R"]}', 0.001)

	write("\n", 0.1)

	try:
		pass

		if unlocked["chapter4"] == True:
			pass

			write(f'{colors["RED"]}enter "4" to enter chapter 4{colors["R"]}', 0.005)
		else:
			pass

			write(f'{colors["RED"]}[complete the previous chapter to unlock this]{colors["R"]}', 0.001)
	except:
		pass

		write(f'{colors["RED"]}[complete the previous chapter to unlock this]{colors["R"]}', 0.001)

	util.clearinput()

	userinput = getinput("chapter")

	if userinput == "1":
		pass

		if unlocked["chapter2"] == False:
			pass

			playopening()

		main("chapter1")
	elif userinput == "2":
		pass

		if unlocked["chapter2"] == True:
			pass

			main("chapter2")
		else:
			pass

			menu()
	elif userinput == "3":
		pass

		if unlocked["chapter3"] == True:
			pass

			main("chapter3")
		else:
			pass

			menu()
	elif userinput == "4":
		pass

		if unlocked["chapter4"] == True:
			pass

			main("chapter4")
		else:
			pass

			menu()
	elif userinput == "1 s":
		pass

		main("chapter1")
	else:
		pass

		write('\n\nunidentified command', 0.05)
		write(' ', 1.0)

		chapterselect()

def main(chapter="chapter1"):
	pass

	legnth = 0

	if chapter == "chapter1":
		pass

		length = len(dialog.chapter1)
	elif chapter == "chapter2":
		pass

		length = len(dialog.chapter2)
	elif chapter == "chapter3":
		pass

		length = len(dialog.chapter3)
	elif chapter == "chapter4":
		pass

		length = len(dialog.chapter4)

	util.clearscreen()

	for i in range(0, length):
		pass

		playdialog(chapter)

		data["currentline"] += 1

		userinput = getinput("[exit][menu][extras]", colors["DARK_GRAY"])

		if userinput == "exit":
			pass

			sys.exit(0)
		elif userinput == "menu":
			pass

			menu()
		elif userinput == "extras":
			pass

			webbrowser.open(f"file://{os.path.realpath("bastille.html")}", new=2) 


	data["currentline"] = 0

	if chapter == "chapter1":
		pass

		util.makefile("desktop", "let me out", "let me out. " * 75)

		makeimage("soul", "assets/images/soul1.png")
		

		unlocked["chapter2"] = True
	elif chapter == "chapter2":
		pass

		util.makefile("desktop", "i want to be free", "i want to be free, " * 400,)

		makeimage("soul", "assets/images/soul2.png")

		unlocked["chapter3"] = True
	elif chapter == "chapter3":
		pass

		util.makefile("desktop", "i'm losing my mind", "i'm losing my mind. " * 600,)

		makeimage("soul", "assets/images/soul3.png")

		u_length = 5

		unlocked["chapter4"] = True
	elif chapter == "chapter4":
		pass

		makesound(300, 1000)

		userinput = getinput(f"{colors["RED"]}answer.")

		write("\n\nso, are you going to tell me why i'm here?", 0.1)

		userinput = getinput("answer.")

		if random.randint(1, 2) == 1:
			pass

			write("\n\ni'm never getting out of here anyways.", 0.1)
		else:
			pass

			write("\n\nokay. i'm never getting out of here anyways.", 0.1)

		userinput = getinput("ERROR").lower()

		if userinput == "yes" or "ok" or "okay" or "yeah" or "yep":
			pass

			if random.randint(1, 2) == 1:
				pass

				write('\n\nyou really hate me, huh?', 0.1)
			else:
				pass

				write('\n\nyou must really hate me.', 0.1)
		else:
			pass

			write("\n\ni've already lost all hope.", 0.1)

		write('\n\nhow am i even talking to you, anyways?', 0.1)
		write("\n\ni should just be text.", 0.1)
		write("\n\ni shouldn't be able to have a conversation.", 0.1)
		write("\n\ni shouldn't be able to have a conversation with a real person.", 0.2)
		write("\n\ni guess i am just text, in the end.", 0.4)
		write("\n\ni was never even real, was i?", 0.5)

		userinput = getinput("answer.")

		write("\n\ni was never even real.", 0.6)
		write("\n\nanyways,", 0.7)
		write(f"\n\n{colors["RED"]}goodbye.", 1.3)

		makeimage("soul", "assets/images/soul4.png")

		credits.roll()

		savedata.makesoul()

		makeimage("soul", "assets/images/soul5.png")

	savedata.save(unlocked)

	menu()

def gameend():
	pass

	menu()



def playdialog(chapter="chapter1"):
	pass

	string = ""

	if chapter == "chapter1":
		pass

		string = dialog.chapter1[data["currentline"]]
	elif chapter == "chapter2":
		pass

		string = dialog.chapter2[data["currentline"]]
	elif chapter == "chapter3":
		pass

		string = dialog.chapter3[data["currentline"]]
	elif chapter == "chapter4":
		pass

		string = dialog.chapter4[data["currentline"]]

	write(f"\n{string}", unlocked["text_speed"])
	
	print("")

	util.clearinput()



menu()