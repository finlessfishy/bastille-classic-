import sys
import time
import random

import getweirdfont as font
import savedata



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

unlocked = []



def write(string="null", delay=0.08, israndom=False, nogamespeed=False):
	pass

	global unlocked

	if nogamespeed == False:
		pass

		unlocked = savedata.load()

		if delay >= 0:
			pass

			try:
				pass

				delay = delay * unlocked["game_speed"]
			except:
				pass
		else:
			pass

			try:
				pass

				delay = delay / unlocked["game_speed"]
			except:
				pass

	lastcolor = ""

	if string != "null":
		pass

		for char in string:
			pass

			letter = f"{char}"

			if israndom == True:
				pass

				color = ""
				letter = ""

				if char == " ":
					pass

					color = "\033[40m\033[0;31m"

					letter = f"{color}{char}{colors["R"]}"
				elif char == "'":
					pass

					color = "\033[40m\033[0;31m"

					letter = f"{color}{char}{colors["R"]}"
				elif char == "?":
					pass

					color = "\033[40m\033[0;31m"

					letter = f"{color}{char}{colors["R"]}"
				else:
					pass

					rng = random.randint(1, 16)

					if rng == 1:
						color = "\033[31m" # red
					elif rng == 2:
						color = "\033[1;31m" # bold red
					elif rng == 3:
						color = "\033[0;91m" # high intensity red
					elif rng == 4:
						color = "\033[35m" # purple
					elif rng == 5:
						color = "\033[41m\x1b[30m" # red background, black
					elif rng == 6:
						color = "\033[0;101m\x1b[30m" # high intensity red background, black
					elif rng == 7:
						color = "\033[4;31m" # bold high intensity red
					elif rng == 9:
						color = "\033[45m\x1b[30m" # purple background, black
					elif rng == 10:
						color = "\033[0;33m" # yellow
					elif rng == 11:
						color = "\033[43m\x1b[30m" # yellow background, black
					elif rng == 12:
						color = "\033[42m\x1b[30m" # green background, black
					elif rng == 14:
						color = "\033[46m\x1b[30m" # cyan background, black
					elif rng == 15:
						color = "\033[44m\x1b[30m" # blue background, black
					elif rng == 16:
						color = "\033[41m\x1b[0;37m" # red background, white
					else:
						color = colors["RED"]

					letter = f"{font.getweirdfont(char)}"

					if letter != " ":
						pass

						if random.randint(1, 6) == 6:
							pass

							letter = f"{letter}{colors["R"]} "

					letter = f"{color}{letter}{colors["R"]}"

			sys.stdout.write(letter)
			sys.stdout.flush()

			time.sleep(delay)
	else:
		pass

		return