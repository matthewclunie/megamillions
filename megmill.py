"""
Program:MegaMillions.py
Author: Matthew 11/22/2021


*** Note: the file breezypythongui.py MUST be in the
same directory as this file for the application to work
"""
import random
from breezypythongui import EasyFrame
from tkinter.font import Font

class MegaMill(EasyFrame):
	def __init__(self):
		"""Sets up the window and the widgets."""
		EasyFrame.__init__(self, title = "Mega Millions!", background = "MistyRose", width = 380, height = 260)

		#Slot Machine Title
		self.addLabel(text = "Mega Millions!", row = 0, column = 0, columnspan = 5, background = "LightCoral", foreground = "PapayaWhip", font = Font(family = "Impact", size = 28), sticky = "NSEW")

		#Command Button
		self.playButton = self.addButton(text = "PLAY!", row = 3, column = 0, columnspan = 5, command = self.slots)
	
		#Label for the MegaBall message!
		self.outputLabel = self.addLabel(text = "", row = 4, column = 0, columnspan = 5, sticky = "NSEW", background = "DarkSeaGreen", foreground = "PapayaWhip", font = Font(family = "Georgia", size = 32))
		
	#Event Handling Method
	def slots(self):

		columnCount = 0
		num = random.randint(1, 9)

		while columnCount < 5:
			self.announce = self.addLabel(text = "The Ball:", row = 1, column = columnCount)
			self.numField1 = self.addIntegerField(value = num, row = 2, column = columnCount)
			num = random.randint(1, 70)
			columnCount += 1

		self.outputLabel["text"] = random.randint(1, 25)

#Definition of the main() function for program entry
def main(): 
	"""Instantiates and pops up the window."""
	MegaMill().mainloop()

#Global call to trigger the main function
if __name__ == "__main__":
	main()
