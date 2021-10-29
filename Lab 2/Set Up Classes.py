class Person:
    def __init__(self, name, money, mood, heathRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.hth = heathRate

    def sleep(self, hours):
        if hours == 7:
            self.mood = 'Happy'
        elif hours > 7:
            self.mood = 'Lazy'
        elif hours < 7:
            self.mood = 'Tired'

    def eat(self, meals):
        if meals == 3:
            self.hth = 100
        elif meals == 2:
            self.hth = 75
        elif meals == 1:
            self.hth = 50
    def buy(self, items):
        for _ in range(items):
            self.money -= 10

class Car:
    def __init__(self, name, fuelRate, velocity) -> None:
        self.name = name
        self.fR = fuelRate
        self.vel = velocity
    
    def run(self, distance, velocity):
        self.vel = velocity
        self.fR -= 5

    def stop(self):
        print('Car Has Stopped.')


class Employee(Person, Car):
    def __init__(self, name, money, mood, heathRate, eid, car, email, sarry, d2w):
        super().__init__(name, money, mood, heathRate)
        # Person.__init__()
        self.id = eid
        self.car = car
        self.email = email
        self.sarry = sarry
        self.d2w = d2w
    
    def work(self, hours):
        if hours == 8:
            self.mood = 'Happy'
        elif hours > 8:
            self.mood = 'Tired'
        elif hours < 8:
            self.mood = 'Lazy'

    def refuel(self, gasAmount = 100):
        self.fR += gasAmount

    def drive(self, distance, velocity):
        self.run(distance, velocity)

    def send_mail(self):
        print(self.name + ' is sending a mail')

class Office:
    def __init__(self, name, employees):
        self.name = name
        self.emps = employees
    
    def get_all_employees(self):
        pass

    def get_employee(self):
        pass

    def hire(self):
        pass

    def fire(self):
        pass

    def calculate_lateness(self):
        pass
    
    def deduct(self):
        pass

    def reward(self):
        pass