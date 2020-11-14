from tkinter import *
import json 
import tkinter.messagebox
from difflib import get_close_matches 
import goslate

window = Tk()

window.title("Dictionary")

gs = goslate.Goslate()
lang = {"English": "en", "French":"fr", "Tamil": "ta"}
drop_lang = ["English", "French", "Tamil"]

def word():
	#loads the dataset that holds the dictionary values
	data = json.load(open("data.json", encoding="utf-8"))
	word = e1_value.get().lower()
	count = 0
	
	if word in data:
		for x in data[word]:
			count = count + 1
		#used to clear the previous entries in the text box for the new output
		t1.configure(state='normal')
		t1.delete(1.0, END)
		t2.configure(state='normal')
		t2.delete(1.0, END)
		if variable.get() != "English":
			t2.insert(END, gs.translate(word.capitalize(),lang[variable.get()])  + "\n \n")
		else:
			t2.insert(END,word.capitalize()+ "\n \n")
		if count > 1:
			t2.insert(END, str(count) + " defintions were found")
		else:
			t2.insert(END, str(count) + " defintion was found")
		#outputs the definition of the word
		for x in data[word]:
			if variable.get() != "English":
				t1.insert(END, " - " + gs.translate(x, lang[variable.get()]) + "\n \n")
			else:
				t1.insert(END, " - " + x + "\n \n")
		#ensures the content in the text window can't be edited
		t1.configure(state='disabled')
		t2.configure(state='disabled')

	#handles the word not in the dictionary or a spelling error
	else:
		alts = get_close_matches(word, data.keys(), cutoff=0.6)
		if len(alts) > 0:
			result = tkinter.messagebox.askquestion("Unrecognized Word", "Did you mean * " + alts[0] + " *?", icon='warning')
			if result == "yes":
				for x in data[alts[0]]:
					count = count + 1
				#returns definition(s) of alternate word suggested
				t1.configure(state='normal')
				t1.delete(1.0, END)
				t2.configure(state='normal')
				t2.delete(1.0, END)
				if variable.get() != "English":
					t2.insert(END, gs.translate(alts[0].capitalize(),lang[variable.get()])  + "\n \n")
				else:
					t2.insert(END,alts[0].capitalize()+ "\n \n")
				if count > 1:
					t2.insert(END, str(count) + " defintions were found")
				else:
					t2.insert(END, str(count) + " defintion was found")  
				for x in data[alts[0]]:
					if variable.get() != "English":
						t1.insert(END, " - " + gs.translate(x, lang[variable.get()]) + "\n \n")
					else:
						t1.insert(END, " - " + x + "\n \n")
				t1.configure(state='disabled')
				t2.configure(state='disabled')

			else:
				t1.configure(state='normal')
				t1.delete(1.0, END)
				t2.configure(state='normal')
				t2.delete(1.0, END)
				tkinter.messagebox.showinfo("Unrecognized Word", "Please check spelling")
				t2.insert(END, "No defintions were found")
				t1.configure(state='disabled')
				t2.configure(state='disabled')

#Tkinter widgets 
b1 = Button(window, text="Define", command=word, pady = 5, padx=5)
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
t1 = Text(window, height=20, width=50, font="Arial", padx="5" ,pady="5", wrap=WORD)
t2 = Text(window, height=5, width=50, font="Arial 18 bold", padx="20")
e1.pack()
b1.pack()
variable = StringVar(window)
variable.set(drop_lang[0])
w = OptionMenu(window, variable, *drop_lang)
w.pack()
t2.pack()
t1.pack()

window.mainloop()