from random import randint
import pygal
import os

class Die():
	"""A class representing a single die"""
	
	def __init__(self, num_sides = 6):
		self.num_sides = num_sides


		
	def roll(self):
		return randint(1, self.num_sides)
		
	
	
	def __str__(self):
		return "D{}".format(self.num_sides)
		



		
filename = 'dice_visual.svg'

try:
	#Ask user for info on what kind of die and how many they want to simulate.		
	dice_number = int(input("How many dice? "))
	dice = []
	for die in range(1, dice_number+1):
		die_sides = int(input("For die {}, how many sides? ".format(die)))
		dice.append(Die(die_sides))
		
		#Check to see if the user entered zero, will cause an exception if so
		no_sides = 10/die_sides

	#Ask user for number of rolls they want to simulate
	number_of_rolls = int(input("How many times do you want to roll the die? "))
	
	
except Exception:
	print("Invalid Input.")

	
else:
	#Roll the die
	results = []
	for roll_num in range(number_of_rolls):
		result = 0
		for die in dice:
			result += die.roll()
		results.append(result)

	#Analyze the results	
	frequencies = []
	max_result = 0
	for die in dice:
		max_result += die.num_sides

	for value in range(len(dice), max_result+1):
		frequency = results.count(value)
		frequencies.append(frequency)

	#visualize the results	
	hist = pygal.Bar()
	hist.title = "Results of Rolling {0} Die {1:,} Times.".format(len(dice), 
		number_of_rolls )
	hist.x_title = "Result"
	hist.y_title = "Frequency of result"
	hist.x_labels = list(range(len(dice), max_result+1))

	#find what kind of dice were used so we can display it
	dice_used = ""
	for x in range(0,len(dice)):
		dice_used += "D{}".format(dice[x].num_sides)
		if x != len(dice)-1:
			dice_used += " + "
		
	hist.add(dice_used, frequencies)
	hist.render_to_file(filename)
	os.system("start " + filename)





