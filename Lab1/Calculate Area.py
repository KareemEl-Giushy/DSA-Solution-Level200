class CalcArea:
    def __init__(self, t, w = None, h = None):
        self.type = t.lower()
        self.width = w
        self.height = h
        self.main()
    
    def main(self):
        if self.type == 't':
            print(self.triangle())
        elif self.type == 'r':
            print(self.rectangle())
        elif self.type == 'c':
            print(self.circle())
        else:
            print('Not Supported Type !')
    
    def triangle(self):
        if not self.width or not self.height:
            raise Exception('You have To Input Base & Height !')
        return 0.5 * self.width * self.height
    
    def rectangle(self):
        if not self.width:
            raise Exception('You Have To Input Width !')
        elif not self.height:
            return self.width ** 2
        else:
            return self.width * self.height

    def circle(self):
        if not self.width:
            raise Exception('You Have To Input Radius !')
        return 3.14 * (self.width ** 2)


if __name__ == '__main__':
    Area = CalcArea('r', 10)
    Area = CalcArea('r', 10, 30)
    Area = CalcArea('t', 10, 10)
    Area = CalcArea('c', 10)