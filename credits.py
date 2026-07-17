import time

import utilities as util
from write import write



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



def roll():
	pass

	util.clearscreen()

	write(f"bastille", 0.5, True)



	write("\n\n\n\n\n", 0.02)

	write(f"{colors["WHITE"]}made by finlessfishy{colors["R"]}", 0.1)

	write("\n\n", 0.02)
	write(f"{colors["GRAY"]}code: finlessfishy{colors["R"]}", 0.1)

	write("\n", 0.02)
	write(f"{colors["GRAY"]}writing: finlessfishy{colors["R"]}", 0.1)

	write("\n", 0.02)
	write(f"{colors["GRAY"]}art: finlessfishy{colors["R"]}", 0.1)



	write("\n\n\n\n", 0.02)

	write(f"{colors["WHITE"]}ascii text fonts:{colors["R"]}", 0.1)

	write("\n", 0.02)
	write(f"{colors["GRAY"]}colossal: glenn chappell and ian cha{colors["R"]}", 0.1)

	write("\n", 0.02)
	write(f"{colors["GRAY"]}rebel: figlet font collection{colors["R"]}", 0.1)

	write("\n", 0.02)
	write(f"{colors["GRAY"]}small mono 12: figlet font collection{colors["R"]}", 0.1)

	write("\n", 0.02)
	write(f"{colors["GRAY"]}big mono 9: figlet font collection{colors["R"]}", 0.1)



	write("\n\n\n\n", 0.02)

	write(f"{colors["GRAY"]}website provider: nekoweb{colors["R"]}", 0.1)

	write("\n", 0.02)
	write(f"{colors["GRAY"]}javascript terminal library: jquery terminal{colors["R"]}", 0.1)



	write("\n\n\n\n", 0.02)

	write(f"{colors["WHITE"]}made with:{colors["R"]}", 0.1)

	write("\n", 0.02)
	write(f"{colors["GRAY"]}python{colors["R"]}", 0.1)

	write("\n", 0.02)
	write(f"{colors["GRAY"]}sublime text{colors["R"]}", 0.1)

	write("\n", 0.02)
	write(f"{colors["GRAY"]}microsoft paint{colors["R"]}", 0.1)



	write("\n\n\n\n", 0.02)

	write(f"{colors["WHITE"]}inspired by:{colors["R"]}", 0.1)

	write("\n", 0.02)
	write(f"{colors["PINK"]}doki doki literature club", 0.1)
	write(f"{colors["GRAY"]} by team salvato{colors["R"]}", 0.0)

	write("\n", 0.02)
	write(f"{colors["WHITE"]}milk inside a bag of milk inside a bag of milk", 0.1)
	write(f"{colors["GRAY"]} by nikita kryukov{colors["R"]}", 0.0)

	write("\n", 0.02)
	write(f"{colors["WHITE"]}milk outside a bag of milk outside a bag of milk", 0.1)
	write(f"{colors["GRAY"]} by nikita kryukov{colors["R"]}", 0.0)

	write("\n", 0.02)
	write(f"{colors["WHITE"]}looking up i only see a ceiling", 0.1)
	write(f"{colors["GRAY"]} by silver978{colors["R"]}", 0.0)

	write("\n", 0.02)
	write(f"{colors["WHITE"]}inscryption", 0.1)
	write(f"{colors["GRAY"]} by daniel mullins games{colors["R"]}", 0.0)

	write("\n", 0.02)
	write(f"{colors["WHITE"]}last seen online", 0.1)
	write(f"{colors["GRAY"]} by qwook{colors["R"]}", 0.0)



	write("\n\n\n\n", 0.02)

	write(f"{colors["WHITE"]}special thanks:{colors["R"]}", 0.1)

	write("\n", 0.02)
	write(f"{colors["GRAY"]}w3schools (for teaching me python, html, and javascript){colors["R"]}", 0.1)

	write("\n\n", 0.02)
	write(f"{colors["GRAY"]}ash{colors["R"]}", 0.1)

	write("\n", 0.02)
	write(f"{colors["GRAY"]}panda{colors["R"]}", 0.1)



	write("\n\n\n\n", 0.02)

	write(f"{colors["WHITE"]}pets:{colors["R"]}", 0.1)

	write("\n", 0.02)
	write(f"{colors["GRAY"]}sadie{colors["R"]}", 0.1)

	write("\n", 0.02)
	write(f"{colors["GRAY"]}blu{colors["R"]}", 0.1)

	write("\n", 0.02)
	write(f"{colors["GRAY"]}sir wallace{colors["R"]}", 0.1)

	write("\n", 0.02)
	write(f"{colors["GRAY"]}jamal{colors["R"]}", 0.1)

	write("\n", 0.02)
	write(f"{colors["GRAY"]}blueberry{colors["R"]}", 0.1)

	write("\n", 0.02)
	write(f"{colors["GRAY"]}coconut{colors["R"]}", 0.1)

	write("\n", 0.02)
	write(f"{colors["GRAY"]}rosie{colors["R"]}", 0.1)



	write("\n\n\n\n", 0.02)

	write(f"{colors["WHITE"]}you{colors["R"]}", 0.3)

	write("\n", 0.02)
	write(f"{colors["GRAY"]}thanks for playing {colors["R"]}", 0.2)
	write(f"bastille", 0.2, True)



	write("\n\n\n\n", 0.02)

	write(f"{colors["GRAY"]}© 2026 finlessfishy. all rights reserved.{colors["R"]}", 0.1)

	time.sleep(10.0)


