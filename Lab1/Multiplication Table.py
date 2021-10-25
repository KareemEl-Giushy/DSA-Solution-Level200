def muli_table(number):
    lst = []
    for i in range(1, number + 1):
        l = []
        for n in range(1, i+1):
            l.append(i * n)
        
        lst.append(l)
    
    return lst

if __name__ == '__main__':
    print(muli_table(3))