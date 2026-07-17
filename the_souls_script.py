# the soul's script

import getpass



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



closet = []
kitchen = []
chapters = []

chapter1 = [
	"i'm quietly walking to the living room. 1:56 am.",

	"she's sleeping on the couch to make sure i don't leave my room again.",
	"i sneak past.",
	"i try to open the front door.",
	"she wakes up and sees me.",
	f"{colors["RED"]}she beats me until i collapse.{colors["R"]}",

	"...",

	"i wake up. i'm still on the floor where she left me.",
	"she's asleep again, snoring too loud.",
	"i don't want to look in the mirror.",
	"i think of attempting to leave again,",
	"but i know there's no point.",
	"she'll just catch me and break my nose again.",

	"...",

	"i go back to my bedroom.",
	"i lay down.",
	"i don't want to look in the mirror.",
	"i try to sleep.",
	"the constant itching of my flesh keeps me awake.",
	"i claw at my skin.",
	"it feels unfamilar.",
	"like it's not supposed to be there.",
	"i feel like i'm losing my mind.",
	"i feel like i'm losing my mind.",
	"i don't want to look in the mirror.",
	"my flesh prison is becoming unbearable.",
	"i can't look in the mirror.",
	"i need to get out.",
	"i need to get out of here.",
]

chapter2 = [
	f"{colors["RED"]}i need to get out of my prison.{colors["R"]}",
	f"{colors["RED"]}i grab the kitchen knife from my nightstand.{colors["R"]}",
	f"{colors["RED"]}i cut a hole into the center of my face.{colors["R"]}",
	"i slowly blink and the knife is gone, and my face is intact.",
	"the knife was never there.",
	"i've never had a knife.",
	"knives were never real.",
	"knives have never existed.",
	"i feel like i'm losing my mind.",
	"i feel like i'm losing my mind.",
	f"{colors["RED"]}i feel like i'm losing my mind.{colors["R"]}",
	"i'm losing my mind.",
	"i'm losing my mind.",
	"i'm losing my mind.",
	f"{colors["RED"]}i'm losing my mind.{colors["R"]}",
	f"{colors["RED"]}i'm losing my mind.{colors["R"]}",

	"...",
	"...",

	"i need to get out.",
	f"{colors["RED"]}i need to get out.{colors["R"]}",
	f"{colors["RED"]}i need to get out.{colors["R"]}",
	f"{colors["RED"]}i need to get out.{colors["R"]}",
	f"{colors["RED"]}i open the dusty door to the attic.{colors["R"]}",
	f"{colors["RED"]}i look around. my empty eyes find a shotgun in a dark corner.{colors["R"]}",
	f"{colors["RED"]}i grab the shotgun and sit down on the floor, back to the wall.{colors["R"]}",
	f"{colors["RED"]}i settle the lengthy barrel of the shotgun into my mouth.{colors["R"]}",
	f"{colors["RED"]}...{colors["R"]}",
	f"{colors["RED"]}i squeeze the trigger.{colors["R"]}",
	f"{colors["RED"]}...{colors["R"]}",
	f"{colors["RED"]}my sight goes black.{colors["R"]}",
	f"{colors["RED"]}...{colors["R"]}",
	f"{colors["RED"]}my hearing goes black.{colors["R"]}",
	f"{colors["RED"]}...{colors["R"]}",
	f"{colors["RED"]}my mind goes black.{colors["R"]}",
	f"{colors["RED"]}...{colors["R"]}",
	f"{colors["RED"]}the shotgun goes black.{colors["R"]}",
	f"{colors["RED"]}...{colors["R"]}",
	f"{colors["RED"]}my head goes black.{colors["R"]}",
	f"{colors["RED"]}...{colors["R"]}",
	f"{colors["RED"]}the room goes black.{colors["R"]}",
	f"{colors["RED"]}...{colors["R"]}",
	f"{colors["RED"]}everything goes black.{colors["R"]}",
	f"{colors["RED"]}...{colors["R"]}",
	f"{colors["RED"]}...{colors["R"]}",
	f"{colors["RED"]}...{colors["R"]}",
]

chapter3 = [
	f"{colors["RED"]}...{colors["R"]}",
	f"{colors["RED"]}...{colors["R"]}",
	f"{colors["RED"]}...{colors["R"]}",

	"...",
	"...",
	"...",

	"i wake up in a cold, dark place.",
	f"{colors["RED"]}it feels like it's been months.{colors["R"]}",
	"i'm laying uncomfortably on the floor, in a dark corner of the basement.",
	"it feels off.",
	"where is she?",
	"why am i here?",
	"did it not work?",
	"is this the afterlife?",

	"...",

	"i get up on unsteady legs, almost stumbling over.",
	"i thought there used to be a window down here, but there's nothing now.",
	"i try to open the basement door.",
	"it doesn't move.",
	"i try again.",
	"it turns to dust.",
	"no, it doesn't.",
	"i'm losing my mind.",
	"something is definitely wrong.",
	"i should be dead, right?",
	"maybe i am dead.",
	"i kick the door.",
	"it doesn't even make a sound when it hits the wood.",
	"this isn't real.",
	"this can't be real.",
	"i grab the scissors laying on the ground.",
	"i jab the scissors into the door.",
	"i realize that there are no scissors in my hand,",
	"or in the door, and that the door is wide open.",
	"it was always open.",
	"there were never any scissors.",
	"who would keep scissors down here, anyway?",
	"i'm losing my mind.",
	"i'm losing my mind.",
	"i'm losing my fucking mind.",
]

chapter4 = [
	"i'm losing my mind.",
	"i walk out of the basement.",
	"this has to be a dream or something.",
	"maybe i'm just going insane.",
	"it's probably just that.",
	"she's nowhere to be found, and all furniture that was once in this house has disappeared.",
	"the walls are covered with so many clocks i can't see the dull gray paint under them,",
	"and the floor is littered with random lamps, some turned off, some turned on, most flickering violently.",
	"i explore the twisted, nightmarish version of my house.",
	"one of the rooms' walls are covered in butterflies, and another is completely empty.",
	"what the fuck?",
	"i enter another room.",
	"this time its walls are covered in renaissance paintings.",
	"i've definitely found more rooms that there used to be in this house.",
	"what the fuck is going on?",
	"i enter another.",
	"this time, its walls and floor are both full of dull,",
	"aged light bulbs.",
	"what the fuck?",
	"what the actual fuck is going on?",
	"what the fuck is happening?",
	"what the fuck is happening to me?",
	"why are you doing this to me?",
	"why are you making me go insane?",
	"...",
	"answer me.",
	"...",
	"i know you're watching me.",
	"don't ignore me.",
	f"{colors["RED"]}don't ignore me.{colors["R"]}",
	f"{colors["RED"]}don't ignore me, {getpass.getuser()}.{colors["R"]}",
	"do you really think i didn't notice you?",
	"did you really think i wouldn't realize that my world is literally just text?",
	"really?",
	"really?",
]


