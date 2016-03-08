def clapyourhands():
	print "clap clap"
def stompyourfeet():
	print "stomp stomp"



def main():
	yourehappy = (raw_input("""Are you happy? Yes or No >>> """)) == "Yes"
	youknowit = (raw_input("""Are you happy and you know it, Yes or No >>> """)) == "Yes"

	if yourehappy and youknowit:
		clapyourhands()
		stompyourfeet()

	print "Good bye"
main()
