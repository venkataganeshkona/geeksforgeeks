class Vehicles:
    name=""
    cost=0.0
    type=""
    def description(self):
        desc_str="%s %s of %d cost" %(self.name,self.type,self.cost)
        return desc_str

car1=Vehicles()
car2=Vehicles()

car1.name="Fer"
car1.cost=10000.00
car1.type="Red Convertible"

car2.name="Jump"
car2.cost=20000.00
car2.type="Jeep"

car1.description()

print car1.description()
print car2.description()