class Animal:
    def __init__(self, name: str, hunger=5, energy=5):
        self.name= name
        self.hunger = hunger
        self.energy = energy

    def __str__(self):
        return f'name: {self.name} \nhunger: {self.hunger} \nenergy: {self.energy}'

    def eat(self):
        amount=int(input("enter amount: "))
        if amount <= self.hunger*50:
            self.hunger -= amount//50
            self.energy -= amount//100
        else:
            eaten= self.hunger*50
            self.hunger=0
            self.energy -= eaten//100

    def play(self):
        duration = int(input("enter duration: "))
        if duration/10 <= 2*self.energy:
            self.hunger += 2*duration //10
            self.energy -= 2*duration//10
            if self.energy < 0:
                self.energy = 0
            if self.hunger > 10:
                self.hunger = 10
        else:
            print("game ended early because the animal is too tired")
            played= self.energy*10
            self.energy = 0
            self.hunger -= 2*played//10
            if self.energy < 0:
                self.energy = 0
            if self.hunger > 10:
                self.hunger = 10







dog=Animal('snowball')
print(dog)
print(dog.play())
print(dog)