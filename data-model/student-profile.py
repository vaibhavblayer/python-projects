# student-profile.py
# student profile - data-modeling


class Student:
	def __init__(self, name, subject, location):
		self.name = name
		self.subject = subject
		self.location = location

	def __str__(self):
		return 'Student with name {0}, {1} from {2}'.format(self.name, self.subject, self.location)


names = ['Vaibhav', 'Stark', 'Tony', 'Steve', 'Clint']
subjects = ['Physics', 'Maths', 'Python', 'JavaScript', 'Swift']
locations = [i for i in range(600)] 

dict = {'Physics': 'Mechanics', 'Maths': 'Calculus', 'Python': 'Tuple'}


if __name__ == '__main__':
	for name, subject, location in zip(names, subjects, locations):
		print name, subject, location


	for i in range(100):
		dict[i] = i**2

	

		
