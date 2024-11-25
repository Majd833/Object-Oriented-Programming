class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
Blu=parrot("Blu",10)
Woo=parrot("Woo",15)
print("Blu is a {}".format(parrot.species))
print("Woo is also a {}".format(parrot.species))
print("{} is {} years old".format(Blu.name,Blu.age))
print("{} is {} years old".format(Woo.name,Woo.age))