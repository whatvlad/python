class Shop:
    def __init__(self,shop_name,store_type):
        self.shop_name=shop_name
        self.store_type=store_type
        self.number_of_units=0
    def describe_shop(self):
        print(self.shop_name,self.store_type)
    def open_shop(self):
        print(f"Онлайн магазин {self.shop_name} відкритий!")
    def set_number_of_units(self,n):
        self.number_of_units=n
        print(f"У нас є {self.number_of_units} видів різних товарів!")
    def increment_number_of_units(self,m):
        self.number_of_units+=m
        print(f"Тепер кількість виду товарів дорівнює {self.number_of_units}")

class Discount(Shop):
    def __init__(self,shop_name,store_type):
        Shop.__init__(self,shop_name,store_type)
        self.discount_products=0
    def get_discounts_products(self):
        self.discount_products=["product1","product2","product3","product4"]
        print("Товари на які зараз є знижка:")
        for i in self.discount_products:    
            print(i)
       
    

