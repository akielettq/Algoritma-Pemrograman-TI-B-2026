class Person:  # Ini yang parent class
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):  # Ini yang child class 
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)  # Make super() bakalan bikin bisa akses semua method dan properti dari parentnya
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x.welcome()