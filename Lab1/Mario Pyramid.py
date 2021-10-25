def pyramid_drawer(num):
    k = num*2 - 2
    for i in range(1, num+1):
        for _ in range(0, k):
            print(' ', end='')
        k -= 2
        for _ in range(1, i+1):
            print('* ', end='')
        print()

def pyramid_drawer_v2(num):
    k = num*2 - 2
    for i in range(1, num+1):
        print(' ' * k, end='')
        k -= 2
        print('* ' * i)

if __name__ == '__main__':
    pyramid_drawer(4)
    pyramid_drawer_v2(4)