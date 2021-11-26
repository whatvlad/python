


def month_to_season(number):
  if number == 3 or number == 4 or number == 5:
    print("Сезон - весна")
  elif number == 6 or number == 7 or number == 8:
    print("Сезон - лето")
  elif number == 9 or number == 10 or number == 11:
    print("Сезон - осень")
  elif number == 12 or number == 1 or number == 2:
    print("Сезон - зима")
  else:
    print("Ошибка!")


n = int(input("Введите номер месяца: "))
month_to_season(n)






