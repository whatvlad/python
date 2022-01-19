# class Human:
#     def __init__(self,name,surname,place_of_birth,year_of_birth):
#         self.name = name
#         self.surname = surname
#         self.place_of_birth = place_of_birth
#         self.year_of_birth = year_of_birth

#     def hello(self):
#         print(f"{self.name} says hello")


#     def info_year(self, years):
#         return print(years-self.year_of_birth)

#     def info(self):
#         print(f"Name: {self.name}, surname: {self.surname}, place of birth: {self.place_of_birth}, year: {self.year_of_birth}")



# a = Human("Vlad", "aasdddsadsa", "Ukraine", 2005)
# a.hello()
# a.info_year(2021)
# a.info()





class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("person created")

    def hello(self):
        print(f"{self.name} says hello")


class Student(Human):
    def __init__(self,name,age, course, mark):
        Human.__init__(self,name,age)
        self.course = course
        self.mark = mark

    def study(self):
        print(f"{self.name} studying")
    
    def hello(self):
        print(f"Student created, {self.name} not says hello")

    def info_university(self):
        print(f"студент под именем {self.name}, который учится на {self.course} курсе, который имеет оценку за первый семестр {self.mark}")

class Teacher(Human):
    def teach(self):
        print(f"{self.name} - teaches, age:{self.age}")



a = Student("Vlad", 16, 0, 0)
b = Teacher("Den", 25)
a.hello()
a.info_university()
# a.hello()
# b.hello()
# a.study()
# b.teach()
