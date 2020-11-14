def word():
	data = json.load(open("dictionary.json"))
	word = str(input("What word are you looking for? ")).lower()
	#keeps count of the number of definitions returned
	count = 0
	if word in data:
		for x in data[word]:
			count = count + 1
		#returns definition(s) of word inputted 
		print(count, "definition(s) was found:") 
		print(data[word])    
		#for x in data[word]:
		#   print("-", x)

	else:
		alts = get_close_matches(word, data.keys(), cutoff=0.6)
		print("Sorry, this word is not in the dictionary.")
		if len(alts) > 0:
			print("Did you mean *", alts[0], "*? Y\\N")
			different_word = str(input())
			if different_word == "Y" or "y" or "yes":
				for x in data[alts[0]]:
					count = count + 1
				#returns definition(s) of word inputted 
				print(count, "definition(s) was found:")  
				print(data[alts[0]])   
				#for x in data[alts[0]]:
				#    print("-", x)

			else:
				print("Please check spelling.")

		 
word()