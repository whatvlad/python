from shop import *

shop1=Shop("Adidas","одяг")
shop1.describe_shop()
shop1.open_shop()
shop2=Shop("Rozetka","електроніка")
shop2.describe_shop()
n=int(input("Задайте кількість видів товару --> "))
shop1.set_number_of_units(n)
m=int(input("Задайте кількість новіх видів товарів після завезеня --> "))
shop1.increment_number_of_units(m)
store_discount=Discount("Nike","одяг")
store_discount.get_discounts_products()
all_store=Shop("Comfi","електроніка")
all_store.describe_shop()