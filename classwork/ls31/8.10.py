class Rectangle:
    def __init__(self,a1,a2):
        self.a1=a1
        self.a2=a2
    def plosha(self):
        pl=a1*a2
        print(f"Площадь прямоугольника равна {pl}")
        
a1=int(input("Введите сторону а1 прямоугольника --> "))
a2=int(input("Введите сторону а2 прямоугольника --> "))
p1=Rectangle(a1,a2)
p1.plosha()
