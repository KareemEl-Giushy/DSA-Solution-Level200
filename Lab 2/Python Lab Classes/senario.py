from Person import Person

if __name__ == '__main__':
    x = Person('kareem')
    x.sleep(5)
    x.hr = 99
    x.eat(2)
    print(x.healthRate)
    print(x.mood)