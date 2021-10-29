class Car:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.fuelRate = None
        self.velocity = 0
    
    @property
    def vel(self):
        return self.velocity
    
    @vel.setter
    def vel(self, v):
        assert 0 <= v <= 200
        self.velocity = v
    
    @property
    def fr(self):
        return self.fuelRate
    
    @fr.setter
    def fr(self, f):
        assert 0 <= f <= 100
        self.fuelRate = f

    def run(self, distance):
        pass

    def stop(self):
        pass