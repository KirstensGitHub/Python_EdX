#this is an example of a python UI
#copied directly from course lecture
#from week 8 describing loops

def menu():
	print "(1) Enter event name."
	print "(2) Enter a new attendee."
	print "(3) Show current attendees."
	print "(5) Quit."

def main():
	event_name="Default Name"
	attendees=[]
	while True:
		print "\nThe event is", event_name,"."
		menu()

	uc= input("Choose an option: ")

	if uc == 5:
		break
	elif uc == 1:
		event_name = raw_input("Enter the event name: ")
	elif uc ==2:
		attendees.append(raw_input("Enter the attendee's name: "))
		print "\nThe list of attendees for", event_name,"is:", attendees,"."
	else:
		print "\nThat's not on the menu!"
	
	print
	print "You have quit the program."

