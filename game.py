import cmd, sys, tarot

FLAIR = "********************************************************************************"
WELCOME = "\n\n Welcome to the Tarot game. To begin, set your intentions for this reading.\n\n"
INTENT_LIST = "~*~ Choose an intent from the list:\n\nRomance\nFuture\nGuidance\nClarity\nBrevity\n\n"
SIMPLE_RESPONSE = "\n ~*~ You are looking for a single card drawing, correct? [Y/N]   "
INCORRECT_INPUT = "~*~ Unfortunately that was not one of the options. Please check your spelling and try again."
HOLD = "\n\n~*~ Hold any specific question in your mind. When you're ready for your reading, press the Y key.   "
EXP = "\n\n ~*~ Thank you. Let's explore " 
pGUIDE = "your journey. \n\n"
pROMANCE = "your love life. \n\n"
pFUTURE = "your future. \n\n"
pCLARITY = "then. \n\n"
BEGIN = "\n\nLet's begin...\n"
W_INPUT = "\n\n ~*~ I'll wait until you're ready. When you are, press the Y key.   "
PARTNERQ = "\n~*~Do you currently have a partner? [Y/N]   "
GOALS = "\n~*~What do you want to learn about in this session? Choose a number:   \n\n1. Growth\n2. Transitions\n3. Advice\n\n"
RSPREAD_PARTNER = "\n\n~*~Should I do a 5 card spread to assess your relationship, or would you prefer the 6 card spread to see the future of your relationship? [5/6]   "
RSPREAD_SINGLE = "\n\nLet's do a 6-card spread to find you a compatible partner." + W_INPUT + "\n"
PARTNERED5C = "descriptions"
PARTNERED6C = "descriptions"
SINGLE6C = "descriptions"
GSPREAD_GROWTH = "descriptions"
GSPREAD_CHANGE = "descriptions"
GSPREAD_ADVICE = "descriptions"
POST_MAP = "Keep these meanings in mind as you look through the cards you are dealt."
LOOP_TEXT = " \n\n~*~ If you'd like another reading to clarify or to learn something else, press the Y key. If you'd like to exit, press any other key.   "

# single card spread
def single_card():
	conf = input(HOLD).lower()
	if conf == "y":
		tarot.spread(1)
		return
	else:
		print(W_INPUT)
		y = input()
		if y == "y":
			tarot.spread(1)
		else:
			get_started(1)


#romance spread-- draws 3 or 5 cards depending on
#user input. prints values + returns when complete
#input errors return to welcome page
#to-do -- type of romance spread (partnered/unpartnered)
def romance_spread():
	c = 0
	print("here: " + str(c))
	partnered = input(PARTNERQ).lower()
	# has partner
	if partnered == "y":
		# wants 5 card
		spread_choice =input(RSPREAD_PARTNER).lower()
		if spread_choice == "5":
			c = 5
			print("c is "+ str(c))
			print(PARTNERED5C)
		if spread_choice == "6":
			c = 6
			print(PARTNERED6C)
	if partnered == "n":
		if (input(RSPREAD_SINGLE)).lower == "y":
			c = 6
			print(SINGLE6C)
			#6 card spread map
	print("here now: " + str(c))
	if c == 0: get_started(1)
	tarot.spread(c)
	return


#future spread-- draws 3 or 5 cards depending on
#user input. prints values + returns when complete
#input errors return to welcome page
def future_spread():
	print()

#guidance spread-- draws 3 or 5 cards depending on
#user input. prints values + returns when complete
#input errors return to welcome page
def guidance_spread():
	spread_choice = input(GOALS)
	if spread_choice == "1":
		#spread map
		print(GSPREAD_GROWTH)
	elif spread_choice == "2":
		#spread map
		print(GSPREAD_CHANGE)
	elif spread_choice == "3":
		print(GSPREAD_ADVICE)
	else: 
		get_started(1)

def clarity_spread():
	print()

def get_started(n):
	if n == 0:
		print("\n\n"+FLAIR+WELCOME+FLAIR+"\n\n")
	elif n == 1:
		print("\n\n\n"+INCORRECT_INPUT)
	else: print('\n\n\n')
	intent = (input(INTENT_LIST)).lower()
	choose_mode(intent)

def start_loop():
	loop_bool = (input(LOOP_TEXT))
	if loop_bool != "y":
		exit()
	get_started(0)

def choose_mode(intent):
	match intent:
		case 'brevity':
			confirm = (input(SIMPLE_RESPONSE)).lower() 
			if confirm == 'y':    
				single_card()
				start_loop()
			elif confirm == 'n':
				print("\n\nOkay. Let's try again...\n\n")
				get_started(0)
			get_started(3)
		case 'romance':
			print(EXP + pROMANCE)
			romance_spread()
			start_loop()
		case 'guidance':
			print(EXP + pGUIDE)
			guidance_spread()
			start_loop()
		#case 'clarity': 
			#num = input(EXP + pCLARITY)
		case _:
			get_started(1)
		
	



# MAIN
choose_mode(get_started(0))
#if __name__ == "__main__":
#	main(sys.argv[1:])