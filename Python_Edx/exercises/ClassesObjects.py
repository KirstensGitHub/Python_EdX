
class Person:

	def __init__(self, inputName, inputAge, inputOccupation):
		self.name = inputName
		self.age = inputAge
		self.occupation = inputOccupation

	def __repr__(self):
		return str(self.name)+"(age-" + str(self.name) + "occupation-" + str(self.occupation) +")"

	def changeOccupation(self, newOccupation):
		self.occupation = newOccupation


#can type in terminal:
#>>>>bob = Person('Bob', 8, 'student')
#bob
#Bob (age-8 occupation-student)
#bob.changeOccupation('firefighter')
#bob
#Bob (age-8 occupation-firefighter)