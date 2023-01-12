############################################################
#                           OPPS
############################################################
class Mobile:
    
    def __init__(self,brand,ram,camera,storage,battery,color,price):
        self.brand = brand
        self.ram = ram
        self.camera = camera
        self.storage = storage
        self.battery = battery
        self.color = color
        self.price = price

    def get_warranty(self,warranty):
        print("Warrany",warranty)

    def spec(self):
        print("Brand",self.brand)
        print("Camera",self.camera)
        print("Storage",self.storage)
        print("Battery",self.battery)
        print("Color",self.color)
        print("Price",self.price)


brand = input("Enter Brand: ")
ram = input("Enter Ram: ")
storage = input("Enter Storage: ")
camera = input("Enter Camera: ")
battery = input("Enter Battery: ")
color = input("Enter Color: ")
price = input("Enter Price: ")
warranty = input("Enter Warranty: ")

print("_"*25)
print("Mobile Specifications ")
print()

mob = Mobile(brand,ram,camera,storage,battery,color,price)
mob.spec()
mob.get_warranty(warranty)
