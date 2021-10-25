from webbrowser import open as wopen
from random import randint

if __name__ == '__main__':
    lst = ['https://www.google.com', 'https://www.yahoo.com', 'https://www.gmail.com', 'https://www.facebook.com']
    wopen(lst[randint(0, len(lst))])