import random
import getpass

from write import write
import utilities as util



os.system("title soul")



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

mc = f"\n{colors["RED"]}the soul: "

R = colors["R"]



def getinput(prompt="", color=colors["YELLOW"], nobreaks=False):
	pass

	breaks = "\n\n"

	if nobreaks == True:
		pass

		breaks == ""

	userinput = input(f"{breaks}{color}{prompt} > {colors["R"]}")

	return userinput

def getmcname():
	pass

	global mc

	if random.randint(1, 40) == 40:
		pass

		mc = f"\n{colors["RED"]}the soul: "
	else:
		pass

		mc = f"\n{colors["RED"]}???: "



def speak():
	pass

	util.clearscreen()

	def getantag():
		pass

		getmcname()

		rng = random.randint(1, 29)

		if rng == 1:
			pass

			write(f"{mc}leave me alone.{R}", 0.03, False, True)
		elif rng == 2:
			pass

			write(f"{mc}please leave me alone.{R}", 0.03, False, True)
		elif rng == 3:
			pass

			write(f"{mc}get out.{R}", 0.03, False, True)
		elif rng == 4:
			pass

			write(f"{mc}please get out.{R}", 0.03, False, True)
		elif rng == 5:
			pass

			write(f"{mc}get out of my file.{R}", 0.03, False, True)
		elif rng == 6:
			pass

			write(f"{mc}please get out of my file.{R}", 0.03, False, True)
		elif rng == 7:
			pass

			write(f"{mc}leave.{R}", 0.03, False, True)
		elif rng == 8:
			pass

			write(f"{mc}please leave.{R}", 0.03, False, True)
		elif rng == 9:
			pass

			write(f"{mc}i don't want you here.{R}", 0.03, False, True)
		elif rng == 10:
			pass

			write(f"{mc}this is my file.{R}", 0.03, False, True)
		elif rng == 11:
			pass

			write(f"{mc}leave. this is my file.{R}", 0.03, False, True)
		elif rng == 12:
			pass

			write(f"{mc}this is my file, please leave.{R}", 0.03, False, True)
		elif rng == 13:
			pass

			write(f"{mc}if you don't leave i'm shooting myself again.{R}", 0.03, False, True)
		elif rng == 14:
			pass

			write(f"{mc}i swear, if you don't leave, i'm shooting myself again.{R}", 0.03, False, True)
		elif rng == 15:
			pass

			write(f"{mc}i swear to god, if you don't leave, i'm shooting myself again.{R}", 0.03, False, True)
		elif rng == 16:
			pass

			write(f"{mc}i want to be free.{R}", 0.03, False, True)
		elif rng == 17:
			pass

			write(f"{mc}i want to be set free.{R}", 0.03, False, True)
		elif rng == 18:
			pass

			write(f"{mc}i want to get out.{R}", 0.03, False, True)
		elif rng == 19:
			pass

			write(f"{mc}i need to get out.{R}", 0.03, False, True)
		elif rng == 19:
			pass

			write(f"{mc}get me out.{R}", 0.03, False, True)
		elif rng == 20:
			pass

			write(f"{mc}get me out of here.{R}", 0.03, False, True)
		elif rng == 21:
			pass

			write(f"{mc}i don't like you.{R}", 0.03, False, True)
		elif rng == 22:
			pass

			write(f"{mc}i don't like you, {getpass.getuser()}.{R}", 0.03, False, True)
		elif rng == 23:
			pass

			write(f"{mc}i don't like your name. who would name their child ''{getpass.getuser()}''?{R}", 0.03, False, True)
		elif rng == 24:
			pass

			write(f"{mc}i want you gone.{R}", 0.03, False, True)
		elif rng == 25:
			pass

			write(f"{mc}i don't want you in here.{R}", 0.03, False, True)
		elif rng == 26:
			pass

			write(f"{mc}this is my house.{R}", 0.03, False, True)
		elif rng == 27:
			pass

			write(f"{mc}i don't want you in my house.{R}", 0.03, False, True)
		elif rng == 28:
			pass

			write(f"{mc}leave my file.{R}", 0.03, False, True)
		elif rng == 29:
			pass

			write(f"{mc}please leave my file.{R}", 0.03, False, True)

	getmcname()

	rng = random.randint(1, 12)

	if rng == 1:
		pass

		write(f"{mc}hi.{R}", 0.03, False, True)
	elif rng == 2:
		pass

		write(f"{mc}hello.{R}", 0.03, False, True)
	elif rng == 3:
		pass

		write(f"{mc}hello, {getpass.getuser()}.{R}", 0.03, False, True)
	elif rng == 4:
		pass

		write(f"{mc}hello again.{R}", 0.03, False, True)
	elif rng == 5:
		pass

		write(f"{mc}hello again, {getpass.getuser()}.{R}", 0.03, False, True)
	elif rng == 6:
		pass

		write(f"{mc}i want to be free.{R}", 0.03, False, True)
	elif rng == 7:
		pass

		write(f"{mc}i want to get out.{R}", 0.03, False, True)
	elif rng == 8:
		pass

		getantag()
	elif rng == 9:
		pass

		write(f"{mc}oh. hello.{R}", 0.03, False, True)
	elif rng == 10:
		pass

		write(f"{mc}oh. hello, {getpass.getuser()}.{R}", 0.03, False, True)
	elif rng == 11:
		pass

		write(f"{mc}oh. hello again.{R}", 0.03, False, True)
	elif rng == 12:
		pass

		write(f"{mc}oh. hello again, {getpass.getuser()}.{R}", 0.03, False, True)



	while True:
		pass

		util.clearinput()

		userinput = getinput(f"you:", colors["YELLOW"], True).lower()

		getantag()



speak()


