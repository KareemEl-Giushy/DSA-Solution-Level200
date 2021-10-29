class Person:
    moods = ('happy', 'tired', 'lazy')
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.money = 0
        self.mood = None
        self.healthRate = None

    @property
    def hr(self):
        return self.healthRate
    
    @hr.setter
    def hr(self, hr):
        assert 0 < hr < 100
        self.healthRate = hr

    def sleep(self, hours):
        if hours == 7:
            self.mood = Person.moods[0]
        elif hours < 7:
            self.mood = Person.moods[1]
        elif hours > 7:
            self.mood = Person.moods[2]

    def eat(self, meals):
        assert meals in [1, 2, 3]
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50
    
    def buy(self, *items):
        self.money -= (10 * len(items))
