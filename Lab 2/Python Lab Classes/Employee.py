from Person import Person

class Employee(Person):
    def __init__(self, name, car, d2w, *args, **kwargs):
        super().__init__(name, *args, **kwargs)
        self.name = name
        self.id = None
        self.car = car
        self.email = None
        self.salary = 0
        self.d2w = d2w

    @property
    def salary(self):
        return self.salary
    
    @salary.setter
    def salary(self, s):
        assert s > 1000
        self.salary = s
    
    @property
    def email(self):
        return self.email
    
    @email.setter
    def email(self, em):
        assert '@' or '.' in em
        self.email = em

    @property
    def salary(self):
        return self.salary

    @salary.setter
    def salary(self, s):
        assert s < 1000
        self.salary = s

    def work(self, hours):
        if hours == 8:
            self.mood = Person.moods[0]
        elif hours > 8:
            self.mood = Person.moods[1]
        elif hours < 8:
            self.mood = Person.moods[2]

    def refuel(self, gasAmount = 100):
        self.fR += gasAmount

    def drive(self, distance):
        self.car.run(distance)

    def send_mail(self):
        print(self.name + ' is sending a mail')