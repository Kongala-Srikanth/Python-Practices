class Mobile:
    def __init__(self,model,price,color,camera):
        self.model = model
        self.price = price
        self.color = color
        self.camera = camera

    def features(slef,number):
        print("{} calling...".format(number))
        print("sms from this {}".format(number))
    
    def update(self,model):
        self.model = model

    
mobile_obj = Mobile(
    "IPhone11",
    "RS:89000",
    "Gold",
    "12MP"
)
mobile_obj.features(7075960802)

print(mobile_obj.model)
mobile_obj.update("samsung")
print(mobile_obj.model)