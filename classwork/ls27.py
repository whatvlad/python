# class Human():
#     def __init__(self, name, surname, age, birth):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.birth = birth
#         print("Humans created")

#     def printout(self):
#         print(f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}, Birth : {self.birth}")

# human1 = Human("Vlad", "Tkachenko", 16, 2005)
# human1.printout()

# class Student(Human):
#     def studying(self):
#         print(f"Student: {self.name} is studying")


# class Teacher(Human):
#     def teaching(self):
#         print(f"Teacher {self.name} teaches")

# student = Student("SSS", "SSS", 19, 1999 ,m)

# student.printout()
# student.studying()

# teacher = Teacher("Den", "Dmitriev", 24, 1997)

# teacher.printout()
# teacher.teaching()









class Animal():
   def __init__(self, vid, name, age, color, razvitie, birth):
       self.vid = vid
       self.name = name
       self.age = age
       self.color = color
       self.razvitie = razvitie
       self.birth = birth

   def info(self):
       print(f"Вид: {self.vid}, Кличка: {self.name}, Возраст: {self.age}, Цвет: {self.color}, Развитие: {self.razvitie}, Year: {self.birth}")







class Dog(Animal):
    def bark(self):
        print(f"{self.vid} barking")

    def eattime(self):
        print(f"{self.name} is eating in 12:30, 15:00")


    def live(self):
        n = int(input("god: "))
        print(f"Живет {n - self.birth} года")




class Cat(Animal):
    def ymiv(self):
        print(f"{self.name} is ymivaetsa")

    def sidit(self):
        print(f"{self.name} sidit na okne")

    def live(self):
        n = int(input("god: "))
        print(f"Живет {n - self.birth} года") 



class Frog(Animal):
    def kva(self):
        print(f"{self.vid} kvakaet")

    def live(self):
        n = int(input("god: "))
        print(f"Живет {n - self.birth} года") 




a1 = Dog("Dog", "Pups", 2, "black", "norm", 2019)
a2 = Cat("Cat", "Murzik", 3, "rizhiy", "norm", 2018)
a3 = Frog("Frog", "Mik", 5, "green", "stariy", 2017)

print("-"*40)

a1.info()
a1.bark()
a1.eattime()
a1.live()

print("-"*40)

a2.info()
a2.ymiv()
a2.sidit()
a2.live()


print("-"*40)

a3.info()
a3.kva()
a3.live()



