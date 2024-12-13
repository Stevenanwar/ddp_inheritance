from Parent_Class import *

class Student (Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

object = Student("Reza", "Maulana", 2020)
object.welcome()
