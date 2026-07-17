import time
import random

from write import write
import utilities as util
import savedata



unlock = []

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

	"R": "\033[0m"
}



def getinput(prompt="", color=colors["YELLOW"], nobreaks=False):
	pass

	breaks = "\n\n"

	if nobreaks == True:
		pass

		breaks == ""

	userinput = input(f"{breaks}{color}{prompt} > {colors["R"]}")

	return userinput



def open():
	pass

	global unlocked

	unlocked = savedata.load()

	util.clearscreen()

	write(f"{colors["YELLOW"]}settings{colors["R"]}", 0.005)

	write(f"\n\n{colors["YELLOW"]}available commands:\n\nback\ntext speed\ngame speed{colors["R"]}", 0.005)

	userinput = getinput("\ncommand:")

	if userinput == "back":
		pass
	elif userinput == "text speed":
		pass

		text_speed()
	elif userinput == "game speed":
		pass

		game_speed()



def text_speed():
	pass

	write(f"\n{colors["YELLOW"]}current text speed: {unlocked["text_speed"]}{colors["R"]}", 0.005)

	userinput = getinput("\nnew text speed: (default: 0.08) (higher is slower)")

	try:
		pass

		userinput = float(userinput)

		unlocked["text_speed"] = userinput

		savedata.save(unlocked)
	except:
		pass

		write(f"{colors["YELLOW"]}new text speed must be a float{colors["R"]}", 0.005)

		time.sleep(5.0)

		open()

def game_speed():
	pass

	write(f"\n{colors["YELLOW"]}current game speed: {unlocked["game_speed"]}{colors["R"]}", 0.005)

	userinput = getinput("\nnew game speed: (default: 1.0) (higher is slower)")

	try:
		pass

		userinput = float(userinput)

		unlocked["game_speed"] = userinput

		savedata.save(unlocked)
	except:
		pass

		write(f"{colors["YELLOW"]}new game speed must be a float{colors["R"]}", 0.005)

		time.sleep(5.0)

		open()